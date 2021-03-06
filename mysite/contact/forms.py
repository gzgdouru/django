#coding:utf-8
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label="Your e-mail address")
    message = forms.CharField(widget=forms.Textarea)

    # Django的form系统自动寻找匹配的函数方法，该方法名称以clean_开头，并以字段名称结束.如果有这样的方法，它将在校验时被调用
    def clean_message(self):
        message = self.cleaned_data["message"]
        num_words = len(message.split())
        if num_words < 4: raise forms.ValidationError("Not enough words!")
        return message