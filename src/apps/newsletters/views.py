from pyexpat.errors import messages
from django.shortcuts import render
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, send_mail

""" from .models import Newsletter
from .forms import NewsletterSuscribeForm """

# Create your views here.

""" def newsletter_suscribe(request):
    form = NewsletterSuscribeForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if Newsletter.objects.filter(email = instance.correo).exists():
            messages.warning(request, "El correo ya existe")
        else:
            instance.save()
            messages.success(request, "Se ha suscrito exitosamente")
            subject = "Bienvenido"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.correo]
            html_template = "newsletters/welcome.html"
            html_message=render_to_string(html_template)
            message = EmailMessage(subject, html_message, from_email, to_email)
            message.content_subtype = "html"
            message.send()
    
    ctx = {
        "form": form
    }
    return render(request, "newsletters/suscribe.html", ctx) """