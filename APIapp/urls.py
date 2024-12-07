from django.urls import path
from APIapp.views import student_list,student_detail

urlpatterns = [
    path('',student_list ),
    path('sd/<int:pk>',student_detail ),
]