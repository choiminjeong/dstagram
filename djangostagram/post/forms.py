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
       
        
        # if imgurl and contents:
        #     post = Post(
        #         imgurl=imgurl,
        #         contents=contents
        #     )
        #     post.save()

            # for tag in tags:
            #     if not tag:
            #         continue

            #     _tag, _ = Tag.objects.get_or_create(name=tag)
            #     post.tags.add(_tag) 
        if not (imgurl and contents and tags):
            self.add_error('imgurl', '값이 없습니다')
            self.add_error('contents', '값이 없습니다')
        