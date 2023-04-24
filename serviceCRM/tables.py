import django_tables2 as tables
from .models import Insert


class InsertTable(tables.Table):
    class Meta:
        model = Insert
        template_name = "serviceCRM/list.html"
        edit = tables.TemplateColumn(template_name="serviceCRM/edit.html", verbose_name="edit", orderable=False)

