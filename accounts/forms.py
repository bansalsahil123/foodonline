from django import forms
from .models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ["first_name","last_name","username","phone_number","email","password"]
    

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data["password"]!= cleaned_data["confirm_password"]:
            raise forms.ValidationError("Password does not match")
