from django.db import models


class SumpReading(models.Model):
    water_level = models.IntegerField()
    mud_level = models.IntegerField()
    leakage_current = models.IntegerField()
    motor_status = models.BooleanField()  # True = ON, False = OFF
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Water: {self.water_level} | Mud: {self.mud_level} | Leakage: {self.leakage_current}"
