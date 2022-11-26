import smtplib,email,email.encoders,email.mime.text,email.mime.base

smtpserver = 'email@site.com'
to = ['address@gmail.com']
fromAddr = 'email@site.com's
subject = "testing email attachments"

# create html email
html = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" '
html +='"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml">'
html +='<body style="font-size:12px;font-family:Verdana"><p>...</p>'
html += "</body></html>"
emailMsg = email.MIMEMultipart.MIMEMultipart('text/csv')
emailMsg['Subject'] = subject
emailMsg['From'] = fromAddr
emailMsg['To'] = ', '.join(to)
emailMsg['Cc'] = ", ".join(cc)
emailMsg.attach(email.mime.text.MIMEText(html,'html'))

# now attach the file
fileMsg = email.mime.base.MIMEBase('text/csv')
fileMsg.set_payload(file('rsvps.csv').read())
email.encoders.encode_base64(fileMsg)
fileMsg.add_header('Content-Disposition','attachment;filename=rsvps.csv')
emailMsg.attach(fileMsg)

# send email
server = smtplib.SMTP(smtpserver)
server.sendmail(fromAddr,to,emailMsg.as_string())
server.quit()