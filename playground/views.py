from django.shortcuts import render
from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage
from templated_mail.mail import BaseEmailMessage # external template mail lib


def say_hello(request):
    # Sending email
    # The send mail function will through an exception if an attacker, tries to modify email headers
    # .... and controls the from and to fields
    # Prevention => We use bad header error
    try:
        #? send_mail('subject', 'message', 'info@noahfake.com', ['someone@fake.com'])
        #? mail_admins('subjject', 'message', html_message='htm message')
        # Attaching files to emails we have to use an email object from EmailMessageClass
        message = EmailMessage('subject', 'message', 'from@adminnoah.com', ['fake@user.com'])
        message.attach_file('playground/static/images/WineLaVielleFerme.png')
        # message.send()
        
        # Templated mail
        emailMessage = BaseEmailMessage(template_name='emails/hello.html', 
                                        context={"name": "Noah"})
        emailMessage.send(['templated@user.com'])
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Mosh'})
 