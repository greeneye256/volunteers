from django import forms
from .models import Volunteer


class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = '__all__'
        labels = {
            'first_name': 'Nume',
            'last_name': 'Prenume',
            'email': 'Email',
            'phone': 'Numar de telefon',
            'date_of_birth': 'Data nasterii (yyyy-mm-dd)',
            'address': 'Adresa',
            'branch': 'Filiala'
        }

    def __init__(self, *args, **kwargs):
        super(VolunteerForm, self).__init__(*args, **kwargs)
        self.fields['branch'].empty_label = "Selecteaza filiala"
        self.fields['email'].required = False
        self.fields['phone'].required = False
