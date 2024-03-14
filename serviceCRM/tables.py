import django_tables2 as tables
from .models import Insert
from django_tables2.utils import A


class InsertTable(tables.Table):
    class Meta:
        model = Insert
        template_name = "list.html"
        sequence = ("name", "phone", "description","date","done" )
        delete = tables.LinkColumn('main:delete_item', args=[A('pk')], attrs={
            'a': {'class': 'btn'}
        })
