from django.db import models

class ProgramAudience(models.Model):
    signal = models.CharField(max_length=100)
    program_code = models.CharField(max_length=100)
    exhibition_date = models.DateField()
    program_start_time = models.TimeField()
    average_audience = models.FloatField()

    def __str__(self):
        return f"{self.program_code} on {self.signal} at {self.exhibition_date}"

class InventoryAvailability(models.Model):
    signal = models.CharField(max_length=100)
    program_code = models.CharField(max_length=100)
    date = models.DateField()
    available_time = models.IntegerField()

    def __str__(self):
        return f"{self.program_code} on {self.signal} at {self.date}"