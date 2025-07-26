from flask import Flask
from config import Config
from flask_mail import Mail

mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mail.init_app(app)

    from app.main.routes import main
    from app.orders.routes import orders

    app.register_blueprint(main)
    app.register_blueprint(orders, url_prefix='/orders')

    return app
