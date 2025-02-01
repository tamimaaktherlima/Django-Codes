from django.db import models

# Create your models here.
class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    fathers_name = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return f"Roll : {self.roll} - {self.name}"

