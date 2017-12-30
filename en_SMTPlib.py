import smtplib
from email.message import EmailMessage
from customConstants import *

def smtp_send(message):
    '''Send SMTP Message using an SMTP Relay.
       use a dict to identify:
          dict['subject']
          dict['from']
          dict['to']
          dict['body']
    '''
    print("Sending email to {}".format(message['from']))
    s = smtplib.SMTP(smtp_relay)
    msg = EmailMessage()
    msg.set_content(message['body'])
    msg["Subject"] = message['subject']
    msg["From"] = message['from']
    msg["To"] = message['to']
    s.send_message(msg)
    s.quit()
