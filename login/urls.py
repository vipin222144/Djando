from django.urls import path
from . import views 

urlpatterns = [
    path('data', views.login_list, ),
     path("", views.student_form, name="student_form"),
]