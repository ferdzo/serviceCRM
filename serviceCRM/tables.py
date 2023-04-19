import django_tables2 as tables
from .models import Insert


class InsertTable(tables.Table):
    class Meta:
        model = Insert
        template_name = "serviceCRM/list.html"
        attrs = {'class':'table table-sm'}
        fields = ['id', 'name', 'phone', 'description', 'date', 'done', 'edit']
        edit = tables.TemplateColumn(template_name='serviceCRM/edit.html')


