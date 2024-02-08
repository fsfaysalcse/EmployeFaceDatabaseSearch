import face_recognition
import numpy as np

def encode_face(image_array):
    face_encodings = face_recognition.face_encodings(image_array)
    return face_encodings[0] if face_encodings else None

def compare_faces(known_face_encodings, face_encoding_to_check, tolerance=0.6):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding_to_check, tolerance)
    return matches
