from rest_framework import serializers
from .models import emp_work , emp , Ad_data

# Create your models here.
class emp_Serializer(serializers.ModelSerializer) :
    class Meta:
        model = emp
        fields = '__all__'
    
class emp_work_Serializer(serializers.ModelSerializer) :
    class Meta:
        model = emp_work
        fields = '__all__'

    def __str__(self):
        return self.name

class Ad_data_Serializer(serializers.ModelSerializer) :
    class Meta:
        model = Ad_data
        fields = '__all__'