from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Insert


class DateInput(forms.DateInput):
    input_type = 'date'


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
            'date': DateInput(),
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