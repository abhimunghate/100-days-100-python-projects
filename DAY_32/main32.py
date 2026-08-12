# This is Day 32 project : Drawing Pad App

import tkinter as tk
from tkinter import colorchooser, filedialog
from PIL import ImageGrab

root = tk.Tk()
root.title("Drawing Pad App")
root.geometry("700x650")
root.configure(bg="#f0f0f0")

current_color = "black"
current_thickness = 2
current_tool = "freehand"

start_x = None
start_y = None
preview_shape = None

canvas = tk.Canvas(root, width=600, height=450, bg="white", relief="ridge", bd=2)
canvas.pack(pady=20)

def draw(event):
    if current_tool not in ("freehand", "eraser"):
        return
    
    x, y = event.x, event.y
    if current_tool == "freehand":
        color = current_color
    else:
        color = "white"
    canvas.create_oval(
        x - current_thickness, y - current_thickness,
        x + current_thickness, y + current_thickness,
        fill=color, outline=color
    )
    
def start_shape(event):
    global start_x, start_y
    if current_tool in ("rectangle", "oval", "line", "triangle"):
        start_x = event.x
        start_y = event.y

def draw_shape(event):
    global preview_shape
    if current_tool not in ("rectangle", "oval", "line", "triangle"):
        return

    if preview_shape:
        canvas.delete(preview_shape)

    if current_tool == "rectangle":
        preview_shape = canvas.create_rectangle(start_x, start_y, event.x, event.y, outline=current_color, width=current_thickness)
    elif current_tool == "oval":
        preview_shape = canvas.create_oval(start_x, start_y, event.x, event.y, outline=current_color, width=current_thickness)
    elif current_tool == "line":
        preview_shape = canvas.create_line(start_x, start_y, event.x, event.y, fill=current_color, width=current_thickness)
    elif current_tool == "triangle":
        preview_shape = canvas.create_polygon(start_x, event.y, (start_x + event.x) / 2, start_y, event.x, event.y, outline=current_color, fill="", width=current_thickness)
        
def finish_shape(event):
    global preview_shape
    if current_tool not in ("rectangle", "oval", "line", "triangle"):
        return

    if preview_shape:
        canvas.delete(preview_shape)

    if current_tool == "rectangle":
        canvas.create_rectangle(start_x, start_y, event.x, event.y, outline=current_color, width=current_thickness)
    elif current_tool == "oval":
        canvas.create_oval(start_x, start_y, event.x, event.y, outline=current_color, width=current_thickness)
    elif current_tool == "line":
        canvas.create_line(start_x, start_y, event.x, event.y, fill=current_color, width=current_thickness)
    elif current_tool == "triangle":
        canvas.create_polygon(start_x, event.y, (start_x + event.x) / 2, start_y, event.x, event.y, outline=current_color, fill="", width=current_thickness)
    preview_shape = None
    
def clear_canvas():
    canvas.delete("all")
    
def change_color():
    global current_color
    color = colorchooser.askcolor()[1]
    if color:
        current_color = color
        
def change_thickness(value):
    global current_thickness
    current_thickness = int(value)
    
def select_tool(tool):
    global current_tool
    current_tool = tool
    tool_label.config(text=f"Tool: {tool.capitalize()}")
    
def save_drawing():
    try:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Image", "*.png"), ("JPEG Image", "*.jpg"), ("All Files", "*.*")])

        if not file_path:
            return
        x = root.winfo_rootx() + canvas.winfo_x()
        y = root.winfo_rooty() + canvas.winfo_y()
        x2 = x + canvas.winfo_width()
        y2 = y + canvas.winfo_height()
        image = ImageGrab.grab(bbox=(x, y, x2, y2))
        image.save(file_path)
        print(f"Drawing saved successfully: {file_path}")
    except Exception as e:
        print(f"Error saving drawing: {e}")
    
canvas.bind("<Button-1>", start_shape)
canvas.bind("<B1-Motion>", lambda event: (draw(event) if current_tool in ("freehand", "eraser") else draw_shape(event)))
canvas.bind("<ButtonRelease-1>", finish_shape)

control_frame = tk.Frame(root, bg="#f0f0f0")
control_frame.pack(pady=10)

color_btn = tk.Button(control_frame, text="Choose Color", command=change_color, bg="#4CAF50", fg="black", font=("Arial", 10))
color_btn.grid(row=0, column=0, padx=5)

clear_btn = tk.Button(control_frame, text="Clear Canvas", command=clear_canvas, bg="#f44336", fg="black", font=("Arial", 10))
clear_btn.grid(row=0, column=1, padx=5)

save_btn = tk.Button(control_frame, text="Save Drawing", command=save_drawing, bg="#2196F3", fg="white", font=("Arial", 10))
save_btn.grid(row=0, column=2, padx=5)

tool_frame = tk.Frame(root, bg="#f0f0f0")
tool_frame.pack(pady=5)

freehand_btn = tk.Button(tool_frame, text="Freehand", command=lambda: select_tool("freehand"), font=("Arial", 10))
freehand_btn.grid(row=0, column=0, padx=5)

eraser_btn = tk.Button(tool_frame, text="Eraser", command=lambda: select_tool("eraser"), font=("Arial", 10))
eraser_btn.grid(row=0, column=1, padx=5)

rectangle_btn = tk.Button(tool_frame, text="Rectangle", command=lambda: select_tool("rectangle"), font=("Arial", 10))
rectangle_btn.grid(row=0, column=2, padx=5)

oval_btn = tk.Button(tool_frame, text="Oval", command=lambda: select_tool("oval"), font=("Arial", 10))
oval_btn.grid(row=0, column=3, padx=5)

line_btn = tk.Button(tool_frame, text="Line", command=lambda: select_tool("line"), font=("Arial", 10))
line_btn.grid(row=0, column=4, padx=5)

triangle_btn = tk.Button(tool_frame, text="Triangle", command=lambda: select_tool("triangle"), font=("Arial", 10))
triangle_btn.grid(row=0, column=5, padx=5)

thickness_label = tk.Label(tool_frame, text="Thickness : ", bg="#f0f0f0", font=("Arial", 10))
thickness_label.grid(row=0, column=6, padx=5)

thickness_slider = tk.Scale(tool_frame, from_=1, to=10, orient="horizontal", command=change_thickness, bg="#f0f0f0")
thickness_slider.set(2)
thickness_slider.grid(row=0, column=7, padx=5)

tool_label = tk.Label(root, text="Tool: Freehand", bg="#f0f0f0", font=("Arial", 11))
tool_label.pack(pady=5)

root.mainloop()

# Done