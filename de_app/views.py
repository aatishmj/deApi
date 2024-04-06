from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from .serializers import t_user_Serializer , t_info_Serializer 
from rest_framework import serializers

# Create your views here.

class T_UserViewSet(viewsets.ModelViewSet):
    queryset = t_user.objects.all()
    serializer_class = t_user_Serializer


class T_InfoViewSet(viewsets.ModelViewSet):
    queryset = t_info.objects.all()
    serializer_class = t_info_Serializer



from rest_framework.views import APIView
from rest_framework.response import Response
from .models import t_user, t_info
from .serializers import t_info_Serializer, t_user_Serializer

class EmployeeWorkAPIView(APIView):
    def get(self, request):
        # Query all employees
        employees = t_user.objects.all()
        employee_work_dict = {}

        # Loop through employees and gather their work entries
        for employee in employees:
            # Query the work entries associated with this employee
            work_entries = t_info.objects.filter(name=employee)

            # Serialize the work entries for this employee
            work_serializer = t_info_Serializer(work_entries, many=True)

            # Add the employee's name as the key and the serialized work entries as the value
            employee_work_dict[employee.name] = work_serializer.data

        return Response(employee_work_dict)


