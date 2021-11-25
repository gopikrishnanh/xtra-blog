from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from django.urls import reverse


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=400)
    img = models.ImageField(default='default.jpg', upload_to='pro_pic')

    def get_absolute_url(self):
        return reverse('hm')