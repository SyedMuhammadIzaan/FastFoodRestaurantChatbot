from flask import Flask
from app.models import db
from config import CONFIG_BY_NAME


def create_app(config_name: str = 'development'):
    app = Flask(__name__)
    app.config.from_object(CONFIG_BY_NAME[config_name])

    db.init_app(app)
    
    from app.main.routes import main_bp
    from app.webhook import webhook_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(webhook_bp)
    # app.register_blueprint(api_bp, url_prefix="/api")

    with app.app_context():
        db.create_all()

    return app
