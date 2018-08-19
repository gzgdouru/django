from django import forms

from .models import UserProfile

from captcha.fields import CaptchaField


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={
        "invaild" : "验证码错误!"
    })


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class ForgetPwdForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={
        "invaild": "验证码错误!"
    })


class ModifyPwdForm(forms.Form):
    password = forms.CharField(required=True, min_length=6, max_length=20)
    password2 = forms.CharField(required=True, min_length=6, max_length=20)


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["image"]