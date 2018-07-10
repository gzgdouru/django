from django import forms
from django.contrib.admin import widgets
from .models import Diary, UserInfo

class LoginForm(forms.Form):
    username = forms.CharField(label="姓名", max_length=32)
    passwd = forms.CharField(label="密码", widget=forms.PasswordInput())

class DateInput(forms.DateInput):
    input_type = "date"

class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ["budget", "weight", "note", "ddate"]
        widgets = {
            "ddate" : DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super(DiaryForm, self).__init__(*args, **kwargs)
        self.fields["budget"].label = "今日花费(元)"
        self.fields["weight"].label = "今日体重(kg)"
        self.fields["note"].label = "心情留言"
        self.fields["ddate"].label = "日期"

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ["height", "male", "website"]

    def __init__(self, *args, **kwargs):
        super(UserInfoForm, self).__init__(*args, **kwargs)
        self.fields["height"].label = "身高(cm)"
        self.fields["male"].label = "是男生吗"
        self.fields["website"].label = "个人网站"