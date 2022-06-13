import importlib

from django.shortcuts import render, redirect, HttpResponse
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings


def home(request):

    EmailTestForm = importlib.import_module(f"{__name__.split('.')[0]}").forms.EmailTestForm
    if request.method == 'POST':
        form = EmailTestForm(request.POST)
        if form.is_valid():
            subject = 'Email system test'
            body = 'The Email System is properly working !'
            try:
                send_mail(subject, body, settings.EMAIL_HOST_USER, [form.cleaned_data['email'],])
                print(f'Sent a mail to {form.cleaned_data["email"]}')
            except BadHeaderError:
                return HttpResponse('Invalid header. Could not send the email.')
            return render(request, 'core/home.html', context={'email_sent': True})

    form = EmailTestForm()
    return render(request, 'core/home.html', context={'form': form})