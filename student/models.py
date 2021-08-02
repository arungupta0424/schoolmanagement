from django.db import models

# Create your models here.
class studentuser(models.Model):
    name=models.CharField(max_length=50)
    father_name=models.CharField(max_length=50)
    mother_name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    mob_no=models.IntegerField()
    stclass=models.IntegerField()
    status=models.BooleanField()
