from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from dsuser.decorators import login_required
from .forms import UploadForm
from dsuser.models import Dsuser
from .models import Post
from tag.models import Tag



# Create your views here.


# class PostList(ListView):
#     model = Post
#     template_name = 'post.html'
#     context_object_name = 'post_list'

@method_decorator(login_required, name='dispatch')
class PostUpload(FormView):
    template_name = 'post_upload.html'
    form_class = UploadForm
    success_url = '/'

    def form_valid(self, form):
        user_id = self.request.session.get('user')
        dsuser = Dsuser.objects.get(pk=user_id)
        
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


    

# class PostDetail(DetailView):
#     template_name = 'Post_detail.html'
#     queryset = Post.objects.all()
#     context_object_name = 'post'

    
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다')

    return render(request, 'Post_detail.html', {'post': post})
   