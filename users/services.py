import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import dotenv
import os


dotenv.load_dotenv()
from_mail = os.getenv('MY_MAIL')
my_pass = os.getenv('MY_PASS')

def send_mail(_to_mail, _subject ,_message):
    msg = MIMEMultipart()

    to_email = _to_mail
    message = _message

    msg.attach(MIMEText(message, 'plain'))
    msg['Subject'] = _subject

    server = smtplib.SMTP('smtp.mail.ru: 25')
    server.starttls()
    server.login(from_mail, my_pass)
    server.sendmail(from_mail, to_email, msg.as_string())
    server.quit()