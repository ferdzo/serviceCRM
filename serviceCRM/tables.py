import django_tables2 as tables
from .models import Insert

class InsertTable(tables.Table):
    class Meta:
        model = Insert
        template_name="base.html"