from rest_framework import serializers
from .models import t_user , t_info

# Create your models here.
class t_user_Serializer(serializers.ModelSerializer) :
    class Meta:
        model = t_user
        fields = '__all__'
    
class t_info_Serializer(serializers.ModelSerializer) :
    class Meta:
        model = t_info
        fields = '__all__'

    def __str__(self):
        return self.name
