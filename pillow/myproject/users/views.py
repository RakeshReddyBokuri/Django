from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
def register(request):
  if request.method == "POST":
    form=UserCreationForm(request.POST)
    if form.is_valid():
      login(request,form.save())
      return redirect("posts:list")
  else:
    form=UserCreationForm()
  return render(request,'users/register_page.html',{'form':form})
# Create your views here.
def login_page(request):
  if request.method == "POST":
    form=AuthenticationForm(data=request.POST)
    if form.is_valid():
      login(request,form.get_user())
      if 'next' in request.POST:
        return redirect(request.POST.get('next'))
      return redirect("posts:list")
  else:
    form=AuthenticationForm()
  return render(request,'users/login_page.html',{'form':form})

def logout_page(request):
  if request.method == "POST":
    logout(request)
    return redirect("posts:list")