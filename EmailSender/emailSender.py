from email.message import EmailMessage
from password import mail_password
from listOfReceiver import customer
import ssl
import smtplib

def sender():
    email_sender = "fordpipatkitkul@gmail.com";
    return email_sender
def sender_password():
    email_password = mail_password;
    return email_password


subject = "scam mail don't read it";
body = " sadsda ";


email = EmailMessage();
email['To'] = customer()
email['From'] = sender()
email['subject'] = subject
email.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL( 'smtp.gmail.com' , 465, context=context) as smtp:
    smtp.login(sender(), sender_password())
    smtp.sendmail(sender(), customer(), email.as_string())
