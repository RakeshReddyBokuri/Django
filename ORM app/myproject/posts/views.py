from django.shortcuts import render
from .models import Post
def post(request):
  posts=Post.objects.all().order_by('-date')
  return render(request,"post/post_list.html",{'posts':posts})
def post_page(request,slug):
  post=Post.objects.get(slug=slug)
  return render(request,"post/post_page.html",{'post':post})
# Create your views here.
