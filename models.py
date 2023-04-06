import random
from flask import render_template, url_for
from initial import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Boolean
from datetime import datetime, timedelta
from typing import Dict
from markupsafe import Markup
from itsdangerous import URLSafeTimedSerializer
from initial import create_app

import os
from dotenv import load_dotenv
load_dotenv()

app,mail=create_app()

class Volunteer(db.Model):
    id = db.Column(db.Integer, primary_key=True,nullable=False)
    firstName = db.Column(db.String, unique=False, primary_key=False,nullable=False)
    surname = db.Column(db.String, unique=False, primary_key=False,nullable=False)
    email = db.Column(db.String, unique=True, primary_key=False,nullable=False)
    password = db.Column(db.String, unique=False, primary_key=False,nullable=False)

class School(db.Model):
    id = db.Column(db.Integer, primary_key=True,nullable=False)
    firstName = db.Column(db.String, unique=False, primary_key=False,nullable=False)
    surname = db.Column(db.String, unique=False, primary_key=False,nullable=False)
    email = db.Column(db.String, unique=True, primary_key=False,nullable=False)
    password = db.Column(db.String, unique=False, primary_key=False,nullable=False)
    
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True,nullable=False)
    name = db.Column(db.String, unique=True, primary_key=False,nullable=False)
    capacity = db.Column(db.Integer, unique=False, primary_key=False,nullable=False)
    location = db.Column(db.String, unique=False, primary_key=False,nullable=False)
    description = db.Column(db.String, unique=False, primary_key=False,nullable=False)
    date = db.Column(db.DateTime, unique=False, primary_key=False,nullable=False)
    startTime = db.Column(db.DateTime, unique=False, primary_key=False,nullable=False)
    endTime = db.Column(db.DateTime, unique=False, primary_key=False,nullable=False)
    ownerID = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=False, nullable=False)
    
    
class Hires(db.Model):
    id = db.Column(db.Integer, primary_key=True,nullable=False)
    volunteerID = db.Column(db.Integer, db.ForeignKey('volunteer.id'), primary_key=False,nullable=False)
    jobID = db.Column(db.Integer, db.ForeignKey('job.id'), primary_key=False,nullable=False)



