from django.shortcuts import render, get_object_or_404
from .models import Project

def home(request):
    projects = Project.objects.order_by('-date')
    return render(request, 'portfolio/home.html', {'projects': projects})

def test(request):
    return render(request, 'portfolio/test.html')

def all_projects(request):
    projects = Project.objects.order_by('-date')
    return render(request, "portfolio/all_projects.html", {'projects': projects})

def proj_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'portfolio/project_detail.html', {'project': project})
