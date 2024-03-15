from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from .forms import InputForm
from .tables import InsertTable
from .models import Insert
from django_tables2 import SingleTableView


# from django.template import loader

def index(request):
    proba = Insert.objects.order_by("date")
    return HttpResponse(proba)


# def detail(request,question_id):
#     req = get_object_or_404(Insert,id=question_id)
#     context = {"name":req.name, "phone":req.phone,"desc":req.description,"date":req.date}
#     return HttpResponse(render(request,"serviceCRM/id.html", context))
#
class ReportById(generic.DetailView):
    model = Insert
    template_name = "serviceCRM/python.exe -m pip install --upgrade pipid.html"

    def ReportById(request, question_id):
        req = get_object_or_404(Insert, id=question_id)
        context = {"name": req.name, "phone": req.phone, "desc": req.description, "date": req.date}
        return HttpResponse(f"Report ID: {question_id} \nName: {req.name} \nPhone: {req.phone} \nDescription: {req.description} \nDate: {req.date} \nDone: {req.done}")

class InsertNew(generic.View):
    model = Insert
    template_name = "serviceCRM/form.html"

    def insert(request):
        if request.method == 'POST':
            form = InputForm(request.POST)
            if form.is_valid():
                form.save()
                print("Raboti")
                return HttpResponseRedirect("/admin/")
        else:
            form = InputForm()

        return render(request, InsertNew.template_name, {'form': form})


class TableView(SingleTableView):
    model = Insert
    template_name = "serviceCRM/list.html"


def done(request, id):
    req = get_object_or_404(Insert, id=id)
    if req.isDone():
        return HttpResponse("Done")
    return HttpResponse("Not Done")
