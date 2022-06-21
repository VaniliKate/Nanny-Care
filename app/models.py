from django.db import models

# Create your models here.


class Nanny(models.Model):
    profile_pic = models.ImageField(
        upload_to='profilepic/', default='default.jpeg')
    name = models.CharField(max_length=50, blank=True)
    experience = models.CharField(max_length=50, blank=True)
    rates = models.CharField(max_length=50, blank=True)
    availability =  models.CharField(max_length=50, blank=True)
    age =  models.CharField(max_length=50, blank=True)
    location =  models.CharField(max_length=50, blank=True)

    def save_profile(self):
        self.save()

    def __str__(self):
        return self.name


class Bio(models.Model):
    about = models.TextField()
    skills = models.TextField()
