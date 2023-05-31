from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    tecnology = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    

