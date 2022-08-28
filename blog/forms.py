from unicodedata import name
from django import forms
from .models import Comment, ImageUpload, Meeting


class Commentform(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "body")
        labels={'name':'ユーザー名', 'body':'コメント', }


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = "__all__"


class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ("name", "email", "contents")
        labels = {'name':'お名前', 'email':'Email', 'contents':'内容'}
        
