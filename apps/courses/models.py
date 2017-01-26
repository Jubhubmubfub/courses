from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def validate_inputs(self,request):
        errors = []
        if len(request.POST['course_name'])<1:
            errors.append("Please enter a course name")
            return (False,errors)
        else:
            course_list = Course.objects.filter(course_name=request.POST['course_name'])
            if len(course_list)>0:
                errors.append("That course already exists")
            else:
                if len(request.POST['description'])<1:
                    errors.append("Please enter a description")
            if errors:
                return (False, errors)
            else:
                return (True, request)

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add = True)
    objects = CourseManager()

class Description(models.Model):
    description = models.TextField()
    course = models.ForeignKey(Course)
    created_at = models.DateTimeField(auto_now_add = True)

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    course = models.ForeignKey(Course)
    created_at = models.DateTimeField(auto_now_add = True)
