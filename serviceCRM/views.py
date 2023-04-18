from django.http import HttpResponse
from .models import Insert
from django.template import loader

def index(request):
    proba = Insert.objects.order_by("name")
    return HttpResponse(proba)

def detail(request,question_id):
    proba = Insert.objects.get(id=question_id)
    template = loader.get_template("serviceCRM/id.html")
    context = {"name":proba.name, "phone":proba.phone,"desc":proba.description,"date":proba.date}
    return HttpResponse(template.render(context, request))

