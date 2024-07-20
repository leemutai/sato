from django.db import models


# Create your models here.
class Employee(models.Model):
    # name, email, dob, salary , disabled
    name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    dob = models.DateField(null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    disabled = models.BooleanField(default=False)
    profile = models.ImageField(upload_to='employees',null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True) #once during creation
    updated_at = models.DateTimeField(auto_now=True, null=True) #Every time an update happens

    def __str__(self):
        return self.name


# python manage.py makemigrations

# python manage.py migrate

#Pip install pillow
