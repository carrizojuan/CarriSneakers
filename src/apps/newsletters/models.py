from django.db import models

# Create your models here.

class UserNewsLetter(models.Model):
    email = models.EmailField(primary_key=True),
    date_added = models.DateTimeField(auto_now_add=True),

    def __str__(self):
        return self.email

class NewsLetters(models.Model):
    name = models.CharField(max_length=255),
    subject = models.CharField(max_length=255),
    body = models.TextField(blank=True, null=True),
    email = models.ManyToManyField(UserNewsLetter),
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    