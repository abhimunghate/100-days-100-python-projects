# This is Day 57 project : ASCII Art Generator

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image
import colorama
from colorama import Fore, Style
import os

ASCII_SETS = {
    "Detailed": "@%#*+=-:. ",
    "Simple": "#*:. ",
    "Blocks": "█▓▒░ ",
    "Binary": "10 ",
    "Classic": "@#S%?*+;:,."
}

DEFAULT_WIDTH = 100
MAX_WIDTH = 200

colorama.init(autoreset=True)

def load_image(image_path, new_width=100):
    """Load and resize an image while maintaining aspect ratio.
    The 0.55 factor compensates for terminal character height."""
    
    img = Image.open(image_path)
    if img.width == 0:
        raise ValueError("Invalid image width.")
    
    aspect_ratio = img.height / img.width
    new_height = max(1, int(new_width * aspect_ratio * 0.55))
    
    try:
        resample_filter = Image.Resampling.LANCZOS
    except AttributeError:
        resample_filter = Image.LANCZOS
        
    img = img.resize((new_width, new_height), resample_filter)
    return img

def convert_to_grayscale(img):
    """Convert an image to grayscale."""
    return img.convert("L")

def map_pixels_to_ascii(img, ascii_chars):
    """Convert grayscale pixels into ASCII characters.

    Pixel values range from 0 to 255.
    The formula dynamically maps them to any ASCII character set."""
    
    pixels = img.getdata()
    ascii_str = "".join([ascii_chars[pixel * (len(ascii_chars) - 1) // 255] for pixel in pixels])
    return ascii_str

def generate_ascii_art(image_path, new_width=100, character_set="Detailed"):
    """Generate grayscale ASCII art from an image."""

    if new_width < 10 or new_width > MAX_WIDTH:
        raise ValueError(f"Width must be between 10 and {MAX_WIDTH}.")
    
    img = load_image(image_path, new_width)
    gray_image = convert_to_grayscale(img)
    ascii_chars = ASCII_SETS[character_set]
    ascii_str = map_pixels_to_ascii(gray_image, ascii_chars)
    ascii_art = "\n".join(ascii_str[i:i + new_width] for i in range(0, len(ascii_str), new_width))
    return ascii_art

def rgb_to_ansi_color(r, g, b):
    """Convert RGB values to an ANSI terminal color.

    Uses the dominant RGB component to approximate the original image color."""

    brightness = (r + g + b) / 3
    if brightness < 35:
        return Fore.BLACK

    if r > g * 1.4 and r > b * 1.4:
        return Fore.RED

    if g > r * 1.3 and g > b * 1.3:
        return Fore.GREEN

    if b > r * 1.3 and b > g * 1.3:
        return Fore.BLUE

    if r > 120 and g > 80 and b < 80:
        return Fore.YELLOW

    if r > 100 and b > 100 and g < 100:
        return Fore.MAGENTA

    if g > 100 and b > 100 and r < 100:
        return Fore.CYAN

    if brightness > 180:
        return Fore.WHITE

    return Fore.LIGHTBLACK_EX

def generate_color_ascii(image_path, new_width=80):
    """Generate colorized ASCII art for terminal output."""

    img = Image.open(image_path).convert("RGB")
    aspect_ratio = img.height / img.width
    new_height = max(1, int(new_width * aspect_ratio * 0.55))

    try:
        resample_filter = Image.Resampling.LANCZOS
    except AttributeError:
        resample_filter = Image.LANCZOS

    img = img.resize((new_width, new_height), resample_filter)
    ascii_chars = "@%#*+=-:. "
    lines = []
    
    for y in range(img.height):
        line = ""
        for x in range(img.width):
            r, g, b = img.getpixel((x, y))
            brightness = (0.299 * r + 0.587 * g + 0.114 * b)
            index = int(brightness * (len(ascii_chars) - 1) / 255)
            character = ascii_chars[index]
            color = rgb_to_ansi_color(r, g, b)
            line += (color + character + Style.RESET_ALL)
        lines.append(line)
    return "\n".join(lines)

def save_ascii_art(ascii_art, output_path):
    """Save ASCII art to a text file."""
    
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(ascii_art)

class ASCIIArtGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ASCII Art Generator - Day 57")
        self.root.geometry("1200x750")
        self.root.minsize(900, 600)
        self.root.configure(bg="#f2f2f2")

        self.image_path = None
        self.ascii_art = ""

        self.create_widgets()

    def create_widgets(self):
        header = tk.Frame(self.root, bg="#222222", height=70)
        header.pack(fill="x")
        title = tk.Label(header, text="ASCII ART GENERATOR", font=("Segoe UI", 22, "bold"), fg="white", bg="#222222")
        title.pack(pady=(10, 0))
        subtitle = tk.Label(header, text="Image • Color", font=("Segoe UI", 10), fg="#cccccc", bg="#222222")
        subtitle.pack()

        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=15, pady=15)
        self.image_tab = tk.Frame(notebook, bg="#f2f2f2")
        notebook.add(self.image_tab, text="  Image to ASCII  ")
        self.create_image_tab()

    def create_image_tab(self):
        control_frame = tk.Frame(self.image_tab, bg="#f2f2f2")
        control_frame.pack(fill="x", padx=10, pady=10)
        ttk.Button(control_frame, text="📁 Select Image", command=self.select_image).grid(row=0, column=0, padx=5, pady=5)
        self.file_label = tk.Label(control_frame, text="No image selected", bg="#f2f2f2", fg="#555555", anchor="w")
        self.file_label.grid(row=0, column=1, columnspan=3, sticky="ew", padx=10)
        tk.Label(control_frame, text="Width:", bg="#f2f2f2").grid(row=1, column=0, padx=5, pady=5)
        self.width_var = tk.StringVar(value=str(DEFAULT_WIDTH))
        ttk.Entry(control_frame, textvariable=self.width_var, width=10).grid(row=1, column=1, padx=5)
        tk.Label(control_frame, text="Character Set:", bg="#f2f2f2").grid(row=1, column=2, padx=5)
        self.charset_var = tk.StringVar(value="Detailed")
        ttk.Combobox(control_frame, textvariable=self.charset_var, values=list(ASCII_SETS.keys()), state="readonly", width=15).grid(row=1, column=3, padx=5)

        ttk.Button(control_frame, text="⚡ Generate ASCII", command=self.generate).grid(row=2, column=0, padx=5, pady=8)
        ttk.Button(control_frame, text="💾 Save TXT", command=self.save).grid(row=2, column=1, padx=5)
        ttk.Button(control_frame, text="📋 Copy", command=self.copy_to_clipboard).grid(row=2, column=2, padx=5)
        ttk.Button(control_frame, text="🗑 Clear", command=self.clear).grid(row=2, column=3, padx=5)
        control_frame.columnconfigure(1, weight=1)

        preview_frame = tk.Frame(self.image_tab, bg="#111111")
        preview_frame.pack(fill="both", expand=True, padx=10, pady=10)
        self.ascii_text = tk.Text(preview_frame, bg="#111111", fg="#eeeeee", insertbackground="white", font=("Consolas", 8), wrap="none", padx=10, pady=10)
        vertical_scroll = ttk.Scrollbar(preview_frame, orient="vertical", command=self.ascii_text.yview)
        horizontal_scroll = ttk.Scrollbar(preview_frame, orient="horizontal", command=self.ascii_text.xview)
        self.ascii_text.configure(yscrollcommand=vertical_scroll.set, xscrollcommand=horizontal_scroll.set)
        self.ascii_text.grid(row=0, column=0, sticky="nsew")
        vertical_scroll.grid(row=0, column=1, sticky="ns")
        horizontal_scroll.grid(row=1, column=0, sticky="ew")
        preview_frame.rowconfigure(0, weight=1)
        preview_frame.columnconfigure(0, weight=1)

    def select_image(self):
        file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif *.webp"), ("All Files", "*.*")])
        if not file_path:
            return

        self.image_path = file_path
        self.file_label.config(text=os.path.basename(file_path))

    def generate(self):
        if not self.image_path:
            messagebox.showwarning("No Image", "Please select an image first.")
            return

        try:
            width = int(self.width_var.get())
            charset = self.charset_var.get()

            self.ascii_art = generate_ascii_art(self.image_path, width, charset)
            self.ascii_text.delete("1.0", tk.END)
            self.ascii_text.insert(tk.END, self.ascii_art)
        except ValueError as error:
            messagebox.showerror("Invalid Input", str(error))
        except Exception as error:
            messagebox.showerror("Error", f"Could not generate ASCII art:\n\n{error}")
            
    def save(self):
        if not self.ascii_art:
            messagebox.showwarning("Nothing to Save", "Generate ASCII art first.")
            return

        output_path = filedialog.asksaveasfilename(title="Save ASCII Art", defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if not output_path:
            return

        try:
            save_ascii_art(self.ascii_art, output_path)
            messagebox.showinfo("Saved", f"ASCII art saved successfully:\n\n{output_path}")
        except Exception as error:
            messagebox.showerror("Save Error", str(error))
            
    def copy_to_clipboard(self):
        if not self.ascii_art:
            messagebox.showwarning("Nothing to Copy", "Generate ASCII art first.")
            return

        self.root.clipboard_clear()
        self.root.clipboard_append(self.ascii_art)
        self.root.update()
        messagebox.showinfo("Copied", "ASCII art copied to clipboard.")
        
    def clear(self):
        self.ascii_art = ""
        self.ascii_text.delete("1.0", tk.END)
        self.image_path = None
        self.file_label.config(text="No image selected")

def main():
    print(Fore.GREEN + "\nASCII Art Generator - Day 57")
    
    while True:
        print()
        print(Fore.CYAN + "=" * 55)
        print(Fore.CYAN + "        ASCII ART GENERATOR")
        print(Fore.CYAN + "=" * 55)

        print("1. Generate Colorized ASCII from Image")
        print("2. Open Tkinter GUI")
        print("3. Exit")
        print()

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            image_path = input("Enter image path: ").strip()
            if not os.path.isfile(image_path):
                print(Fore.RED + "Image file not found.")
                continue

            try:
                width = int(input("Enter ASCII width (default 80): ") or 80)
                print("\033[2J\033[H", end="")
                print(Fore.CYAN + "COLORIZED ASCII ART")
                print()

                ascii_art = generate_color_ascii(image_path, width)
                print(ascii_art)
                input("\nPress Enter to return to the main menu...")
            except ValueError:
                print(Fore.RED + "Please enter a valid width.")
            except Exception as error:
                print(Fore.RED + f"Error: {error}")
        elif choice == "2":
                root = tk.Tk()
                app = ASCIIArtGUI(root)
                def on_close():
                    root.destroy()
                root.protocol("WM_DELETE_WINDOW", on_close)
                root.mainloop()
        elif choice == "3":
            print(Fore.GREEN + "\nThank you for using ASCII Art Generator!")
            break
        else:
            print(Fore.RED + "Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
    
# Done