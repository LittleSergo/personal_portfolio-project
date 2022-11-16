from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.all_projects, name='all_projects'),
    path('<int:project_id>/', views.proj_detail, name='proj_detail'),
]
