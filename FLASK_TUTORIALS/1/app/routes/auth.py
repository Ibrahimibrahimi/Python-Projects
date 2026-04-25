from flask import Blueprint , flash
from flask import render_template , request , redirect
from ..models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user , current_user , login_required , logout_user
from ..extensions import db

# root route
auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login",methods=["POST","GET"])
def login():
    if current_user.is_authenticated :
        return redirect("/profile")
    # check if already logged
    if request.method == "POST" :
        email = request.form.get("email")
        password = request.form.get("password")
        # verify
        user = User.query.filter_by(email=email).first()
        if user :
            # compare password
            if check_password_hash(user.password, password) :
                login_user(user)
                return render_template("profile.html")
            else :
                return render_template("login.html",p_error="Wrong password")
        else :
            return render_template("login.html",e_error="Email not found")
    return render_template("login.html")

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")

@auth_bp.route("/register",methods=["POST","GET"])
def register():
    if current_user.is_authenticated :
        return redirect("/profile")
    if request.method == "POST" : 
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        bio = request.form.get("bio")
        # check if already exists
        user = User.query.filter_by(email=email).first()
        if user :
            return render_template("register.html",e_error="User already exists , try to log in")
        # else create another one
        new_user =  User(username=username, email=email , bio=bio, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        return redirect("/login")
    return render_template("register.html")