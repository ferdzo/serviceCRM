from .models import Insert
import django_filters as filters
from django_filters import FilterSet
from django.db.models import Q
from django import forms

class InsertFilter(FilterSet):
    start_date = filters.DateFilter(field_name="date", lookup_expr='gte', label='Од датум', widget=forms.TextInput(attrs={'type': 'date'}))
    end_date = filters.DateFilter(field_name="date", lookup_expr='lte', label='До датум', widget=forms.TextInput(attrs={'type': 'date'}))
    search = filters.CharFilter(method='filter_search', label='Пребарај (Име, Тел, ID, Опис)')

    class Meta:
        model = Insert
        fields = ['search', 'done']

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) |
            Q(phone__icontains=value) |
            Q(description__icontains=value) |
            Q(plateno__icontains=value) |
            Q(ticket_id__icontains=value) |
            Q(id__icontains=value)
        )

class DoneTable(FilterSet):
    class Meta:
        model = Insert
        fields = ["done"]

    def filter_done(self, queryset, name, value):
        if value:
            return queryset.filter(done=True)
        else:
            return queryset.filter(done=False)
class DoneFilter(FilterSet):
    start_date = filters.DateFilter(field_name="date_close", lookup_expr='gte', label='Од датум (Затворено)', widget=forms.TextInput(attrs={'type': 'date'}))
    end_date = filters.DateFilter(field_name="date_close", lookup_expr='lte', label='До датум (Затворено)', widget=forms.TextInput(attrs={'type': 'date'}))
    search = filters.CharFilter(method='filter_search', label='Пребарај (Име, Тел, ID)')

    class Meta:
        model = Insert
        fields = ['status']

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) |
            Q(phone__icontains=value) |
            Q(description__icontains=value) |
            Q(plateno__icontains=value) |
            Q(ticket_id__icontains=value) |
            Q(id__icontains=value)
        )
