from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup_view, name='signup'),
     path('login/', views.login_view, name='login'),
     path('dashboard/', views.dashboard, name='dashboard'),
     path('logout/', views.logout_view, name='logout'),
     path('dash/',views.dash,name='dash'),
     path('home/',views.home,name='home'),
     path('contact/',views.contact,name='contact')
]