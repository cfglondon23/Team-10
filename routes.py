from flask import Flask, render_template, redirect, request, url_for, flash,session, send_from_directory
from flask_login import LoginManager, login_user,current_user,logout_user,login_required
from initial import login_manager,create_app, Message
import json
from models import Volunteer, VolunteerObject


app,mail = create_app()

with app.app_context():
    JobObject.loadTotalJobs()


# Define a function to load a user given their ID
@login_manager.user_loader
def load_user(user_id):
    try:
        return VolunteerObject.getUser(user_id)
    except:
        return None

#route for index page
@app.route('/', methods =['POST','GET'])
def index():
    
    return render_template('index.html', title="Events",  )
      
      
@app.route('/Signup',methods =['POST','GET'])
def register():
    
    if current_user.is_authenticated and current_user.isValidated():
        return redirect(url_for('index'))
    else:
        if request.method == "POST":
            alreadyExists = VolunteerObject.userExists(request.form["email"])
            if alreadyExists:
                flash(f'Email already exists','danger')        
            else: 
                # If the email is not registered, create a new user
                user = VolunteerObject.createVolunteer(request.form, False)
                if user:
                    session["email"] = request.form["email"]
                    
                    login_user(user)
                    session["id"] = user.get_id()
                else:
                    flash(f'Invalid Credentials','danger')
                    
    return render_template('Signup.html', title="Sign Up")

  
@app.route('/login',methods =['POST','GET'])
def Login():
    # If user is already authenticated and validated, redirect to index page    
    if current_user.is_authenticated and current_user.isValidated():
        return redirect(url_for('index'))
    else:
        if request.method == "POST":
            user = loginVolunteer(request.form["email"],request.form["password"])
            if user:
                session["id"] = user.get_id()
                login_user(user)
                
                flash(f'Welcome {user.get_firstName()}','success')
                return redirect(url_for('index'))

            else:
                flash(f'Invalid Credentials','danger')

    return render_template('Login.html',title="Login")

@app.route('/Signup',methods =['POST','GET'])
def MainPage():
    
    
    
    
    return render_template('Login.html',title="Login")