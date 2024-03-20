from django import forms
from .models import Insert


class DateInput(forms.DateInput):
    input_type = 'date'


class InputForm(forms.ModelForm):
    class Meta:
        model = Insert
        fields = {"name", "phone", "description", "date", "note"}
        labels = {'name': "Name", 'phone': "Phone", 'date': "Date", 'description': "Description", 'note': "Note"}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'date': DateInput(),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'note': forms.TextInput(attrs={'class': 'form-control'})
        }

    field_order = ["name", "phone", "date", "description", "done"]

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