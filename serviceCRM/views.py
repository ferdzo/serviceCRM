from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render
from .models import Insert
from django.template import loader

def index(request):
    proba = Insert.objects.order_by("name")
    return HttpResponse(proba)

def detail(request,question_id):
    req = get_object_or_404(Insert,id=question_id)
    context = {"name":req.name, "phone":req.phone,"desc":req.description,"date":req.date}
    return HttpResponse(render(request,"serviceCRM/id.html", context))

