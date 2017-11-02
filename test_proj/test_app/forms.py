from django import forms
from test_app.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    """Sign up"""
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2',
                  'birth_date', 'avatar')


class UserListForm(forms.Form):
    """Search and sort"""
    search = forms.CharField(required=False)
    search2 = forms.CharField(required=False)
    sort_field = forms.ChoiceField(choices=(('username', 'username'), ('first_name', 'first_name'),
                                            ('last_name', 'last_name'), ('birth_date', 'birth_date')),
                                   required=False)
