from django.shortcuts import render, redirect

from coursesApp.forms import CourseForm
from coursesApp.models import Course


# Create your views here.
def getCourses(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request,"courseappTemplates/index.html",context)

def createCourse(request):
    form = CourseForm()
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,"courseappTemplates/add_course.html",{"form":form})

def deleteCourse(request,id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('/')

def updateCourse(request,id):
    course = Course.objects.get(id=id)
    form = CourseForm(instance=course)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,"courseappTemplates/add_course.html",{"form":form})





