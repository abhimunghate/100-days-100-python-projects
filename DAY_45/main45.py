# This is Day 45 project : Graph Plotter

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

class GraphPlotterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Graph Plotter")
        self.root.geometry("1100x750")
        self.data = None
        self.x = []
        self.y = []
        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self.root, text="Graph Plotter", font=("Arial", 24, "bold"))
        title.pack(pady=10)
        
        data_frame = tk.LabelFrame(self.root, text="Data Input", padx=10, pady=10)
        data_frame.pack(fill="x", padx=15, pady=5)
        
        tk.Label(data_frame, text="X Values : ").grid(row=0, column=0, sticky="w")
        self.x_entry = tk.Entry(data_frame, width=70)
        self.x_entry.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(data_frame, text="Y Values : ").grid(row=1, column=0, sticky="w")
        self.y_entry = tk.Entry(data_frame, width=70)
        self.y_entry.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Button(data_frame, text="Use Manual Data", command=self.use_manual_data).grid(row=2, column=1, sticky="w", pady=5)
        tk.Button(data_frame, text="Load CSV / Excel", command=self.load_file).grid(row=2, column=1, sticky="e", pady=5)

        settings_frame = tk.LabelFrame(self.root, text="Graph Settings", padx=10, pady=10)
        settings_frame.pack(fill="x", padx=15, pady=5)
        
        tk.Label(settings_frame, text="Graph Type : ").grid(row=0, column=0, padx=5)
        self.graph_type = ttk.Combobox(settings_frame, values=["Line Graph", "Bar Chart", "Scatter Plot", "Pie Chart", "Histogram", "Area Chart"], state="readonly", width=20)
        self.graph_type.current(0)
        self.graph_type.grid(row=0, column=1, padx=5)
        
        tk.Label(settings_frame, text="Color:").grid(row=0, column=2, padx=5)
        self.color = ttk.Combobox(settings_frame, values=["blue", "red", "green", "orange", "purple", "black", "cyan", "magenta"], state="readonly", width=12)
        self.color.current(0)
        self.color.grid(row=0, column=3, padx=5)
        
        tk.Label(settings_frame, text="Marker:").grid(row=0, column=4, padx=5)
        self.marker = ttk.Combobox(settings_frame, values=["o", "s", "^", "D", "*", "+", "x", "."], state="readonly", width=8)
        self.marker.current(0)
        self.marker.grid(row=0, column=5, padx=5)
        
        self.grid_var = tk.BooleanVar(value=True)
        tk.Checkbutton(settings_frame, text="Grid", variable=self.grid_var).grid(row=0, column=6, padx=10)
        
        self.legend_var = tk.BooleanVar(value=True)
        tk.Checkbutton(settings_frame, text="Legend", variable=self.legend_var).grid(row=0, column=7, padx=10)

        label_frame = tk.LabelFrame(self.root, text="Graph Labels", padx=10, pady=10)
        label_frame.pack(fill="x", padx=15, pady=5)
        
        tk.Label(label_frame, text="Graph Title : ").grid(row=0, column=0)
        self.title_entry = tk.Entry(label_frame, width=25)
        self.title_entry.insert(0, "Graph Plotter")
        self.title_entry.grid(row=0, column=1, padx=10)
        
        tk.Label(label_frame, text="X-axis Label:").grid(row=0, column=2)
        self.x_label_entry = tk.Entry(label_frame, width=25)
        self.x_label_entry.insert(0, "X-axis")
        self.x_label_entry.grid(row=0, column=3, padx=10)
        
        tk.Label(label_frame, text="Y-axis Label:").grid(row=0, column=4)
        self.y_label_entry = tk.Entry(label_frame, width=25)
        self.y_label_entry.insert(0, "Y-axis")
        self.y_label_entry.grid(row=0, column=5, padx=10)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        tk.Button(button_frame, text="Plot Graph", command=self.plot_graph, width=15).pack(side="left", padx=5)
        tk.Button(button_frame, text="Clear", command=self.clear_data, width=15).pack(side="left", padx=5)
        tk.Button(button_frame, text="Save Graph", command=self.save_graph, width=15).pack(side="left", padx=5)

        self.figure = plt.Figure(figsize=(8, 4.5), dpi=100)
        self.axis = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().pack(fill="both", expand=True, padx=15, pady=10)

    def use_manual_data(self):
        try:
            x_text = self.x_entry.get().strip()
            y_text = self.y_entry.get().strip()

            if not x_text or not y_text:
                raise ValueError("Please enter both X and Y values.")
            self.x = list(map(float,x_text.split()))
            self.y = list(map(float,y_text.split()))
            self.validate_data()
            messagebox.showinfo("Success", "Manual data loaded successfully.")
        except ValueError as error:
            messagebox.showerror("Invalid Data", str(error))

    def validate_data(self):
        if len(self.x) != len(self.y):
            raise ValueError("X and Y values must have the same number of values.")
        if len(self.x) == 0:
            raise ValueError("Data cannot be empty.")

    def load_file(self):
        filename = filedialog.askopenfilename(filetypes=[("Data Files", "*.csv *.xlsx *.xls"), ("CSV Files", "*.csv"), ("Excel Files", "*.xlsx *.xls")])

        if not filename:
            return
        try:
            if filename.lower().endswith(".csv"):
                self.data = pd.read_csv(filename)
            else:
                self.data = pd.read_excel(filename)
            if len(self.data.columns) < 2:
                raise ValueError("File must contain at least two columns.")
            columns = list(self.data.columns)
            self.choose_columns(columns)
        except Exception as error:
            messagebox.showerror("File Error", str(error))

    def choose_columns(self, columns):
        window = tk.Toplevel(self.root)
        window.title("Choose Columns")
        window.geometry("400x250")
        
        tk.Label(window, text="Select X-axis column : ").pack(pady=10)
        x_column = ttk.Combobox(window, values=columns, state="readonly", width=30)
        x_column.current(0)
        x_column.pack()

        tk.Label(window, text="Select Y-axis column : ").pack(pady=10)
        y_column = ttk.Combobox(window, values=columns, state="readonly", width=30)
        y_column.current(1)
        y_column.pack()

        def load_selected_columns():
            try:
                self.x = self.data[ x_column.get()].tolist()
                self.y = self.data[ y_column.get()].tolist()
                self.validate_data()

                self.x_entry.delete( 0, tk.END)
                self.x_entry.insert( 0, "Data loaded from file")
                self.y_entry.delete( 0, tk.END)
                self.y_entry.insert( 0, "Data loaded from file")
                window.destroy()
                messagebox.showinfo( "Success", "Data loaded successfully.")
            except Exception as error:
                messagebox.showerror( "Data Error", str(error))
        tk.Button(window, text="Load Data", command=load_selected_columns, width=15).pack(pady=20)

    def plot_graph(self):
        try:
            if not self.x or not self.y:
                self.use_manual_data()
                if not self.x:
                    return
            self.validate_data()

            graph_type = (self.graph_type.get())
            color = self.color.get()
            marker = self.marker.get()
            title = (self.title_entry.get())
            x_label = (self.x_label_entry.get())
            y_label = (self.y_label_entry.get())
            self.axis.clear()

            if graph_type == "Line Graph":
                self.axis.plot(self.x, self.y, color=color, marker=marker, label="Line Graph")
            elif graph_type == "Bar Chart":
                self.axis.bar(self.x, self.y, color=color, label="Bar Chart")
            elif graph_type == "Scatter Plot":
                self.axis.scatter(self.x, self.y, color=color, marker=marker, label="Scatter Plot")
            elif graph_type == "Pie Chart":
                self.axis.pie(self.y, labels=self.x, autopct="%1.1f%%")
            elif graph_type == "Histogram":
                self.axis.hist(self.y, bins=10, color=color, edgecolor="black", label="Histogram")
            elif graph_type == "Area Chart":
                self.axis.fill_between(self.x, self.y, color=color, alpha=0.5, label="Area Chart")
                self.axis.plot(self.x, self.y, color=color, marker=marker)

            self.axis.set_title(title)
            self.axis.set_xlabel(x_label)
            self.axis.set_ylabel(y_label)

            if self.grid_var.get():
                self.axis.grid(True)

            if (self.legend_var.get() and graph_type != "Pie Chart"):
                self.axis.legend()
            self.figure.tight_layout()
            self.canvas.draw()
        except Exception as error:
            messagebox.showerror("Plot Error", str(error))

    def save_graph(self):
        filename = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Image", "*.png"), ("JPG Image", "*.jpg"), ("PDF Document", "*.pdf")])

        if not filename:
            return
        try:
            self.figure.savefig(filename, bbox_inches="tight")
            messagebox.showinfo("Success", f"Graph saved successfully:\n{filename}")
        except Exception as error:
            messagebox.showerror("Save Error", str(error))

    def clear_data(self):
        self.x = []
        self.y = []
        self.data = None
        self.x_entry.delete(0, tk.END)
        self.y_entry.delete(0, tk.END)
        self.axis.clear()
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphPlotterGUI(root)
    root.mainloop()
    
# Done