from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] =  'postgresql://postgres:Saad1234@localhost/dbapp'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    
    db.init_app(app)

    from routes import reg_routes

    reg_routes(app, db)

    migrate = Migrate(app,db)

    return app