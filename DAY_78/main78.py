# This is Day 78 project : Object Detection App

import os
import threading
import tkinter as tk

from tkinter import (filedialog, messagebox, ttk)
import cv2
import torch
from PIL import Image, ImageTk

CUSTOM_MODEL = "models/best.pt"
DEFAULT_MODEL = "yolov5s"

model = None
camera = None
webcam_running = False
current_frame = None
photo_image = None

def load_model():
    global model

    try:
        if os.path.exists(CUSTOM_MODEL):
            status_label.config(text="Loading custom YOLOv5 model...")
            model = torch.hub.load("ultralytics/yolov5", "custom", path=CUSTOM_MODEL, force_reload=False)
            model_name_label.config(text="Model: Custom YOLOv5")
        else:
            status_label.config(text="Loading pretrained YOLOv5s...")
            model = torch.hub.load("ultralytics/yolov5", DEFAULT_MODEL, pretrained=True)
            model_name_label.config(text="Model: YOLOv5s pretrained")

        model.conf = 0.40
        status_label.config(text="Model ready")
        enable_buttons()
    except Exception as error:
        status_label.config(text="Model loading failed")
        messagebox.showerror("Model Error", str(error))

def enable_buttons():
    image_button.config(state="normal")
    webcam_button.config(state="normal")

def update_confidence(value):
    if model is not None:
        model.conf = float(value)
        confidence_label.config(text=f"Confidence: {float(value):.2f}")

def detect_image():
    global current_frame

    if model is None:
        messagebox.showwarning("Please Wait", "The model is still loading.")
        return

    image_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")])
    if not image_path:
        return

    image = cv2.imread(image_path)
    if image is None:
        messagebox.showerror("Error", "Could not open the selected image.")
        return

    try:
        results = model(image)
        detections = results.pandas().xyxy[0]

        object_count = len(detections)
        rendered = results.render()[0]
        current_frame = rendered.copy()

        display_image(rendered)
        update_detection_info(detections)
        status_label.config(text=(f"Detection completed - {object_count} object(s)"))
    except Exception as error:
        messagebox.showerror("Detection Error", str(error))

def display_image(frame):
    global photo_image

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(frame_rgb)

    max_width = 800
    max_height = 500

    width, height = image.size

    scale = min(max_width / width, max_height / height, 1)
    new_size = (int(width * scale), int(height * scale))

    image = image.resize(new_size, Image.Resampling.LANCZOS)
    photo_image = ImageTk.PhotoImage(image)
    image_label.config(image=photo_image)
    image_label.image = photo_image

def update_detection_info(detections):
    result_text.delete("1.0", tk.END)

    if detections.empty:
        result_text.insert(tk.END, "No objects detected.")
        return

    counts = (detections["name"].value_counts().to_dict())

    result_text.insert(tk.END, f"Total Objects: {len(detections)}\n\n")
    result_text.insert(tk.END, "Object Counts:\n")
    
    for name, count in counts.items():
        result_text.insert(tk.END, f"• {name}: {count}\n")

    result_text.insert(tk.END, "\nDetections:\n")
    for _, row in detections.iterrows():
        result_text.insert(tk.END, (f"• {row['name']} ({row['confidence']:.2%})\n"))

def start_webcam():
    global camera
    global webcam_running

    if model is None:
        messagebox.showwarning("Please Wait", "The model is still loading.")
        return

    if webcam_running:
        return

    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        messagebox.showerror("Camera Error", "Could not open webcam.")
        return

    webcam_running = True
    webcam_button.config(state="disabled")
    stop_button.config(state="normal")
    status_label.config(text="Webcam detection running...")
    update_webcam()

def update_webcam():
    global current_frame

    if not webcam_running:
        return

    ret, frame = camera.read()
    if not ret:
        stop_webcam()
        return

    try:
        results = model(frame)
        detections = results.pandas().xyxy[0]

        rendered = results.render()[0]
        current_frame = rendered.copy()

        display_image(rendered)
        update_detection_info(detections)
    except Exception as error:
        print("Webcam detection error:", error)

    root.after(30, update_webcam)

def stop_webcam():
    global camera
    global webcam_running

    webcam_running = False

    if camera is not None:
        camera.release()
        camera = None

    stop_button.config(state="disabled")
    webcam_button.config(state="normal")
    status_label.config(text="Webcam stopped")

def save_detection():
    if current_frame is None:
        messagebox.showwarning("No Detection", "Run object detection first.")
        return

    save_path = filedialog.asksaveasfilename(title="Save Detection", defaultextension=".jpg", filetypes=[("JPEG Image", "*.jpg"), ("PNG Image", "*.png")])
    if not save_path:
        return

    cv2.imwrite(save_path, current_frame)
    messagebox.showinfo("Saved", f"Detection saved to:\n{save_path}")

def clear_screen():
    global current_frame
    global photo_image

    current_frame = None
    photo_image = None

    image_label.config(image="")
    result_text.delete("1.0", tk.END)
    status_label.config(text="Ready")

def close_application():
    stop_webcam()
    root.destroy()

root = tk.Tk()
root.title("Day 78 - Object Detection App")
root.geometry("1100x800")
root.minsize(900, 650)

header = tk.Frame(root, pady=10)
header.pack(fill="x")

title = tk.Label(header, text="🎯 OBJECT DETECTION APP", font=("Segoe UI", 22, "bold"))
title.pack()

model_name_label = tk.Label(header, text="Loading model...", font=("Segoe UI", 10))
model_name_label.pack(pady=3)

main_frame = tk.Frame(root, padx=15, pady=10)
main_frame.pack(fill="both", expand=True)

image_frame = tk.LabelFrame(main_frame, text="Detection Preview", padx=10, pady=10)
image_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))
image_label = tk.Label(image_frame, text="Select an image or start webcam", font=("Segoe UI", 12))
image_label.pack(fill="both", expand=True)

right_frame = tk.Frame(main_frame, width=280)
right_frame.pack(side="right", fill="y")
right_frame.pack_propagate(False)

image_button = tk.Button(right_frame, text="📂 Select Image", command=detect_image, state="disabled", width=25, height=2)
image_button.pack(pady=5)

webcam_button = tk.Button(right_frame, text="📷 Start Webcam", command=start_webcam, state="disabled", width=25, height=2)
webcam_button.pack(pady=5)

stop_button = tk.Button(right_frame, text="⏹ Stop Webcam", command=stop_webcam, state="disabled", width=25, height=2)
stop_button.pack(pady=5)

save_button = tk.Button(right_frame, text="💾 Save Detection", command=save_detection, width=25, height=2)
save_button.pack(pady=5)

clear_button = tk.Button(right_frame, text="🧹 Clear", command=clear_screen, width=25, height=2)
clear_button.pack(pady=5)

confidence_label = tk.Label(right_frame, text="Confidence: 0.40", font=("Segoe UI", 10, "bold"))
confidence_label.pack(pady=(20, 5))

confidence_slider = tk.Scale(right_frame, from_=0.10, to=0.90, resolution=0.05, orient="horizontal", length=220, command=update_confidence)
confidence_slider.set(0.40)
confidence_slider.pack()

results_frame = tk.LabelFrame(right_frame, text="Detection Results", padx=5, pady=5)
results_frame.pack(fill="both", expand=True, pady=15)

result_text = tk.Text(results_frame, wrap=tk.WORD, font=("Consolas", 10))
result_text.pack(fill="both", expand=True)

status_label = tk.Label(root, text="Loading model...", anchor="w", padx=15, pady=5)
status_label.pack(fill="x")

root.protocol("WM_DELETE_WINDOW", close_application)

thread = threading.Thread(target=load_model, daemon=True)
thread.start()

root.mainloop()

# Done