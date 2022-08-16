from django import forms
from .models import NewsletterUser, Newsletter

class NewsletterSuscribeForm(forms.ModelForm):

    class meta:
        model = NewsletterUser
        field = ['correo']

class NewsletterCreationForm(forms.ModelForm):

    class meta:
        model = Newsletter
        field = ['name', 'subject', 'body', 'email']
    
