from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.http import Http404
from .models import Post
from .forms import EmailPostForm

# Create your views here.
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog_app/post/list.html'


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, publish__year = year, publish__month = month, publish__day = day, status = Post.Status.PUBLISHED)
    return render(
        request, 'blog_app/post/detail.html', {'post':post}
    )
    
def post_share(request, post_id):
    post = get_object_or_404(Post, id = post_id, status = Post.Status.PUBLISHED)
    
    if request.method == 'POST':
        form = EmailPostForm(request.POST) #form is submiited
        if form.is_valid():
            cd = form.cleaned_data 
    else:
        form = EmailPostForm()
        return render(request, 'blog/post/share.html', {'post': post, 'form': form})