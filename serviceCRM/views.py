from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .forms import InputForm, CloseForm
from .models import Insert, TicketLog
from .tables import DoneInsertTable, InsertTable
from .filter import InsertFilter, DoneFilter

from django_tables2.views import SingleTableMixin,SingleTableView
from django_filters.views import FilterView
from datatableview.views import DatatableView

class InsertListView(LoginRequiredMixin, SingleTableMixin, FilterView):
    model = Insert
    table_class = InsertTable
    template_name = 'serviceCRM/list.html'
    filterset_class = InsertFilter

    def get_queryset(self):
        return Insert.objects.filter(done=False).order_by('-date', '-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Dashboard Widgets Data
        context['stats_active'] = Insert.objects.filter(done=False).count()
        context['stats_today_closed'] = Insert.objects.filter(done=True, date_close=timezone.now().date()).count()
        context['stats_ready'] = Insert.objects.filter(status='READY', done=False).count()
        return context
  
class InsertNew(generic.View):
    model = Insert
    template_name = "serviceCRM/form.html"

    @login_required
    def insert(request):
        if request.method == 'POST':
            form = InputForm(request.POST)
            if form.is_valid():
                ticket = form.save()
                TicketLog.objects.create(ticket=ticket, action="Креирано", details="Налогот е креиран во системот.")
                return HttpResponseRedirect(f"/ticket/{ticket.ticket_id}/")
        else:
            form = InputForm()

        return render(request, InsertNew.template_name, {'form': form})

class Update(LoginRequiredMixin, generic.UpdateView):
    model = Insert
    template_name = "serviceCRM/edit.html"
    fields = ["status", "name", "phone", "description","note", "repair", "plateno", "done"]
    success_url = '/'
    slug_field = 'ticket_id'
    slug_url_kwarg = 'ticket_id'

    def form_valid(self, form):
        response = super().form_valid(form)
        if 'status' in form.changed_data:
            TicketLog.objects.create(ticket=self.object, action="Промена на статус", details=f"Статусот е променет во {self.object.get_status_display()}")
        else:
            TicketLog.objects.create(ticket=self.object, action="Ажурирано", details="Деталите за налогот се ажурирани.")
        return response

class CloseTicketView(LoginRequiredMixin, generic.UpdateView):
    model = Insert
    form_class = CloseForm
    template_name = "serviceCRM/close_ticket.html"
    success_url = '/done/'
    slug_field = 'ticket_id'
    slug_url_kwarg = 'ticket_id'

    def form_valid(self, form):
        form.instance.done = True
        form.instance.date_close = timezone.now().date()
        response = super().form_valid(form)
        TicketLog.objects.create(ticket=self.object, action="Затворено", details="Налогот и поправката се завршени.")
        return response


@login_required
def Nalog(request, ticket_id):
    data = get_object_or_404(Insert, ticket_id=ticket_id)
    template = "serviceCRM/nalog.html"
    context = {"data": data}
    return render(request, template, context)

@login_required
def print_label(request, ticket_id):
    ticket = get_object_or_404(Insert, ticket_id=ticket_id)
    return render(request, 'serviceCRM/print_label.html', {'ticket': ticket})

@login_required
def print_receipt(request, ticket_id):
    ticket = get_object_or_404(Insert, ticket_id=ticket_id)
    return render(request, 'serviceCRM/print_receipt.html', {'ticket': ticket})
    
class Done(LoginRequiredMixin, SingleTableMixin, FilterView):
    model = Insert
    table_class = DoneInsertTable
    template_name = 'serviceCRM/done.html'
    filterset_class = DoneFilter
    
    def get_queryset(self):
        return Insert.objects.filter(done=True)
    
    @login_required
    def done_by_id(request, ticket_id):
        req = get_object_or_404(Insert, ticket_id=ticket_id)
        return HttpResponse(f"Report ID: {ticket_id} \nName: {req.name} \nPhone: {req.phone} \nDescription: {req.description} \n Note:{req.note} \nDate: {req.date} \nDone: {req.done} \nRepair: {req.repair} \n Plateno: {req.plateno} \n")

class Delete(generic.View):
    model = Insert

    @login_required
    def delete(request, ticket_id):
        req = get_object_or_404(Insert, ticket_id=ticket_id)
        req.delete()
        return HttpResponseRedirect("/")
    
class DatatableView(LoginRequiredMixin, DatatableView):
    model = Insert
    template_name = 'serviceCRM/Insert_list.html'
def track_ticket(request):
    if request.method == 'GET' and 'ticket_id' in request.GET:
        ticket_id = request.GET.get('ticket_id').strip()
        try:
            ticket = Insert.objects.get(ticket_id=ticket_id)
            return render(request, 'serviceCRM/public_track_result.html', {'ticket': ticket})
        except Insert.DoesNotExist:
            return render(request, 'serviceCRM/public_track_form.html', {'error': 'Налогот не е пронајден. Проверете го бројот на налогот.'})
            
    return render(request, 'serviceCRM/public_track_form.html')    
def logout_view(request):
    logout(request)
    return redirect('/')

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return track_ticket(request)
