from django.db import models
 
class Message(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    msg_from = models.CharField(max_length=255)
    msg_to = models.CharField(max_length=255)
    text = models.TextField()

 
    # def __str__(self) -> str:
    #     return self.name

