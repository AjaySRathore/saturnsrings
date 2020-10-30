from django import forms
from ringer.models import Ringer

class RingerLoginForm(forms.Form):
    """Generates a login form with two fields.

       Attributes:
       username -- form field for username.
       password -- form field for password with forms.PasswordInput() widget.
    """
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())
