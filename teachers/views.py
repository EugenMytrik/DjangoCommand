from django.shortcuts import render
from .models import Teacher


def list_teachers(request):
    teachers = Teacher.objects.all()
    return render(request, "list_teachers.html", {"teachers":teachers})
