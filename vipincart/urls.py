
from django.contrib import admin
from django.urls import path,include
from home import views
from login import views 
from account import views
from modelfrom import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',include("home.urls")),
    path('login/', include('login.urls')),
    path('account/', include('account.urls')),
    path('student/', views.student_create, name='student_create'),
    path('students/', views.student_list, name='student_list'),
]


