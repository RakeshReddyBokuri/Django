from django.contrib import admin
from django.urls import path,include
from . import views

app_name="users"
urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout_page,name='logout'),
]

