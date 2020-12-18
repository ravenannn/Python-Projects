from django.db import models

# Create djangoClasses model and set parameters


class djangoClasses(models.Model):
    title = models.CharField(max_length=100, default="", blank=True, null=False)
    Course_Number = models.IntegerField(default=0, blank=True, null=False)
    Instructor_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    Duration = models.FloatField(default=0.00)
