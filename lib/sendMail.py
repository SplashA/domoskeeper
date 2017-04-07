# Module d'envoi de mails
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMail(destinataire)
    msg = MIMEMultipart()
    msg['Subject'] = 'domoskeeper info'
    message = 'Bonjour on vous cambriole lol'
    msg.attach(MIMEText(message))
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login('jtellier@pocketresult.com', 'PASSWORD')
    mailserver.sendmail('XXXXXX@gmail.com', 'XXXXXX@hotmail.fr',msg.as_string())
    mailserver.quit()