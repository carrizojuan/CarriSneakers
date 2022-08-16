from django.db import models

# Create your models here.

class NewsletterUser(models.Model):
    correo = models.EmailField(primary_key=True),
    date_added = models.DateTimeField(auto_now_add=True),

    def __str__(self):
        return self.correo

class Newsletter(models.Model):
    name = models.CharField(max_length=255),
    subject = models.CharField(max_length=255),
    body = models.TextField(blank=True, null=True),
    email = models.ManyToManyField(NewsletterUser),
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    