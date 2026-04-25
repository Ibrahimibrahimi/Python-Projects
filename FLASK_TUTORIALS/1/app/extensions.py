from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


# login manager
login_manager = LoginManager()


@login_manager.user_loader
# THIS IS IMPORTANT
def load_user(email):
    from .models import User
    return User.query.get(email)

# redirect to /login endpoint if not logged in
login_manager.login_view = "auth.login"

# db
db = SQLAlchemy()
