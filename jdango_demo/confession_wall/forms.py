from django import forms
from .models import Profile, Post

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["nickname", "male", "age"]

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields["nickname"].label = "昵称"
        self.fields["male"].label = "性别(男)"
        self.fields["age"].label = "年龄"

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["context"]

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields["context"].label = "您想说的话"