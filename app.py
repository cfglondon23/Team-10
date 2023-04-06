from flask import Flask, render_template, redirect, request, url_for, flash,session, send_from_directory
from flask_login import LoginManager, login_user,current_user,logout_user,login_required
from initial import login_manager,create_app
import json
from models import Volunteer, VolunteerObject, JobObject, School, Hires, loginSchool, loginVolunteer
from datetime import datetime

dummy_jobs = [
    {
        "id": 1,
        "name": "Charity Run",
        "location": "Central Park",
        "description": "Help us organize a charity run in Central Park.",
        "date": datetime(2023, 5, 10),
        "startTime": datetime(2023, 5, 10, 8, 0),
        "endTime": datetime(2023, 5, 10, 12, 0),
        "ownerID": 1,
        "volunteerID": None
    },
    {
        "id": 2,
        "name": "Food Drive",
        "location": "New York City Food Bank",
        "description": "We need volunteers to help distribute food to families in need.",
        "date": datetime(2023, 6, 15),
        "startTime": datetime(2023, 6, 15, 10, 0),
        "endTime": datetime(2023, 6, 15, 14, 0),
        "ownerID": 2,
        "volunteerID": None
    },
    {
        "id": 3,
        "name": "Beach Cleanup",
        "location": "Rockaway Beach",
        "description": "Help us keep our beaches clean!",
        "date": datetime(2023, 7, 20),
        "startTime": datetime(2023, 7, 20, 9, 0),
        "endTime": datetime(2023, 7, 20, 12, 0),
        "ownerID": 3,
        "volunteerID": None
    }
]


app = create_app()

with app.app_context():
    JobObject.loadtotalJobs()


# Define a function to load a user given their ID
@login_manager.user_loader
def load_user(user_id):
    try:
        return VolunteerObject.getUser(user_id)
    except:
        return None

#route for MainPage page
@app.route('/', methods =['POST','GET'])
def MainPage():
    
    return render_template('MainPage.html', totalJobs=dummy_jobs)
# totalJobs=JobObject.totalJobs
      
@app.route('/Signup',methods =['POST','GET'])
def register():
    
    if current_user.is_authenticated and current_user.isValidated():
        return redirect(url_for('MainPage'))
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
                    
    return render_template('Signup.html', title="Sign Up", )

  
@app.route('/login',methods =['POST','GET'])
def Login():
    # If user is already authenticated and validated, redirect to MainPage page    
    if current_user.is_authenticated and current_user.isValidated():
        return redirect(url_for('MainPage'))
    else:
        if request.method == "POST":
            user = loginVolunteer(request.form["email"],request.form["password"])
            if user:
                session["id"] = user.get_id()
                login_user(user)
                
                flash(f'Welcome {user.get_firstName()}','success')
                return redirect(url_for('MainPage'))

            else:
                flash(f'Invalid Credentials','danger')

    return render_template('Login.html',title="Login")


# @app.route('/MainPage',methods =['POST','GET'])
# def MainPage():
    
    
    
    
#     return render_template('MainPage.html',title="Listings")