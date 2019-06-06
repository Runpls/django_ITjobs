from django.urls import path

from . import views

urlpatterns = [
    path('', views.JobListView.as_view(), name='home'),
    path('jobs/<int:pk>-<str:slug>', views.job_detail, name='job_detail'),
]
