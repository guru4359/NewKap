from flask_mail import Message
from app import mail

def send_order_notification(recipient, subject, body):
    """
    Send an email notification (e.g., order confirmation or admin alert).

    :param recipient: str - recipient email address
    :param subject: str - email subject line
    :param body: str - plain text email body
    """
    msg = Message(subject, recipients=[recipient], body=body)
    try:
        mail.send(msg)
        print(f"Email sent to {recipient} with subject '{subject}'")
    except Exception as e:
        # Log error or handle failure
        print(f"Failed to send email to {recipient}: {e}")
