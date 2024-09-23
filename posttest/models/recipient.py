from django.db import models
from .users import Users  

class Recipient(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, limit_choices_to={'role': Users.RECIPIENT})  # Relasi ke Users dengan role = Recipient
    address = models.TextField() 

    def __str__(self):
        return self.user.username