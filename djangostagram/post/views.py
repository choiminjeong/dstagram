from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .forms import UploadForm
from .models import Post
from tag.models import Tag



# Create your views here.

class PostList(ListView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post_list'

class PostUpload(FormView):
    template_name = 'post_upload.html'
    form_class = UploadForm
    success_url = '/post/'

    # def form_valid(self, form):
    #     tags = form.data.get('tags').split(',')
    #     post = Post(
    #         imgurl=form.data.get('imgurl'),
    #         contents=form.data.get('contents')          
    #     )
    #     post.save()

    #     for tag in tags:
    #         if not tag:
    #             continue

    #         _tag, _ = Tag.objects.get_or_create(name=tag)
    #         post.tags.add(_tag)

    #     return super().form_valid(form)


    

class PostDetail(DetailView):
    template_name = 'Post_detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'

    

   