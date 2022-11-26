import os
import smtplib

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

with smtplib.SMTP('localhost', 1025) as smtp:
    subject = 'Dinner'
    body = 'Lets have dinner togather tonight'
    msg = f'Subject: {subject}\n\n{body}'
    smtp.sendemail(EMAIL_ADDRESS, 'bennetjoy03@gmail.com',msg)