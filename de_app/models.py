from django.db import models

class t_user(models.Model):
    name = models.TextField(max_length=50)
    phone_no = models.IntegerField()
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=10)
    age = models.CharField(max_length=10)

    def __str__(self):
        return self.name 

class t_info(models.Model):
    name = models.ForeignKey(t_user, on_delete=models.CASCADE, related_name='work_entries')  # Added related_name
    income = models.CharField(max_length=100)
    income_goal = models.CharField(max_length=100)
    risk = models.CharField(max_length=100)
    submission_time = models.DateTimeField(auto_now_add=True)

