from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.security import generate_password_hash

from os import path

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'HELLO'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    
    from .auth.auth import auth as authy
    from .views.views import main as mainy
    from .improvements.improvements import improvement as hee
    from .system.system import system as system

    app.register_blueprint(authy)
    app.register_blueprint(mainy)
    app.register_blueprint(hee)
    app.register_blueprint(system)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    
    from .models import User

    #admin_user = User(id=220, email='ad34@amazon.com', password=generate_password_hash('hello'),name = 'fads',type='admin')
    #with app.app_context():
     # db.session.add(admin_user)
      #db.session.commit()
      #print("added admin")


    #with app.app_context():
      # users = db.session.query(User).all()
    #for user in users:
    #    print(f'User ID: {user.id}, Username: {user.name}, Email: {user.email} type: {user.type}, Password: {user.password}')
    #    print(" Admin exist")
    #create_database(app)
    

    with app.app_context():
        db.create_all()

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

   
    return app

def create_database(app):
    if not path.exists(f"L&B/ + {DB_NAME}"):
         with app.app_context():
            db.create_all()
            print('Created Database!')