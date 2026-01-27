import django_tables2 as tables
from django_tables2 import TemplateColumn
from django_filters import FilterSet
from django.db.models.query import QuerySet  # Add missing import
from .models import Insert

class InsertTable(tables.Table):
    
    actions = TemplateColumn(template_code='''
        <div class="flex flex-wrap gap-1 sm:gap-2">
            <a class="text-indigo-600 hover:text-indigo-900 text-sm" href="{% url 'nalog' ticket_id=record.ticket_id %}">Види</a>
            <a class="text-gray-600 hover:text-gray-900 text-sm" href="{% url 'update' ticket_id=record.ticket_id %}">Уреди</a>
            {% if not record.done %}
            <a class="text-green-600 hover:text-green-900 font-medium text-sm" href="{% url 'close_ticket' ticket_id=record.ticket_id %}">Затвори</a>
            {% endif %}
        </div>
    ''', orderable=False)
    
    phone = TemplateColumn(template_code='''
        <a href="tel:{{ record.phone }}" class="text-blue-600 hover:text-blue-800 inline-flex items-center">
            <svg class="w-4 h-4 mr-1 sm:hidden" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
            </svg>
            <span class="hidden sm:inline">{{ record.phone }}</span>
            <span class="sm:hidden">Повикај</span>
        </a>
    ''', orderable=False)
    
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
