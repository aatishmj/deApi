from django.db import models


# Create your models here.
class emp(models.Model) :
    id=models.CharField(max_length=10,primary_key=True)
    name=models.TextField(max_length=50)
    phone_no=models.IntegerField()
    email=models.EmailField(blank=True)
    def __str__(self):
        return self.name
    
class emp_work(models.Model) :
    name=models.TextField(max_length=50)
    component_name=models.CharField(max_length=100)
    quantity=models.IntegerField()

class Ad_data(models.Model) :
    drawing=models.ImageField()
    name=models.CharField(max_length=100)
