from django import forms
from .models import Tag


class UploadForm(forms.Form):
    contents = forms.IntegerField(
        error_messages={
            'required': '내용을 입력해주세요.'
        },
        widget=forms.HiddenInput, label="내용")
    tags = forms.CharField(
        required=False, label="태그")

    def clean(self):
        cleaned_data = super().clean()
        contents = cleaned_data.get('contents')
        tags = cleaned_data.get('tags').split(',')
       
        
       