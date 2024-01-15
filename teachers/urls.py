from django.urls import path
from .views import list_teachers

urlpatterns = [
    path('list_teachers', list_teachers, name="list_teachers")
]