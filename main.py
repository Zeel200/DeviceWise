import dotenv
from flask import Flask, render_template, request, redirect, url_for, session
import os
import utils
# from flask_sqlalchemy import SQLAlchemy



WEBSITE_NAME = "DeviseWise"
utils.load_data()
dotenv.load_dotenv()
# create flask application
webapp = Flask(__name__)
webapp.secret_key = os.getenv("SECRET_KEY")


@webapp.route('/')
def h():
    return redirect(url_for("login"))

@webapp.route("/home")
def home():
    if session.get("LOGGEDIN") is not None:
        return render_template("homePage.html", username=session.get('username'), websiteName=WEBSITE_NAME)
    else:
        return redirect(url_for("login"))


@webapp.route("/about") # about route,
def about(): # what ever we have to show on /about we will return that from this function
    return "Hey I am zeel patel, akdjajhsdkjh...."

@webapp.route("/login", methods=["GET", "POST"])
def login():
    if session.get("LOGGEDIN"):
        return redirect(url_for("home"))
    
    else:

        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")

            if username:          
                user = utils.get_user(username)
                if not user:
                    return render_template("login.html", websiteName = WEBSITE_NAME)
                


            if username and utils.check_password(user, password):
                session["username"] = username
                session["password"] = password
                session["LOGGEDIN"] = True
                print(session["LOGGEDIN"])
                return redirect(url_for("home"))

        
        
        return render_template("login.html", websiteName = WEBSITE_NAME)

@webapp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@webapp.route("/navbar" )
def nav():
    return render_template("navbar.html")


@webapp.route("/signup")
def signup():
    return render_template("signup.html", websiteName = WEBSITE_NAME)

if __name__ == '__main__':
    webapp.run(port=5501, debug=True)
