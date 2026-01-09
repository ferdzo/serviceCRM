import django_tables2 as tables
from django_tables2 import TemplateColumn
from django_filters import FilterSet
from django.db.models.query import QuerySet  # Add missing import
from .models import Insert

class InsertTable(tables.Table):
    
    actions = TemplateColumn(template_code='''
        <a class="text-indigo-600 hover:text-indigo-900 mr-2" href="{% url 'nalog' ticket_id=record.ticket_id %}">Види</a>
        <a class="text-gray-600 hover:text-gray-900 mr-2" href="{% url 'update' ticket_id=record.ticket_id %}">Уреди</a>
        {% if not record.done %}
        <a class="text-green-600 hover:text-green-900 font-medium" href="{% url 'close_ticket' ticket_id=record.ticket_id %}">Затвори</a>
        {% endif %}
    ''')
    
    class Meta:
        model = Insert
        fields = ("ticket_id","name","phone","description","date","status","done")
        per_page = 5


class DoneInsertTable(InsertTable):
    class Meta:
        model = Insert
        fields = ("ticket_id","name","phone","description","date", "date_close", "done")
        per_page = 5

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.data)
