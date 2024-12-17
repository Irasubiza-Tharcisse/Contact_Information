from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    contact_type = models.CharField(max_length=20, choices=[('personal', 'Personal'), ('work', 'work'),('friends','friends')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return f'{self.name}'