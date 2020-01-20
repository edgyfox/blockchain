# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 16:07:31 2019

"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy, sqlalchemy
from flask_marshmallow import Marshmallow
import os
from exceptions import NotFoundError, BadRequest

# setting up app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
db = SQLAlchemy(app)
marsh = Marshmallow(app)

# Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(40))
    last_name = db.Column(db.String(40))
    
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
        
# Student schema for field exposure
class StudentSchema(marsh.Schema):
    class Meta:
        fields = ('first_name', 'last_name', 'id')
        
student_schema = StudentSchema()
students_schema = StudentSchema(many = True)

# =============================================================================
# ROUTES
# =============================================================================
@app.route('/student', methods = ['POST'])
def add_student():
    if (not request.json.get('first_name')) or (not request.json.get('last_name')):
        raise BadRequest('first_name and last_name required.', 400)
    
    fname = request.json['first_name']
    lname = request.json['last_name']
    
    new_student = Student(fname, lname)
    
    db.session.add(new_student)
    db.session.commit()
    
    return student_schema.jsonify(new_student)

@app.route('/student', methods = ['GET'])
def get_students():
    all_students = Student.query.all()
    result = students_schema.dump(all_students)
    return jsonify(result)

@app.route('/student/<id>', methods = ['DELETE'])
def delete_student(id):
    try:
        student = Student.query.get(id)
        db.session.delete(student)
        db.session.commit()
        return student_schema.jsonify(student)
    except sqlalchemy.orm.exc.UnmappedInstanceError:
        raise NotFoundError('UnmappedInstanceError occured', 404)
        
@app.route('/student/<id>', methods = ['PUT'])
def modify_student(id):
    if (not request.json.get('first_name')) or (not request.json.get('last_name')):
        raise BadRequest('first_name and last_name required.', 400)
    try:
        student = Student.query.get(id)
        fname = request.json['first_name']
        lname = request.json['last_name']
        student.first_name = fname
        student.last_name = lname
        db.session.commit()
    except sqlalchemy.orm.exc.UnmappedInstanceError:
        raise NotFoundError('UnmappedInstanceError occured', 404)
        
# =============================================================================
# ERROR REGISTRATIONS
# =============================================================================
@app.errorhandler(NotFoundError)
def handle_not_found_request(error):
    payload = dict(())
    payload['status'] = error.status
    payload['message'] = error.message
    return jsonify(payload), 404

@app.errorhandler(BadRequest)
def handle_bad_request(error):
    payload = dict(())
    payload['status'] = error.status
    payload['message'] = error.message
    return jsonify(payload), 400

if __name__ == "__main__":
    app.run(debug=True)