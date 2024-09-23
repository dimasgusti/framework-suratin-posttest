from django.db import models
from .users import Users  

class Sender(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, limit_choices_to={'role': Users.SENDER})  # Relasi ke Users dengan role = Sender
    address = models.TextField() 

    def __str__(self):
        return self.user.username