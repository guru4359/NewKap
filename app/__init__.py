from flask import Flask

def create_app():
    app = Flask(__name__)
    # Load config, init extensions here if any

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from app.orders import orders as orders_blueprint
    app.register_blueprint(orders_blueprint, url_prefix='/orders')

    return app
