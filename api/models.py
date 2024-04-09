# myapp/models.py
from django.db import models

class TestData(models.Model):
    url = models.CharField(max_length=10, unique=True)
    json_data = models.JSONField()
