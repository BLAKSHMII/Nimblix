from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Designation
from .serializers import DesignationSerializer


# 🔹 1. Create API
@api_view(['POST'])
def create_designation(request):
    serializer = DesignationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


# 🔹 2. List API
@api_view(['GET'])
def list_designations(request):
    designations = Designation.objects.all()
    serializer = DesignationSerializer(designations, many=True)
    return Response(serializer.data)
