from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from datetime import datetime, timedelta
#from django.contrib.auth.models import User




def sendmail(subject,template,to,context):
    subject = 'Subject'
    template_str = 'app/'+ template+'.html'
    html_message = render_to_string(template_str, {'data': context})
    plain_message = striprender_to_string_tags(html_message)
    from_email = 'rahularya146@gmail.com'
    send_mail(subject, plain_message, from_email, [to], html_message=html_message)
