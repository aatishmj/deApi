from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from .serializers import emp_Serializer , emp_work_Serializer ,Ad_data_Serializer
# Create your views here.

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = emp.objects.all()
    serializer_class = emp_Serializer


class EmployeeworkViewSet(viewsets.ModelViewSet):
    queryset = emp_work.objects.all()
    serializer_class = emp_work_Serializer

class adminViewSet(viewsets.ModelViewSet):
    queryset = Ad_data.objects.all()
    serializer_class = Ad_data_Serializer