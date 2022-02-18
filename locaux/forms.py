from django import forms
from django.forms import ModelForm

from locaux.models import local


# creation local form

class LocalForm(ModelForm):
    class Meta:
        model = local
        # fields = "__all__"
        fields = ('libelle', 'etat', 'type', 'nb_heure', 'nb_post', 'description')
        # labels = {
        #     'libelle': 'libelle',
        #     'etat': 'etat',
        #     'type': 'type',
        #     'nb_heure': 'nombre d\'heure d\'occupation/semaine',
        #     'nb_post': 'nombre de poste/local',
        #     'description': 'description',
        #
        # }
        # widgets = {
        #     'libelle': forms.TextInput(attrs={'class': 'form-control'}),
        #     'etat': forms.CheckboxSelectMultiple(),
        #     'type': forms.Select(choices=local.local_choices),
        #     'nb_heure': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'nb_post': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'description': forms.Textarea(attrs={'class': 'form-control'}),
        # }
