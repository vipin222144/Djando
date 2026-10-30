from django import forms
from .models import vipin

class StudentForm(forms.ModelForm):

    class Meta:
        model = vipin
        fields = '__all__'