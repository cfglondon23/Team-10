from flask import Flask, render_template, redirect, request, url_for, flash,session, send_from_directory
from flask_login import LoginManager, login_user,current_user,logout_user,login_required
from initial import login_manager,create_app, Message
import json
from models import Volunteer, VolunteerObject


app,mail = create_app()

# Define a function to load a user given their ID
# @login_manager.user_loader
# def load_user(user_id):
#     try:
#         return UserObject.getUser(user_id)
#     except:
#         return None

#route for index page
@app.route('/', methods =['POST','GET'])
def index():
    
    
    return render_template('index.html', title="Events")
      