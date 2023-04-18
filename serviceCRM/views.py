from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Insert
from django.views import generic
from .forms import InputForm

from django.template import loader


def index(request):
    proba = Insert.objects.order_by("name")
    return HttpResponse(proba)


# def detail(request,question_id):
#     req = get_object_or_404(Insert,id=question_id)
#     context = {"name":req.name, "phone":req.phone,"desc":req.description,"date":req.date}
#     return HttpResponse(render(request,"serviceCRM/id.html", context))
#

def inputform(request):
    if request.method == 'POST':
        if request.POST.get():
            return


class ReportById(generic.DetailView):
    model = Insert
    template_name = "serviceCRM/id.html"

    def ReportById(request, question_id):
        req = get_object_or_404(Insert, id=question_id)
        context = {"name": req.name, "phone": req.phone, "desc": req.description, "date": req.date}
        return HttpResponse(render(request, ReportById.template_name, context))


class InsertNew(generic.View):
    model = Insert
    template_name = "serviceCRM/form.html"
    def insert(request):
        if request.method == 'POST':
            form=InputForm(request.POST)
            if form.is_valid():
                form.save()
                print("Raboti")
                return HttpResponseRedirect("/admin/")
        else:
            form = InputForm()

        return render(request,InsertNew.template_name,{'form':form})

def done(request,question_id):
    req = get_object_or_404(Insert, id=question_id)
    if req.isDone():
        return HttpResponse("Done")
    return HttpResponse("Not Done")

