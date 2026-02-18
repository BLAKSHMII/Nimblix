from django.db import models

# Create your models here.
from django.db import models

class Designation(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    company_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
