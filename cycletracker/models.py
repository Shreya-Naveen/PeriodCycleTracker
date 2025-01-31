from django.db import models

class MenstrualTracking(models.Model):
    cycle_length = models.IntegerField()
    last_period_start = models.DateField()
    submission_date = models.DateTimeField(auto_now_add=True)

class SymptomTracking(models.Model):
    tracking_date = models.DateField(auto_now_add=True)
    cramps = models.CharField(max_length=10, choices=[
        ('None', 'None'), ('Mild', 'Mild'), ('Moderate', 'Moderate'), ('Severe', 'Severe')
    ])
    mood = models.CharField(max_length=10, choices=[
        ('Happy', 'Happy'), ('Neutral', 'Neutral'), ('Irritable', 'Irritable'),
        ('Anxious', 'Anxious'), ('Sad', 'Sad')
    ])
    trained_today = models.BooleanField()
    performance_rating = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.tracking_date}: {self.cramps}, {self.mood}"
