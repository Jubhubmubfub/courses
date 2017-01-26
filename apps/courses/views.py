from django.shortcuts import render, redirect
from .models import Course, Description, Comment

# Create your views here.

def index(request):
    context = {
        'courses':Course.objects.all()
    }
    return render(request, 'courses/index.html',context)

def process(request):
    result = Course.objects.validate_inputs(request)
    Course.objects.create(course_name=request.POST['course_name'], description=request.POST['description'])
    return redirect('/')

def delete(request,id):
    context = {
        'courses':Course.objects.filter(id=id)
    }
    return render(request, 'courses/delete.html',context)

def remove(request,id):
    Course.objects.filter(id=id).delete()
    return redirect('/')
