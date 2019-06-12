from django import forms
from userapp.models import User

class NewUserForm(forms.ModelForm):
    #you can add validation here
    class Meta():
        model = User
        fields = '__all__'
