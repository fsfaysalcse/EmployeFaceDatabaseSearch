from flask import request, jsonify
from werkzeug.utils import secure_filename
from PIL import Image
import numpy as np
import os
from app import app, db  # Import Flask app and database instance
from models import Employee  # Import the Employee model
from face_utils import encode_face, compare_faces  # Import utility functions
import face_recognition

@app.route('/')
def index():
    return "Welcome to the face recognition API"

@app.route('/upload', methods=['POST'])
def upload_employee():
    name = request.form['name']
    email = request.form['email']
    photo = request.files['photo']
    if not photo:
        return jsonify({"error": "Photo is required"}), 400
    
    filename = secure_filename(photo.filename)
    photo_path = os.path.join('uploads', filename)
    photo.save(photo_path)
    
    # Process the saved photo for face recognition
    image = face_recognition.load_image_file(photo_path)
    encodings = face_recognition.face_encodings(image)
    if not encodings:
        os.remove(photo_path)  # Cleanup if no face is detected
        return jsonify({"error": "No face detected in the photo"}), 400

    # Use the first encoding found
    photo_encoding = encodings[0]
    new_employee = Employee(name=name, email=email, photo=photo_encoding.tobytes())
    db.session.add(new_employee)
    db.session.commit()
    
    return jsonify({"message": "Employee uploaded successfully"}), 201

@app.route('/search', methods=['POST'])
def search_employee():
    photo = request.files['photo']
    if not photo:
        return jsonify({"error": "Photo is required"}), 400
    
    # Convert the uploaded photo to a format suitable for face recognition
    image = Image.open(photo.stream)
    image_array = np.array(image.convert('RGB'))
    encodings = face_recognition.face_encodings(image_array)
    if not encodings:
        return jsonify({"error": "No face detected in the photo"}), 400

    unknown_encoding = encodings[0]
    match_found = False
    matched_employee = None
    employees = Employee.query.all()
    for employee in employees:
        known_encoding = np.frombuffer(employee.photo, dtype=np.float64)
        if face_recognition.compare_faces([known_encoding], unknown_encoding, tolerance=0.6)[0]:
            match_found = True
            matched_employee = employee
            break
    
    if match_found:
        return jsonify({"employee": {"name": matched_employee.name, "email": matched_employee.email}}), 200
    else:
        return jsonify({"message": "No matching employee found"}), 404
