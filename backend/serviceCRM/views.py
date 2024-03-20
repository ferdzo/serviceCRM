from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .forms import InputForm
from .models import Insert
from .tables import DoneInsertTable, InsertTable

from django_tables2 import SingleTableView
from datatableview.views import DatatableView

class InsertListView(SingleTableView):
    model = Insert
    table_class = InsertTable
    template_name = 'serviceCRM/list.html'
  
class InsertNew(generic.View):
    model = Insert
    template_name = "serviceCRM/form.html"

    def insert(request):
        if request.method == 'POST':
            form = InputForm(request.POST)
            if form.is_valid():
                ticket = form.save()
                print("Raboti")
                return HttpResponseRedirect(f"/nalog/{ticket.id}/")
        else:
            form = InputForm()
ch
        return render(request, InsertNew.template_name, {'form': form})

class Update(generic.UpdateView):
    model = Insert
    template_name = "serviceCRM/edit.html"
    fields = ["name", "phone", "description","note", "done", "repair", "plateno"]
    success_url = '/'


def Nalog(request, id):
    try:
        data = Insert.objects.get(id=id)
    except:
        return HttpResponseRedirect("/")
    template = "serviceCRM/nalog.html"
    context = {"name": data.name, "phone": data.phone, "desc": data.description, "date": data.date}
    return render(request, template, context)
    
class Done(SingleTableView):
    model = Insert
    table_data = Insert.objects.filter(done=True)
    table_class = DoneInsertTable
    template_name = 'serviceCRM/done.html'
    
    def done_by_id(request, id):
        try:
            req = get_object_or_404(Insert, id=id)
        except:
            return HttpResponseRedirect("/done/")
        context = {"name": req.name, "phone": req.phone, "desc": req.description, "date": req.date}
        return HttpResponse(f"Report ID: {id} \nName: {req.name} \nPhone: {req.phone} \nDescription: {req.description} \n Note:{req.note} \nDate: {req.date} \nDone: {req.done} \nRepair: {req.repair} \n Plateno: {req.plateno} \n")

class Delete(generic.View):
    model = Insert

    def delete(request, id):
        req = get_object_or_404(Insert, id=id)
        req.delete()
        return HttpResponseRedirect("/")
    
class DatatableView(DatatableView):
    model = Insert
    template_name = 'serviceCRM/Insert_list.html'
    