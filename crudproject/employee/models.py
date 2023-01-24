from django.db import models

# Create your models here.
class Employee(models.Model):
    eid=models.CharField(max_length=10)
    ename=models.CharField(max_length=30)
    email=models.EmailField()
    econtact=models.CharField(max_length=10)

    def __str__(self):
        return "%s" %(self.ename)
    class Meta:
        db_table="employee"