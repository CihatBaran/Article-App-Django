from django import forms
from django.contrib.auth import get_user_model, authenticate, login


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, required=True, label="Username")
    password = forms.CharField(
        max_length=15, required=True, widget=forms.PasswordInput,
        label="Password")
    confirm = forms.CharField(
        max_length=15, required=True, widget=forms.PasswordInput, label="Confirm Password")

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Passwords are not same")

        User = get_user_model()
        users = User.objects.values()
        for user in users:
            if user["username"] == username:
                raise forms.ValidationError("Username exists!")

        values = {
            "username": username,
            "password": password,
            "confirm": confirm
        }
        return values


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", required=True)
    password = forms.CharField(
        label="Password", widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            raise forms.ValidationError("Check your credential please")

        values = {
            "username": username,
            "password": password
        }
        return values
