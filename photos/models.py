from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Photo(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  image = models.ImageField(upload_to='photos/')
  title = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return f'Photo: {self.title}'