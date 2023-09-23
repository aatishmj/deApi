from django.db import models

class emp(models.Model):
    name = models.TextField(max_length=50)
    phone_no = models.IntegerField()
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name 

class emp_work(models.Model):
    name = models.ForeignKey(emp, on_delete=models.CASCADE, related_name='work_entries')  # Added related_name
    component_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    submission_time = models.DateTimeField(auto_now_add=True)

class Ad_data(models.Model):
    drawing = models.ImageField(upload_to='drawings/')
    name = models.CharField(max_length=100)
