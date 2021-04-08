import face_recognition
import os
import cv2

KNOWN_FACES_DIR = "known_faces"
UNKNOWN_FACES_DIR = "unknown_faces"
TOLERANCE = 0.6
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = "hog"

print("Loading known faces")

known_faces = []
known_names = []

for name in os.listdr(KNOWN_FACES_DIR):
    for filename in os.listdr(f"{KNOWN_FACES_DIR}/{name}")
    


