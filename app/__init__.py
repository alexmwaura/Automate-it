from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_user import SQLAlchemyAdapter
from flask_login import LoginManager

db = SQLAlchemy() 

login_manager = LoginManager()

def create_app(config_name):
    
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   
    app.config.from_object(config_options[config_name])
    from .models import User
    # db_adapter = SQLAlchemyAdapter(db, User)
    # user_manager = UserManager(db_adapter)
    login_manager.init_app(app)


    db.init_app(app)

    # user_manager.init_app(app)
    
    from .main import main as main_blueprint
    

    app.register_blueprint(main_blueprint)
    # with app.app_context():
    #     from .main import views
    #     db.create_all()
    @login_manager.user_loader
    def user_loader(user_id):
        """Given *user_id*, return the associated User object.

        :param unicode user_id: user_id (email) user to retrieve

        """
        return User.query.get(user_id)

    return app

