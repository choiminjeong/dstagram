from django.shortcuts import render
# from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.http import Http404
from .forms import UploadForm
from dsuser.models import Dsuser
from .models import Post
from tag.models import Tag
from django.core.paginator import Paginator


class PostUpload(FormView):
    template_name = 'post_upload.html'
    form_class = UploadForm
    success_url = '/'

    def form_valid(self, form):
        user_id = self.request.session.get('user')
        dsuser = Dsuser.objects.get(userid=user_id)
        
        post = Post(
            imgurl=form.data.get('imgurl'),
            contents=form.data.get('contents'),
            writer=dsuser         
        )
        post.save()

        tags = form.data.get('tags').split(',')
        for tag in tags:
            if not tag:
                continue

            _tag, _ = Tag.objects.get_or_create(name=tag)
            post.tags.add(_tag)
            

        return super().form_valid(form)
    
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다')

    return render(request, 'post_detail.html', {'post': post})
   
def post_list(request):
    all_posts = Post.objects.all().order_by('-registered_dttm')
    page = request.GET.get('p', 1)
    paginator = Paginator(all_posts, 4)

    posts = paginator.get_page(page)
    userid = request.session.get('user')
    return render(request, 'timeline.html', {'posts': posts ,'userid': userid})

