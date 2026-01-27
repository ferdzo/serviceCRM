from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Insert, Todo


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'


class InputForm(forms.ModelForm):
    class Meta:
        model = Insert
        fields = ["name", "phone", "date", "description", "note"]
        labels = {
            'name': "Име",
            'phone': "Телефон", 
            'date': "Датум на прием",
            'description': "Опис на проблем",
            'note': "Забелешка"
        }
        widgets = {
            'date': DateInput(format='%Y-%m-%d'),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class CloseForm(forms.ModelForm):
    class Meta:
        model = Insert
        fields = ["repair", "plateno"]
        labels = {
            'repair': "Детали за поправка",
            'plateno': "Наплатено"
        }
        widgets = {
            'repair': forms.Textarea(attrs={'rows': 4}),
            'plateno': forms.TextInput(attrs={'placeholder': 'пр. 1500 МКД'})
        }

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'name', 'phone', 'scheduled_date', 'scheduled_time']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Опис на задача...',
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Име на лице...'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '070-xxx-xxx'
            }),
            'scheduled_date': DateInput(format='%Y-%m-%d'),
            'scheduled_time': TimeInput(format='%H:%M', attrs={
                'class': 'form-control'
            })
        }
        labels = {
            'title': 'Задача',
            'name': 'Име',
            'phone': 'Телефон',
            'scheduled_date': 'Датум',
            'scheduled_time': 'Време'
        }

# class EditForm(forms.ModelForm):

#     class Meta:
#         model = Insert
#         fields = {"name", "phone", "description", "done"}
#         labels = {'name': "Name", 'phone': "Phone", 'description': "Description", 'done': "Done"}
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#             'phone': forms.TextInput(attrs={'class': 'form-control'}),
#             'description': forms.Textarea(attrs={'class': 'form-control'})
#         }

#     field_order = ["name", "phone", "description", "done"]