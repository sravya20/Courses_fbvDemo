from django import forms

from coursesApp.models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
