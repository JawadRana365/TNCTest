from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    confirmpassword = models.CharField(max_length=50)
    conditions = models.BooleanField(default=False)
    policies = models.BooleanField(default=False)

    def __str__(self):
        return self.name