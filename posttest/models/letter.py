from django.db import models
from .sender import Sender
from .recipient import Recipient

class Letter(models.Model):
    letter_number = models.CharField(max_length=50, unique=True)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    issue_date = models.DateField(auto_now_add=True)
    
    sender = models.ForeignKey(Sender, on_delete=models.CASCADE)  
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE) 

    def __str__(self):
        return f"Letter #{self.letter_number} - {self.subject}"