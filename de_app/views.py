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

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import emp, emp_work
from .serializers import emp_Serializer, emp_work_Serializer

class EmployeeWorkAPIView(APIView):
    def get(self, request):
        # Query all employees
        employees = emp.objects.all()
        employee_work_dict = {}

        # Loop through employees and gather their work entries
        for employee in employees:
            # Query the work entries associated with this employee
            work_entries = emp_work.objects.filter(name=employee)

            # Serialize the work entries for this employee
            work_serializer = emp_work_Serializer(work_entries, many=True)

            # Add the employee's name as the key and the serialized work entries as the value
            employee_work_dict[employee.name] = work_serializer.data

        return Response(employee_work_dict)
