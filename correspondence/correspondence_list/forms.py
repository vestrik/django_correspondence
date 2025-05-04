from django import forms
from . import models

class DateInput(forms.DateInput):
    input_type = 'date'

class CorrespondenceForm(forms.ModelForm):
    class Meta:
        model = models.Correspondence
        date = forms.DateField(widget=DateInput)
        fields = ['outcoming_mail_number', 'outcoming_mail_receiver', 'department', 'category',
                  'header', 'date', 'outcoming_file', 'incoming_file']
        