from django import forms
from .models import Client


class AddClientForm(forms.ModelForm):
    """Add client form"""
    class Meta:
        model = Client
        fields = ("username", "first_name", "last_name", "birth_date",
                  "avatar")


class ListClientsForm(forms.Form):
    """Search and sort"""
    search_first_name = forms.CharField(required=False)
    search_last_name = forms.CharField(required=False)
    sort_field = forms.ChoiceField(choices=(("username", "username"),
                                            ("first_name", "first_name"),
                                            ("last_name", "last_name"),
                                            ("birth_date", "birth_date")),
                                   required=False)
