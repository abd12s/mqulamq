from django.shortcuts import render, redirect
from .models import Tool

def home(request):
    tools = Tool.objects.all()
    return render(request, 'tools/home.html', {'tools': tools})

def add_tool(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        code = request.POST['code']
        tool = Tool.objects.create(name=name, description=description, code=code, created_by=request.user)
        return redirect('tools:home')
    return render(request, 'tools/add_tool.html')