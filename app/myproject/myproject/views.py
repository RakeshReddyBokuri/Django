#from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  return render(request, 'home.html')
  #return HttpResponse("Hello World! I'mHome.")
def about(request):
  return render(request, 'about.html')
  #return HttpResponse("About Page Here.")