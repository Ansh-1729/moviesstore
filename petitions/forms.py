from django import forms
from .models import Petition

class PetitionForm(forms.ModelForm):
    class Meta:
        model = Petition
        fields = ["title", "description"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Movie request title"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 5, "placeholder": "Why should this be added?"}),
        }