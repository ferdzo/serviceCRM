from django import forms
from .models import Insert

class DateInput(forms.DateInput):
    input_type = 'date'


class InputForm(forms.ModelForm):
    class Meta:
        model = Insert
        fields = {"name", "phone", "description", "date","done"}
        labels = {'name': "Name", 'phone':  "Phone", 'date': "Date", 'description': "Description",'done':"Done"}
        widgets = {
            'date': DateInput(),
            'description':forms.Textarea
        }
    field_order =["name", "phone", "date","description","done"]

        # name = forms.CharField(label="Name", max_length=30)
        # phone = forms.CharField(label="Phone", max_length=30)
        # date = forms.DateField()
        # description = forms.CharField(label="Write description of the problem...", max_length=300)
