from django.shortcuts import render
def posts(request):
  return render(request,'posts/posts_list.html')
# Create your views here.
