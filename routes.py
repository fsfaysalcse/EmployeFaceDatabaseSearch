from flask import request, jsonify
from werkzeug.utils import secure_filename
import numpy as np
import os
import face_recognition
import base64
from app import app, db
from models import Employee

@app.route('/')
def index():
    return "Welcome to the face recognition API"

@app.route('/upload', methods=['POST'])
def upload_employee():
    name = request.form.get('name')
    email = request.form.get('email')
    photo = request.files.get('photo')
    if not photo:
        return jsonify({"error": "Photo is required"}), 400

    if Employee.query.filter_by(email=email).first():
        return jsonify({"error": "Email already exists"}), 400

    filename = secure_filename(photo.filename)
    photo_path = os.path.join('uploads', filename)
    photo.save(photo_path)

    image = face_recognition.load_image_file(photo_path)
    encodings = face_recognition.face_encodings(image)
    if not encodings:
        os.remove(photo_path)
        return jsonify({"error": "No face detected in the photo"}), 400

    unknown_encoding = encodings[0]
    employees = Employee.query.all()
    for employee in employees:
        known_encoding = np.frombuffer(base64.b64decode(employee.face_encoding), dtype=np.float64)
        match = face_recognition.compare_faces([known_encoding], unknown_encoding, tolerance=0.6)
        if match[0]:
            os.remove(photo_path)
            return jsonify({"error": f"Employee already registered: {employee.name}"}), 400

    serialized_encoding = base64.b64encode(np.array(unknown_encoding).astype(np.float64)).decode('utf-8')
    new_employee = Employee(name=name, email=email, face_encoding=serialized_encoding)
    db.session.add(new_employee)
    db.session.commit()

    return jsonify({"message": "Employee uploaded successfully"}), 201

@app.route('/search', methods=['POST'])
def search_employee():
    photo = request.files.get('photo')
    if not photo:
        return jsonify({"error": "Photo is required"}), 400

    image = face_recognition.load_image_file(photo.stream)
    encodings = face_recognition.face_encodings(image)
    if not encodings:
        return jsonify({"error": "No face detected in the photo"}), 400

    unknown_encoding = encodings[0]
    employees = Employee.query.all()
    for employee in employees:
        known_encoding = np.frombuffer(base64.b64decode(employee.face_encoding), dtype=np.float64)
        match = face_recognition.compare_faces([known_encoding], unknown_encoding, tolerance=0.6)
        if match[0]:
            return jsonify({"employee": {"name": employee.name, "email": employee.email}}), 200

    return jsonify({"message": "No matching employee found"}), 404


@app.errorhandler(404)
def not_found(error):
    return jsonify({"message": "404 - ERROR"}), 404
