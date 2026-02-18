from django.urls import path
from .views import create_designation, list_designations

urlpatterns = [
    path('designations/create/', create_designation),
    path('designations/list/', list_designations),
]
