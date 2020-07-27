from django import forms
from .models import Post
from tag.models import Tag


class UploadForm(forms.Form):
    imgurl = forms.CharField(
        error_messages={
            'required': '이미지 주소를 입력해주세요.'
        },
        max_length=128, label="이미지 주소")

    contents = forms.CharField(
        error_messages={
            'required': '내용을 입력해주세요.'
        },
        widget=forms.Textarea, label="내용")

    tags = forms.CharField(
        required=False, label="태그")
  
    def clean(self):
        cleaned_data = super().clean()
        imgurl = cleaned_data.get('imgurl')
        contents = cleaned_data.get('contents')
        tags = cleaned_data.get('tags')
       