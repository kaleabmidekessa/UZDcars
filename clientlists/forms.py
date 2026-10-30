from django import forms
from .models import Clients_List

class ClientLeadForm(forms.ModelForm):
    class Meta:
        model = Clients_List
        fields = ['name','phone_number', 'desired_car', 'max_budget', 'notes', 'is_active']
