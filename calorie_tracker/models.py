from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Food(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    calories = models.FloatField()
    total_calories = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    calories_reset=models.BooleanField(default=False)
    
    def calculate_total_calories(self):
        self.total_calories = self.calories + self.calories
        self.save()
        

    def reset_calories(self):
        self.calories_reset = True
        self.total_calories = 0
        self.save()

    def __str__(self):
        return self.Name



