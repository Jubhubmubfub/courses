from django.shortcuts import render, redirect
from .models import Course, Description, Comment
from django.contrib import messages


# Create your views here.

def index(request):
    context = {
        'courses':Course.objects.all(),
        'descriptions':Description.objects.all()
    }
    return render(request, 'courses/index.html',context)

def process(request):
    result = Course.objects.validate_inputs(request)
    print "RESULT IS =======>",result
    if result[0]==False:
        for error in result[1]:
            messages.add_message(request, messages.INFO, error)
        return redirect('/')
    else:
        newCourse = Course.objects.create(course_name=request.POST['course_name'])
        newDescription = Description.objects.create(description=request.POST['description'], course=newCourse)
        return redirect('/')

def delete(request,id):
    context = {
        'courses':Course.objects.filter(id=id)
    }
    return render(request, 'courses/delete.html',context)

def remove(request,id):
    Course.objects.filter(id=id).delete()
    return redirect('/')
