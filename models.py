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
    location = db.Column(db.String, unique=False, primary_key=False,nullable=False)
    description = db.Column(db.String, unique=False, primary_key=False,nullable=False)
    
    jobs = db.relationship('Job', backref='volunteer', lazy=True, cascade="all,delete")
    hire = db.relationship('Hires', backref='volunteer', lazy=True, cascade="all,delete")
    
class School(db.Model):
    id = db.Column(db.Integer, primary_key=True,nullable=False)
    name = db.Column(db.String, unique=False, primary_key=False,nullable=False)
    email = db.Column(db.String, unique=True, primary_key=False,nullable=False)
    password = db.Column(db.String, unique=False, primary_key=False,nullable=False)
    location = db.Column(db.String, unique=False, primary_key=False,nullable=False)
    
    jobs = db.relationship('Job', backref='school', lazy=True, cascade="all,delete")
    # hire = db.relationship('Hires', backref='user', lazy=True, cascade="all,delete")
    
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True,nullable=False)
    name = db.Column(db.String, unique=True, primary_key=False,nullable=False)
    # capacity = db.Column(db.Integer, unique=False, primary_key=False,nullable=False)
    location = db.Column(db.String, unique=False, primary_key=False,nullable=False)
    description = db.Column(db.String, unique=False, primary_key=False,nullable=False)
    date = db.Column(db.DateTime, unique=False, primary_key=False,nullable=False)
    startTime = db.Column(db.DateTime, unique=False, primary_key=False,nullable=False)
    endTime = db.Column(db.DateTime, unique=False, primary_key=False,nullable=False)
    ownerID = db.Column(db.Integer, db.ForeignKey('school.id'), primary_key=False, nullable=False)
    
    hire = db.relationship('Hires', backref='event', lazy=True, cascade="all,delete")
    
    
class Hires(db.Model):
    id = db.Column(db.Integer, primary_key=True,nullable=False)
    volunteerID = db.Column(db.Integer, db.ForeignKey('volunteer.id'), primary_key=False,nullable=False)
    jobID = db.Column(db.Integer, db.ForeignKey('job.id'), primary_key=False,nullable=False)
    

def loginVolunteer(email: str, password: str) ->  None or str:
    user = Volunteer.query.filter_by(email=email).first()

    if not user:
        return None
    
    isValid = check_password_hash(user.password,password)
    if isValid:
        return VolunteerObject(user.id, user.firstName, user.surname, user.email, user.location)
        
    return None

def loginSchool(email: str, password: str) ->  None or str:
    user = School.query.filter_by(email=email).first()

    if not user:
        return None
    
    isValid = check_password_hash(user.password,password)
    if isValid:
        return SchoolObject(user.id, user.name, user.email, user.location)
        
    return None

def createVolunteer(volunteerInfo: dict, isOrg):
    
    user = Volunteer(
        firstName=volunteerInfo.get("firstName"),
        surname=volunteerInfo.get("surname"),
        email=volunteerInfo.get("email"),
        password= generate_password_hash(volunteerInfo.get("password")),
        location=volunteerInfo.get("location"),
    )

    if user:
        db.session.add(user)
        db.session.commit()
        return VolunteerObject(user.id, user.firstName, user.surname, user.email, user.isOrg, user.isValidated)
    
    return None 
    
 
def createSchool(schoolInfo: dict, isOrg):
    
    user = School(
        name=schoolInfo.get("name"),
        email=schoolInfo.get("email"),
        password= generate_password_hash(schoolInfo.get("password")),
        location= schoolInfo.get("location")
    )

    if user:
        db.session.add(user)
        db.session.commit()
        return SchoolObject(user.id, user.firstName, user.surname, user.email, user.isOrg, user.isValidated)
    
    return None 

class VolunteerObject():
    # stores all volunteer objects
    allVolunteers= {}
    # constructor method for the VolunteerObject
    def __init__(self,id: str, firstName: str, surname: str, email: str, location: str)->None:
        self.__id = id
        self.__firstName = firstName
        self.__surname = surname
        self.__email = email 
        self.is_authenticated = True
        self.is_active = True
        self.is_anonymous = False
        self.__location = location
        
        self._jobs: Dict[int, JobObject]
        self._jobs = {}
        
        self.__hire: Dict[int, JobObject]
        self.__hire = {}
        
        self.load_hire()
        self.load_jobs()
        VolunteerObject.allVolunteers[self.__id] = self
        
        
    def get_id(self):
        return self.__id
    
    def get_firstName(self):
        return self.__firstName
    
    def get_surname(self):
        return self.__surname
    
    def get_email(self):
        return self.__email
    
    def get_location(self):
        return self.__location
    
    # def addJob(self, jobID: int):
    #     self._jobs[jobID] = JobObject.totaljobs[jobID]
        
    def removeEvent(self, jobID: int):
        self._jobs.pop(jobID)
    
    def ownsEvent(self, jobID: int):
        return jobID in self._jobs
    
    def load_jobs(self):
        jobs = Job.query.filter_by(ownerID=abs(self._id)).all()
        
        for job in jobs:
            self._jobs[job.id] = JobObject.getEvent(job.id)
    
    # Retrieves an Event object with the specified jobID, retrieves all Hires objects associated with the event, extracts the email addresses of the attendees, sends cancellation emails (if applicable), removes the Event object from the JobObject.totaljobs dictionary, deletes the Event object from the database
    # def deleteEvent(self, jobID: int):
    #     event = Event.query.get(jobID)
        
    #     eventRecord = Event.query.filter_by(id=jobID).first()
        
    #     attRecords = Hires.query.filter_by(jobID=jobID).all()
    #     attEmails = []
    
    #     for record in attRecords:
    #         attendee = User.query.filter_by(id=record.attendeeID).first()
    #         attEmails.append(attendee.email)
        
    #     if len(attEmails) != 0:    
    #         uniqueEmails = list(set(attEmails))
    #         sendCancelEmail(uniqueEmails, eventRecord.name)
        
    #     if event is not None:
    #         JobObject.totaljobs.pop(jobID)
    #         db.session.delete(event)
    #         db.session.commit()
                        
            
    #     return True
    
    def get_hire(self):
        return self.__hire
    
    def load_hire(self):
        self.__hire = {}
        hire = Hires.query.filter_by(attendeeID=abs(self.__id)).all()
        for hire in hire:
            self.__hire[hire.id] = JobObject.getEvent(hire.jobID)
        
    #Retrieves an event object from an event ID, creates a new hire for the event and the user buying the hire, adds the hire to the user's hire collection, and notifies the event owner and organisers that a new participant has joined the job. The function returns the ID of the new hire.    
    def buyHires(self, jobID: int):

        job = JobObject.getEvent(int(jobID))
        if not event: return None
        
        hire = Hires(
            jobID = jobID,
            attendeeID = abs(self.__id)
        )
        
        db.session.add(hire) 
        db.session.commit()
        
        self.__hire[hire.id] = event 
        
        ownerID = job.get_ownerID()
        ownerEmail = School.query.filter_by(id=ownerID).first().email
    
        # organiserIDs = Promotion.query.filter_by(jobID=jobID).all()
        # orgEmails = []
        
        # for orgRecord in organiserIDs:
        #     organiserRecord = User.query.filter_by(id=orgRecord.organiserID).first()
        #     orgEmails.append(organiserRecord.email)
        
        # job.add_participant([ownerEmail], orgEmails)

        return hire.id
    
    # # deletes a hire
    # def deleteHires(self, hireID: int):
    #     hire = Hires.query.filter_by(id=hireID).first()
    #     if not hire:
    #         print("No Hires Found :(")
    #         return
    #     event = JobObject.getEvent(hire.jobID)
        
    #     self.deleteBarcode(hireID)
    #     db.session.delete(hire)
    #     db.session.commit()
        
    #     job.remove_participant() 
    #     self.__hire.pop(hireID)
 
        
    # def load_jobs(self):
    #     jobs = Promotion.query.filter_by(organiserID=abs(self.__id)).all()
    #     for event in jobs:
    #         self._jobs[job.jobID] = JobObject.getEvent(job.jobID)
    
    # def ownsHires(self,id):
    #     return id in self.__hire

    @staticmethod
    def getUser(id: str):
        return VolunteerObject.allUsers.get(int(id))
    
    def getUserE(email):
        user = Volunteer.query.filter_by(email=email).first()
        return user
    
    @staticmethod
    def userExists(email: str) -> bool:
        user = Volunteer.query.filter_by(email=email).first()
    
        if user:
            return True
        else:
            return False
    

class JobObject():
        totalJobs = {}
    
        def __init__(self, id:int, name: str, location:str, description:str, startTime:datetime, endTime:datetime, duration:int, date:datetime, capacity:int, ownerID:int)->None:
            
            self.__id = id
            self.__name = Markup(name).striptags()
            self.__location = Markup(location).striptags()
            self.__description = Markup(description).striptags()
            self.__startTime = startTime.strftime("%H:%M")
            self.__endTime = endTime.strftime("%H:%M")
            self.__date = date.strftime("%d/%m/%Y")
            # self.__capacity = capacity
            self.__ownerID = ownerID
            
            
            self.__participants = self.load_participants()
            # self.__organisers: Dict[int, Dict[str,str]]
            # self.__organisers = {}
            # self.load_organisers()
            JobObject.totalJobs[id] = self
            
        def get_id(self):
            return self.__id
    
        def get_name(self):
            return self.__name
    
        def get_location(self):
            return self.__location
    
        def get_description(self):
            return self.__description
        
        def get_start(self):
            return self.__start
    
        def get_end(self):
            return self.__end
    
        def get_date(self):
            return self.__date
    
        def get_startTime(self):
            return self.__startTime
        
        def get_endTime(self):
            return self.__endTime
        
        # def get_capacity(self):
        #     return self.__capacity
        
        # def get_participants(self):
        #     return self.__participants
        
        def get_ownerID(self):
            return self.__ownerID
    
        # def get_organisers(self):
        #     return self.__organisers
    
        # # Define a method to add an organiser to the current event
        # def add_organiser(self, userID):
            
        #     user = User.query.filter_by(id=userID).first()
        #     if not user: 
        #         return
        #     # Add the user to the organisers dictionary, with their ID as the key
        #     self.__organisers[userID] = {
        #         "firstName": Markup(user.firstName).striptags(),
        #         "surname": Markup(user.surname).striptags(),
        #         "email": Markup(user.email).striptags(),
        #         "userID": userID
        #     }
        
        # def load_organisers(self):
        #     organisers = Promotion.query.filter_by(jobID=self.__id).all()
            
        #     for organiser in organisers:
        #         self.add_organiser(organiser.organiserID)
        
        def load_participants(self) -> int:
            return Hires.query.filter_by(jobID=self.__id).count()
        
        # Adds a participant to the current event
        def add_participant(self, ownerEmail, orgEmails):
            self.__participants +=1
            # Check if the event is at 90% capacity or greater
                

        # def remove_organiser(self, userID):
        #     self.__organisers.pop(userID)
        
        def remove_participant(self):
            self.__participants -= 1
        
        def isFull(self):
            return self.__participants == self.__capacity
            
        # def isEventPassed(self):
        #     over = self.__startTime < datetime.now()
  
        #     if over:
        #         #conditions here
        #         return over
        
        #returns true if the event is at 95% capacity or greater
        def capacityWarning(self):
            return (self.__participants / self.__capacity) >= 0.95
        
        #returns true if the event is at 90% capacity or greater
        def capacityWarning10(self):
            return (self.__participants / self.__capacity) >= 0.90
        
        @staticmethod
        def getJob(jobID: int):
            return JobObject.totalJobs.get(jobID)
        
        @staticmethod
        def loadtotalJobs():
            totalJobs = Job.query.all()
            
            for job in totalJobs:
                JobObject(
                    id = job.id,
                    name = job.name,
                    location = job.location,
                    description = job.description,
                    startTime = job.startTime,
                    endTime = job.endTime,
                    duration = job.duration,
                    capacity = job.capacity,
                    ownerID = job.ownerID,
                    date = job.date
                )


class SchoolObject():
    
        totalSchools = {}
        
        def __init__(self,id: str, name: str, email: str, location: str)->None:
            self.__id = id
            self.__name = Markup(name).striptags()
            self.__email = email 
            self.is_authenticated = True
            self.is_active = True
            self.is_anonymous = False
            self.__location = location
            
            self._jobs: Dict[int, JobObject]
            self._jobs = {}
            
            self.__hire: Dict[int, JobObject]
            self.__hire = {}
            
            self.load_hire()
            self.load_jobs()
            VolunteerObject.allVolunteers[self.__id] = self
            
            
        def get_id(self):
            return self.__id
        
        def get_firstName(self):
            return self.__firstName
        
        def get_surname(self):
            return self.__surname
        
        def get_email(self):
            return self.__email
        
        def get_location(self):
            return self.__location
        
        
        def get_ownerID(self):
            return self.__ownerID
        
        def addJob(self, jobID: int):
            self._jobs[jobID] = JobObject.totaljobs[jobID]

            # Creates an Event object with details provided by the details dictionary, stores it in a database, creates an JobObject with the same details, adds the Event ID to the instance of the class, and returns the JobObject.
        def createJob(self, details):
            startTime = datetime.strptime(details["starttime"], "%H:%M")
            endTime = datetime.strptime(details["endtime"], "%H:%M")
            duration = endTime - startTime
            date = datetime.strptime(details["date"], "%Y-%m-%d")

            job = Job(
                name = details["name"],
                description = details["description"],
                location = details["location"],
                startTime = startTime,
                endTime = endTime,
                date = date,
                duration = duration.total_seconds(),
                capacity = details["capacity"],
                ownerID = self.__id
            )
            db.session.add(job)
            db.session.commit()
            
            JobObject = JobObject(
                id = job.id,
                name = job.name,
                location = job.location,
                description = job.description,
                startTime = job.startTime,
                endTime = job.endTime,
                duration = job.duration,
                date = job.date,
                # capacity = job.capacity,
                ownerID = job.ownerID,
            )
            self.addJob(job.id)
            
            return JobObject
    
    
        # Define a method to add an organiser to the current event
        # def add_organiser(self, userID):
            
        #     user = User.query.filter_by(id=userID).first()
        #     if not user: 
        #         return
        #     # Add the user to the organisers dictionary, with their ID as the key
        #     self.__organisers[userID] = {
        #         "firstName": Markup(user.firstName).striptags(),
        #         "surname": Markup(user.surname).striptags(),
        #         "email": Markup(user.email).striptags(),
        #         "userID": userID
        #     }
        
        # def load_organisers(self):
        #     organisers = Promotion.query.filter_by(jobID=self.__id).all()
            
        #     for organiser in organisers:
        #         self.add_organiser(organiser.organiserID)
        
        def load_participants(self) -> int:
            return Hires.query.filter_by(jobID=self.__id).count()
        
        # Adds a participant to the current event
        def add_participant(self, ownerEmail, orgEmails):
            self.__participants +=1
            # Check if the event is at 90% capacity or greater
                

        def remove_organiser(self, userID):
            self.__organisers.pop(userID)
        
        def remove_participant(self):
            self.__participants -= 1
        

        @staticmethod
        def getJob(jobID: int):
            return JobObject.totaljobs.get(jobID)
        
        @staticmethod
        def loadTotaljobs():
            totaljobs = Event.query.all()
            
            for event in totaljobs:
                JobObject(
                    id = job.id,
                    name = job.name,
                    location = job.location,
                    description = job.description,
                    startTime = job.startTime,
                    endTime = job.endTime,
                    duration = job.duration,
                    capacity = job.capacity,
                    ownerID = job.ownerID,
                    date = job.date
                )
                
        @staticmethod
        def getUser(id: str):
            return SchoolObject.allUsers.get(int(id))
        
        def getUserE(email):
            user = School.query.filter_by(email=email).first()
            return user
        
        @staticmethod
        def userExists(email: str) -> bool:
            user = School.query.filter_by(email=email).first()
        
            if user:
                return True
            else:
                return False