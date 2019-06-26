from django import forms
from .models import demotable

class demoform(forms.ModelForm):

    class Meta:
        model = demotable
        fields = '__all__'