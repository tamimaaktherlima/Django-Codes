from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()
    fathers_name = models.TextField(default='Rahim')
    # fathers_name = models.TextField(null=True)
    mothers_name = models.TextField(default='Khatun')
    home_town = models.CharField(max_length=50,default='Barisal')

    # object wise show na kore name show korbe
    def __str__(self):
        return f"Roll : {self.roll} , Name : {self.name}"