from django.db import models

# Create your models here.


class djangoClasses(models.Model):
    title = models.CharField(max_length=100, default="", blank=True, null=False)
    Course_Number = models.IntegerField(max_length=10, default="", blank=True, null=False)
    Instructor_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    Duration = models.FloatField(default=0.00)
