import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'devkey'
    STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY') or 'your_stripe_public_key'
    STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY') or 'your_stripe_secret_key'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'example@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'yourpassword'

