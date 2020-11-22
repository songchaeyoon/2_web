from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.

def post_content(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    paginator = Paginator(posts, 1)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/post_content.html', {'posts': posts})