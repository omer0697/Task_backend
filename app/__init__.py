from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from app.models import user, post, album, todo, comment, photo  # Import models to register them
        db.create_all()  # Create database tables for our models

        from app.routes import main_bp  # Import blueprint
        app.register_blueprint(main_bp, url_prefix='/api')

    return app
