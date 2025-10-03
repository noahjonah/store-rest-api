from django.shortcuts import render
from django.core.mail import send_mail, mail_admins, BadHeaderError


def say_hello(request):
    # Sending email
    # The send mail function will through an exception if an attacker, tries to modify email headers
    # .... and controls the from and to fields
    # Prevention => We use bad header error
    try:
        send_mail('subject', 'message', 'info@noahfake.com', ['someone@fake.com'])
        mail_admins('subjject', 'message', html_message='htm message')
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Mosh'})
