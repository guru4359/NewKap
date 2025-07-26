from flask_mail import Message
from app import mail

def send_order_notification(recipient, subject, body):
    msg = Message(subject, recipients=[recipient], body=body)
    mail.send(msg)
