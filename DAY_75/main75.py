# This is Day 75 project : Face Detection & Recognition App

import os
import cv2
import numpy as np
import tkinter as tk

from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "models")
KNOWN_FACES_DIR = os.path.join(BASE_DIR, "known_faces")
DETECTOR_MODEL = os.path.join(MODEL_DIR, "face_detection_yunet_2023mar.onnx")
RECOGNITION_MODEL = os.path.join(MODEL_DIR, "face_recognition_sface_2021dec.onnx")


COSINE_THRESHOLD = 0.363
DETECTION_THRESHOLD = 0.6
NMS_THRESHOLD = 0.3
TOP_K = 5000

if not os.path.exists(DETECTOR_MODEL):
    raise FileNotFoundError(f"YuNet model not found.\n\n Expected:\n {DETECTOR_MODEL}")

if not os.path.exists(RECOGNITION_MODEL):
    raise FileNotFoundError(f"SFace model not found.\n\n Expected:\n {RECOGNITION_MODEL}")

detector = cv2.FaceDetectorYN.create(DETECTOR_MODEL, "", (320, 320), DETECTION_THRESHOLD, NMS_THRESHOLD, TOP_K)

recognizer = cv2.FaceRecognizerSF.create(RECOGNITION_MODEL, "")

known_features = []
known_names = []

def get_image_files(folder):
    extensions = (".jpg", ".jpeg", ".png", ".bmp", ".webp")

    files = []
    if not os.path.exists(folder):
        return files

    for filename in os.listdir(folder):
        if filename.lower().endswith(extensions):
            files.append(os.path.join(folder, filename))
    return files

def load_known_faces():
    global known_features
    global known_names

    known_features = []
    known_names = []

    if not os.path.exists(KNOWN_FACES_DIR):
        os.makedirs(KNOWN_FACES_DIR)
        return

    person_folders = [folder for folder in os.listdir(KNOWN_FACES_DIR) if os.path.isdir(os.path.join(KNOWN_FACES_DIR, folder))]
    for person_name in person_folders:
        person_folder = os.path.join(KNOWN_FACES_DIR, person_name)
        image_files = get_image_files(person_folder)
        for image_path in image_files:
            image = cv2.imread(image_path)
            if image is None:
                continue

            features = extract_face_feature(image)
            if features is not None:
                known_features.append(features)
                known_names.append(person_name)
    print(f"Loaded {len(known_features)} known face(s).")

def detect_faces(image):
    height, width = image.shape[:2]
    detector.setInputSize((width, height))
    _, faces = detector.detect(image)
    if faces is None:
        return []
    return faces

def extract_face_feature(image):
    faces = detect_faces(image)
    if len(faces) == 0:
        return None

    largest_face = max(faces, key=lambda face: face[2] * face[3])
    aligned_face = recognizer.alignCrop(image, largest_face)
    feature = recognizer.feature(aligned_face)
    return feature

def recognize_face(feature):
    if len(known_features) == 0:
        return "Unknown", 0.0

    best_name = "Unknown"
    best_score = -1.0
    for index, known_feature in enumerate(known_features):
        score = recognizer.match(known_feature, feature, cv2.FaceRecognizerSF_FR_COSINE)
        if score > best_score:
            best_score = score
            best_name = known_names[index]

    if best_score >= COSINE_THRESHOLD:
        return best_name, best_score
    return "Unknown", best_score

def draw_face_info(image, face, name, score):
    x, y, w, h = face[:4].astype(np.int32)
    confidence = face[14]
    
    if name == "Unknown":
        box_color = (0, 0, 255)
    else:
        box_color = (0, 255, 0)

    cv2.rectangle(image, (x, y), (x + w, y + h), box_color, 2)
    
    if name == "Unknown":
        label = (f"Unknown | Detection: {confidence * 100:.1f}%")
    else:
        label = (f"{name} | Match: {score * 100:.1f}%")

    text_y = y - 10
    if text_y < 20:
        text_y = y + h + 25

    cv2.putText(image, label, (x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.55, box_color, 2, cv2.LINE_AA)

def process_image(image):
    output = image.copy()
    faces = detect_faces(image)

    recognized_count = 0

    for face in faces:
        aligned_face = recognizer.alignCrop(image, face)
        feature = recognizer.feature(aligned_face)
        name, score = recognize_face(feature)

        if name != "Unknown":
            recognized_count += 1

        draw_face_info(output, face, name, score)
    return output, len(faces), recognized_count

def open_image():
    global current_image
    
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.webp")])
    if not file_path:
        return

    image = cv2.imread(file_path)
    if image is None:
        messagebox.showerror("Error", "Could not open the selected image.")
        return

    processed_image, face_count, recognized_count = (process_image(image))
    current_image = processed_image
    display_image(processed_image)
    status_label.config(text=(f"Detected Faces: {face_count}  |  Recognized: {recognized_count}"))

def display_image(image):
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(rgb_image)

    max_width = 700
    max_height = 450
    width, height = pil_image.size

    scale = min(max_width / width, max_height / height, 1)
    new_width = int(width * scale)
    new_height = int(height * scale)
    
    pil_image = pil_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    tk_image = ImageTk.PhotoImage(pil_image)
    image_label.config(image=tk_image)
    image_label.image = tk_image

def save_image():
    global current_image
    if current_image is None:
        messagebox.showwarning("No Image", "Please open an image first.")
        return

    save_path = filedialog.asksaveasfilename(title="Save Result", defaultextension=".jpg", filetypes=[("JPEG Image", "*.jpg"), ("PNG Image", "*.png")])
    if not save_path:
        return

    cv2.imwrite(save_path, current_image)
    messagebox.showinfo("Saved", "Processed image saved successfully.")

def start_webcam():
    global webcam_running
    global camera

    if webcam_running:
        return

    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        messagebox.showerror("Camera Error", "Could not open the webcam.")
        return

    webcam_running = True
    status_label.config(text="Webcam: Running")
    update_webcam()

def update_webcam():
    global webcam_running
    if not webcam_running:
        return

    ret, frame = camera.read()
    if not ret:
        stop_webcam()
        return

    frame = cv2.flip(frame, 1)
    processed_frame, face_count, recognized_count = (process_image(frame))
    display_image(processed_frame)

    status_label.config(text=(f"Webcam | Faces: {face_count} | Recognized: {recognized_count}"))
    root.after(15, update_webcam)

def stop_webcam():
    global webcam_running
    global camera

    webcam_running = False

    if camera is not None:
        camera.release()
        camera = None

    status_label.config(text="Webcam: Stopped")

def clear_image():
    global current_image
    current_image = None

    image_label.config(image="")
    image_label.image = None
    status_label.config(text="Ready")

def close_application():
    stop_webcam()
    root.destroy()

current_image = None
camera = None
webcam_running = False

load_known_faces()

root = tk.Tk()
root.title("Face Detection & Recognition")
root.geometry("850x700")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

title_label = tk.Label(root, text="Face Detection & Recognition", font=("Arial", 24, "bold"), bg="#1e1e1e", fg="white")
title_label.pack(pady=(20, 5))

subtitle_label = tk.Label(root, text="YuNet DNN + SFace + OpenCV", font=("Arial", 11), bg="#1e1e1e", fg="#aaaaaa")
subtitle_label.pack(pady=(0, 15))

image_frame = tk.Frame(root, width=720, height=470, bg="#2b2b2b")
image_frame.pack(padx=30, pady=5)
image_frame.pack_propagate(False)
image_label = tk.Label(image_frame, text="Upload an image or start the webcam", font=("Arial", 14), bg="#2b2b2b", fg="#aaaaaa")
image_label.pack(expand=True)

status_label = tk.Label(root, text="Ready", font=("Arial", 11, "bold"), bg="#1e1e1e", fg="#dddddd")
status_label.pack(pady=10)

button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(pady=5)

upload_button = tk.Button(button_frame, text="Upload Image", command=open_image, font=("Arial", 11, "bold"), bg="#3498db", fg="white", activebackground="#2980b9", activeforeground="white", relief="flat", padx=20, pady=10, cursor="hand2")
upload_button.pack(side="left", padx=5)

webcam_button = tk.Button(button_frame, text="Start Webcam", command=start_webcam, font=("Arial", 11, "bold"), bg="#27ae60", fg="white", activebackground="#229954", activeforeground="white", relief="flat", padx=20, pady=10, cursor="hand2")
webcam_button.pack(side="left", padx=5)

stop_button = tk.Button(button_frame, text="Stop Webcam", command=stop_webcam, font=("Arial", 11, "bold"), bg="#e67e22", fg="white", activebackground="#ca6f1e", activeforeground="white", relief="flat", padx=20, pady=10, cursor="hand2")
stop_button.pack(side="left", padx=5)

save_button = tk.Button(button_frame, text="Save Result", command=save_image, font=("Arial", 11, "bold"), bg="#8e44ad", fg="white", activebackground="#71368a", activeforeground="white", relief="flat", padx=20, pady=10, cursor="hand2")
save_button.pack(side="left", padx=5)

clear_button = tk.Button(button_frame, text="Clear", command=clear_image, font=("Arial", 11, "bold"), bg="#555555", fg="white", activebackground="#444444", activeforeground="white", relief="flat", padx=20, pady=10, cursor="hand2")
clear_button.pack(side="left", padx=5)

exit_button = tk.Button(button_frame, text="Exit", command=close_application, font=("Arial", 11, "bold"), bg="#c0392b", fg="white", activebackground="#a93226", activeforeground="white", relief="flat", padx=20, pady=10, cursor="hand2")
exit_button.pack(side="left", padx=5)

root.protocol("WM_DELETE_WINDOW", close_application)
root.mainloop()

# Done