# This is Day 73 project : Handwriting Digit Recognition

import os
import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np
import tensorflow as tf
from PIL import Image, ImageOps, ImageDraw
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import (Conv2D, MaxPooling2D, Flatten, Dense, Input)
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping

MODEL_FILE = "digit_model.keras"
CANVAS_SIZE = 280
MODEL_IMAGE_SIZE = 28

def train_model():
    print("\nLoading MNIST dataset...")
    mnist = tf.keras.datasets.mnist
    (X_train, y_train), (X_test, y_test) = mnist.load_data()

    X_train = X_train.astype("float32") / 255.0
    X_test = X_test.astype("float32") / 255.0
    X_train = X_train.reshape(-1, 28, 28, 1)
    X_test = X_test.reshape(-1, 28, 28, 1)

    print("Training samples:", len(X_train))
    print("Testing samples:", len(X_test))

    datagen = ImageDataGenerator(rotation_range=10, width_shift_range=0.10, height_shift_range=0.10, zoom_range=0.10)
    datagen.fit(X_train)

    model = Sequential([
        Input(shape=(28, 28, 1)),
        Conv2D(32, (3, 3), activation="relu"),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation="relu"),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(128, activation="relu"),
        Dense(10, activation="softmax")
    ])

    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    model.summary()

    early_stopping = EarlyStopping(monitor="val_accuracy", patience=3, restore_best_weights=True)

    print("\nTraining model...")
    history = model.fit(datagen.flow(X_train, y_train, batch_size=128), epochs=15, validation_data=(X_test, y_test), callbacks=[early_stopping])

    test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
    print(f"\nTest Accuracy: {test_accuracy * 100:.2f}%")

    model.save(MODEL_FILE)
    print(f"Model saved as: {MODEL_FILE}")
    return model, test_accuracy

if os.path.exists(MODEL_FILE):
    print("\nSaved model found.")
    print("Loading trained model...")
    model = load_model(MODEL_FILE)

    model_accuracy = None
else:
    print("\nNo saved model found.")
    print("Training a new CNN model...")
    model, model_accuracy = train_model()

def preprocess_image(image):
    image = image.convert("L")

    image_array = np.array(image)
    average_pixel = np.mean(image_array)
    if average_pixel > 127:
        image = ImageOps.invert(image)

    image_array = np.array(image)
    coords = np.argwhere(image_array > 30)
    if coords.size > 0:
        y_min, x_min = coords.min(axis=0)
        y_max, x_max = coords.max(axis=0)
        image = image.crop((x_min, y_min, x_max + 1, y_max + 1))

    image.thumbnail((20, 20), Image.Resampling.LANCZOS)

    final_image = Image.new("L", (28, 28), 0)
    x = (28 - image.width) // 2
    y = (28 - image.height) // 2

    final_image.paste(image, (x, y))
    image_array = np.array(final_image).astype("float32") / 255.0
    image_array = image_array.reshape(1, 28, 28, 1)
    return image_array

def predict_digit(image):
    processed_image = preprocess_image(image)
    predictions = model.predict(processed_image, verbose=0)[0]
    predicted_digit = int(np.argmax(predictions))
    confidence = float(np.max(predictions)) * 100
    return predicted_digit, confidence

root = tk.Tk()
root.title("Handwriting Digit Recognition")
root.geometry("850x700")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

title_label = tk.Label(root, text="Handwriting Digit Recognition", font=("Arial", 24, "bold"), bg="#1e1e1e", fg="white")
title_label.pack(pady=(25, 5))

subtitle_label = tk.Label(root, text="CNN-based MNIST Digit Classifier", font=("Arial", 11), bg="#1e1e1e", fg="#aaaaaa")
subtitle_label.pack(pady=(0, 20))

main_frame = tk.Frame(root, bg="#1e1e1e")
main_frame.pack()

drawing_frame = tk.Frame(main_frame, bg="#1e1e1e")
drawing_frame.grid(row=0, column=0, padx=20)

drawing_label = tk.Label(drawing_frame, text="Draw a Digit", font=("Arial", 13, "bold"), bg="#1e1e1e", fg="white")
drawing_label.pack(pady=(0, 10))

canvas = tk.Canvas(drawing_frame, width=CANVAS_SIZE, height=CANVAS_SIZE, bg="black", highlightthickness=2, highlightbackground="#555555")
canvas.pack()

drawing_image = Image.new("L", (CANVAS_SIZE, CANVAS_SIZE), 0)
drawing = ImageDraw.Draw(drawing_image)

last_x = None
last_y = None

def start_drawing(event):
    global last_x, last_y
    last_x = event.x
    last_y = event.y

def draw(event):
    global last_x, last_y
    if last_x is not None and last_y is not None:
        canvas.create_line(last_x, last_y, event.x, event.y, fill="white", width=20, capstyle=tk.ROUND, smooth=True)
        drawing.line([(last_x, last_y), (event.x, event.y)], fill=255, width=20)
        radius = 10
        drawing.ellipse((event.x - radius, event.y - radius, event.x + radius, event.y + radius), fill=255)

    last_x = event.x
    last_y = event.y

def stop_drawing(event):
    global last_x, last_y
    last_x = None
    last_y = None

canvas.bind("<Button-1>", start_drawing)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", stop_drawing)

result_frame = tk.Frame(main_frame, width=350, height=300, bg="#2b2b2b")
result_frame.grid(row=0, column=1, padx=20)
result_frame.grid_propagate(False)

result_title = tk.Label(result_frame, text="Prediction", font=("Arial", 15, "bold"), bg="#2b2b2b", fg="white")
result_title.pack(pady=(35, 15))

result_label = tk.Label(result_frame, text="-", font=("Arial", 70, "bold"), bg="#2b2b2b", fg="#3498db")
result_label.pack(pady=10)

confidence_label = tk.Label(result_frame, text="Confidence: -", font=("Arial", 13), bg="#2b2b2b", fg="#aaaaaa")
confidence_label.pack(pady=10)

model_label = tk.Label(result_frame, text="CNN Model\nMNIST Dataset", font=("Arial", 10), bg="#2b2b2b", fg="#888888")
model_label.pack(pady=15)

def clear_canvas():
    global drawing_image, drawing
    canvas.delete("all")

    drawing_image = Image.new("L", (CANVAS_SIZE, CANVAS_SIZE), 0)
    drawing = ImageDraw.Draw(drawing_image)

    result_label.config(text="-")
    confidence_label.config(text="Confidence: -")

def predict_drawing():
    try:
        image_array = np.array(drawing_image)
        if np.max(image_array) == 0:
            messagebox.showwarning("Empty Canvas", "Please draw a digit first.")
            return

        digit, confidence = predict_digit(drawing_image)
        result_label.config(text=str(digit))
        confidence_label.config(text=f"Confidence: {confidence:.2f}%")
    except Exception as e:
        messagebox.showerror("Prediction Error", f"Could not predict the digit.\n\n{e}")

def upload_image():
    file_path = filedialog.askopenfilename(title="Select Digit Image", filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")])
    if not file_path:
        return

    try:
        image = Image.open(file_path)
        digit, confidence = predict_digit(image)
        result_label.config(text=str(digit))
        confidence_label.config(text=f"Confidence: {confidence:.2f}%")
    except Exception as e:
        messagebox.showerror("Image Error", f"Could not process the image.\n\n{e}")

button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(pady=25)

predict_button = tk.Button(button_frame, text="Predict Drawing", command=predict_drawing, font=("Arial", 11, "bold"), bg="#3498db", fg="white", activebackground="#2980b9", activeforeground="white", relief="flat", padx=20, pady=10, cursor="hand2")
predict_button.pack(side="left", padx=8)

upload_button = tk.Button(button_frame, text="Upload Image", command=upload_image, font=("Arial", 11, "bold"), bg="#9b59b6", fg="white", activebackground="#8e44ad", activeforeground="white", relief="flat", padx=20, pady=10, cursor="hand2")
upload_button.pack(side="left", padx=8)

clear_button = tk.Button(button_frame, text="Clear", command=clear_canvas, font=("Arial", 11, "bold"), bg="#555555", fg="white", activebackground="#444444", activeforeground="white", relief="flat", padx=25, pady=10, cursor="hand2")
clear_button.pack(side="left", padx=8)

if model_accuracy is not None:
    accuracy_text = (f"Model Test Accuracy: {model_accuracy * 100:.2f}%")
else:
    accuracy_text = ("Trained CNN Model Loaded")

accuracy_label = tk.Label(root, text=accuracy_text, font=("Arial", 10), bg="#1e1e1e", fg="#aaaaaa")
accuracy_label.pack(pady=(0, 15))

root.mainloop()

# Done