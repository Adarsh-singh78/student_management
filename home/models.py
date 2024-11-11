from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class student(models.Model):
    name=models.CharField(max_length=50,blank=False,null=False)
    email=models.EmailField(max_length=254,default="not-provided@gmail.com")
    mobile_no=models.CharField(max_length=10,unique=True,validators=[RegexValidator(regex='^[6-9]\d{9}$',message="enter valid mobile number")],blank=False,null=False)

    def __str__(self) -> str:
        return self.name


# problem   ->1. empty strings are accepted -> blank =False
#           ->   throwing error with non unique values 
#           ->   on shell it bypasses the validation here it is performing
#           ->  it is accpeting the empty valus for all