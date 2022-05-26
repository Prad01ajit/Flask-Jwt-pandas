from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY']='3ad98aac227663c9d34af919553d58e4'
    app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:pradeep@localhost/flask_1'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)

    from .auth import auth_blueprint
    from .aqi import aqi_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(aqi_blueprint)

    return app

