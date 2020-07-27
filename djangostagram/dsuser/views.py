from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import RegisterForm, LoginForm
from django.core.paginator import Paginator
from post.models import Post



class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'

class LoginView(FormView):
    template_name = 'Login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        self.request.session['user'] = form.data.get('userid')
        return super().form_valid(form)

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')




def post_list(request):
    all_posts = Post.objects.all().order_by('-registered_dttm')
    page = request.GET.get('p', 1)
    paginator = Paginator(all_posts, 4)

    posts = paginator.get_page(page)
    userid = request.session.get('user')
    return render(request, 'timeline.html', {'posts': posts ,'userid': userid})

