from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="姓名", max_length=32)
    passwd = forms.CharField(label="密码", widget=forms.PasswordInput())
