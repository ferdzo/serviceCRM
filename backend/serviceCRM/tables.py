import django_tables2 as tables
from django_tables2 import TemplateColumn
from django_filters import FilterSet
from django.db.models.query import QuerySet  # Add missing import
from .models import Insert

class InsertTable(tables.Table):
    
    actions = TemplateColumn(template_code='<a class="btn btn-secondary" href="{% url \'update\' record.id %}">Edit</a> <a class="btn btn-secondary" href="{% url \'done\' record.id %}">Details</a>')
    
    class Meta:
        model = Insert
        fields = ("id","name","phone","description","date","done")
        per_page = 5


class DoneInsertTable(InsertTable):
    class Meta:
        model = Insert
        fields = ("id","name","phone","description","date","done")
        per_page = 5

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.data)
