from django.db import models

class TestData(models.Model):
    json_data = models.JSONField()
    url = models.CharField(max_length=10, unique=True)  # Adjust the length of the URL as needed

