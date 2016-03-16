from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=200)
    mass = models.FloatField()
    calories = models.PositiveIntegerField()
    saturated_fat = models.FloatField()
    sugar = models.FloatField()
    protein = models.FloatField()
    is_exempt = models.BooleanField()

    def __str__(self):
        return self.name
