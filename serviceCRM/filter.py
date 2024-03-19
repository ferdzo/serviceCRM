from .models import Insert
import django_filters as filters
from django_filters import FilterSet

class DoneTable(FilterSet):
    class Meta:
        model = Insert
        fields = ["done"]

    def filter_done(self, queryset, name, value):
        if value:
            return queryset.filter(done=True)
        else:
            return queryset.filter(done=False)