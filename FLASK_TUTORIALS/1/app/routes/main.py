from flask import Blueprint
from flask import render_template , redirect , url_for
from flask_login import login_required , current_user , login_user
from ..models import User
from ..extensions import db
from werkzeug.security import generate_password_hash
# root route
main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    # check if already logged
    return "MAIN PAGE"



def fetchusers():
    import requests
    return requests.get("http://127.0.0.1:8080/gea").json()

@main_bp.route("/gea")
def getallusers():
    return [{"username":user.username , "email":user.email , "created_at":user.created_at , "bio":user.bio} for user in User.query.all()]

@main_bp.route("/users")
def allusers():
    users = fetchusers()
    return render_template("users.html",users=users,l=len(users))


@main_bp.route("/profile")
@login_required
def profile():
    return render_template("profile.html",user=current_user)

@main_bp.route("/admin")
@login_required
def admin():
    # check if there is an admin user , else create it
    admin = User.query.filter_by(email="admin@gmail.com")
    if admin is None :
        admin_user = User(email="admin@gmail.com",
                        username="admin",
                        password=generate_password_hash("admin"),
                        role="admin"
        )
        db.session.add(admin_user)
        db.session.commit()
    # check if user's role is admin
    if current_user.role == "admin":
        return render_template("admin.html")
    else :
        return redirect(url_for("auth.login", e_error = "Please log as admin to access to admin panel"))

### Hidden admin panel & users delete ...
@main_bp.route("/hidden-admin-panel")
def hiddenadminpanel():
    # return list of all users and add buttons to delete each user
    users = User.query.all()
    
    return render_template("admin.html",users=users)
@main_bp.route("/create-50-users")
def createUsers():
    users = [
        User(email=f"user{i}@gmail.com",
            username = f"User n°{i}",
            password = "0000",
            bio = f"Hi im user N°{i}",
            role = "user"
            )
        for i in range(50)
        ]
    for user in users :
        db.session.add(user)
    db.session.commit()
    return "Created successfully"

@main_bp.route("/users/delete/<email>")
def deleteUser(email=None):
    user = User.query.filter_by(email=email)
    if email is None  or user  is None:
        return "User Not found"
    
    user_to_delete = User.query.filter_by(email=email).one()
    db.session.delete(user_to_delete)
    db.session.commit()
    return f"user deleted ? ==> {'yes' if User.query.filter_by(email=email).first() is None else 'no'}"

@main_bp.route("/url/<something>")
def url(something):
    import requests
    try :
        r = requests.get(something.replace('[2]','//').replace("[1]","/"))
        return f"STATUS_CODE : {r.status_code}"
    except :
        return "ERROR"
