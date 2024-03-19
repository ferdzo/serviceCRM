from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic import UpdateView
from .forms import InputForm
from .models import Insert
from .tables import DoneInsertTable, InsertTable
from django_tables2 import SingleTableView
class InsertListView(SingleTableView):
    model = Insert
    table_class = InsertTable
    template_name = 'serviceCRM/list.html'

# class ReportById(generic.DetailView):
#     model = Insert
#     template_name = "serviceCRM/id.html"
#     def ReportById(request, question_id):
#         req = get_object_or_404(Insert, id=question_id)
#         context = {"name": req.name, "phone": req.phone, "desc": req.description, "date": req.date}
#         return HttpResponse(f"Report ID: {question_id} \nName: {req.name} \nPhone: {req.phone} \nDescription: {req.description} \nDate: {req.date} \nDone: {req.done}")

class InsertNew(generic.View):
    model = Insert
    template_name = "serviceCRM/form.html"

    def insert(request):
        if request.method == 'POST':
            form = InputForm(request.POST)
            if form.is_valid():
                ticket=form.save()
                print("Raboti")
                return HttpResponseRedirect(f"/nalog/{ticket.id}/")
        else:
            form = InputForm()

        return render(request, InsertNew.template_name, {'form': form})

class Update(UpdateView):
    model = Insert
    template_name = "serviceCRM/edit.html"
    fields = ["name", "phone", "description", "done"]
    success_url = '/'

def done(request, id):
    req = get_object_or_404(Insert, id=id)
    if req.isDone():
        return HttpResponse("Done")
    return HttpResponse("Not Done")

def Nalog(request, id):
    data = Insert.objects.get(id=id)
    template = "serviceCRM/nalog.html"
    context = {"name": data.name, "phone": data.phone, "desc": data.description, "date": data.date}
    return render(request, template, context)
    
class Delete():
    model = Insert
    def Delete(request, id):
        req = get_object_or_404(Insert, id=id)
        req.delete()
        return HttpResponseRedirect("/")

class Done(SingleTableView):
    model = Insert
    table_data = Insert.objects.filter(done=True)
    table_class = DoneInsertTable
    template_name = 'serviceCRM/done.html'

