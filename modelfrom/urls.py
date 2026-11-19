from django.contrib import admin
from django.urls import path,include
from modelfrom import views

urlpatterns = [
      path('', views.student_create, name='student_create'),
      path('students/', views.student_list, name='student_list'),
   
]
