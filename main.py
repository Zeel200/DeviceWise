## TO RUN THIS
# python main.py

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
    return redirect(url_for("home"))

@webapp.route("/home")
def home():
    return render_template("homePage.html",
                            username=session.get('username'), 
                            websiteName=WEBSITE_NAME, 
                            LOGGEDIN=session.get('LOGGEDIN'))
    



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
                    return render_template("login.html", websiteName = WEBSITE_NAME,  LOGGEDIN=False)
                


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


@webapp.route("/signup", methods= ["GET", "POST"])
def signup():

    if request.method == "GET":
        if session.get("LOGGEDIN"):
            return redirect(url_for("home"))
        else:
            return render_template("signup.html", websiteName = WEBSITE_NAME,  LOGGEDIN=False)
    elif request.method == "POST":
        fName = (request.form.get("first-name")) #required
        lName = request.form.get("last-name")
        email = (request.form.get("email")) #required
        phone = (request.form.get("phone")) #required
        username = (request.form.get("username")) #required
        password = (request.form.get("password")) #required

        user = utils.User(fName, lName, email, phone, username, password)
        user.save_tofile()

        session["LOGGEDIN"] = True
        session["username"] = username

        return redirect(url_for("home"))

@webapp.route("/about") # about route,
def about(): # what ever we have to show on /about we will return that from this function
    return render_template("about.html")




if __name__ == '__main__':
    webapp.run(host="0.0.0.0", port=5501, debug=True)

