# This is Day 70 project : Data Visualizer App

import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

df = None
filtered_df = None
canvas = None
current_figure = None

def load_file(file_path):
    """Load CSV or Excel file."""
    if not file_path:
        return None

    if file_path.lower().endswith(".csv"):
        return pd.read_csv(file_path)
    elif file_path.lower().endswith(".xlsx"):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a .csv or .xlsx file.")

def update_dropdowns(columns):
    """Update all dropdown menus with dataframe columns."""
    x_dropdown.set("")
    y_dropdown.set("")
    filter_column_dropdown.set("")

    x_menu["menu"].delete(0, "end")
    y_menu["menu"].delete(0, "end")
    filter_column_menu["menu"].delete(0, "end")

    for column in columns:
        x_menu["menu"].add_command(label=column, command=lambda value=column: x_dropdown.set(value))
        y_menu["menu"].add_command(label=column, command=lambda value=column: y_dropdown.set(value))
        filter_column_menu["menu"].add_command(label=column, command=lambda value=column: filter_column_dropdown.set(value))
    filter_column_dropdown.set("")

def open_file():
    """Open file selection dialog."""
    return filedialog.askopenfilename(title="Select Data File", filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx"), ("All Supported Files", "*.csv *.xlsx")])

def handle_file_upload():
    """Load the selected CSV or Excel file."""
    global df, filtered_df
    
    file_path = open_file()
    if not file_path:
        return

    try:
        df = load_file(file_path)
        filtered_df = df.copy()
        update_dropdowns(df.columns)

        status_label.config(text=f"Loaded {len(df)} rows and {len(df.columns)} columns.")
        messagebox.showinfo("File Loaded", f"File loaded successfully!\n\n Rows: {len(df)}\n Columns: {len(df.columns)}")
    except Exception as error:
        messagebox.showerror("File Error", f"Could not load the file.\n\n{error}")

def filter_data():
    """Filter dataframe before plotting."""
    global filtered_df
    if df is None:
        messagebox.showwarning("No Data", "Please upload a CSV or Excel file first.")
        return

    filter_column = filter_column_dropdown.get()
    operator = operator_dropdown.get()
    filter_value = filter_value_entry.get().strip()

    if not filter_column:
        messagebox.showwarning("Missing Column", "Please select a filter column.")
        return

    if not filter_value:
        messagebox.showwarning("Missing Value", "Please enter a filter value.")
        return

    try:
        column_data = df[filter_column]
        try:
            numeric_value = float(filter_value)
            is_numeric = pd.api.types.is_numeric_dtype(column_data)
        except ValueError:
            is_numeric = False

        if is_numeric:
            if operator == "==":
                filtered_df = df[column_data == numeric_value]
            elif operator == ">":
                filtered_df = df[column_data > numeric_value]
            elif operator == "<":
                filtered_df = df[column_data < numeric_value]
            elif operator == ">=":
                filtered_df = df[column_data >= numeric_value]
            elif operator == "<=":
                filtered_df = df[column_data <= numeric_value]
            else:
                filtered_df = df[column_data != numeric_value]
        else:
            text_data = column_data.astype(str)
            if operator == "==":
                filtered_df = df[text_data == filter_value]
            elif operator == "!=":
                filtered_df = df[text_data != filter_value]
            elif operator == "contains":
                filtered_df = df[text_data.str.contains(filter_value, case=False, na=False)]
            else:
                messagebox.showwarning("Invalid Filter", "For text columns, use ==, !=, or contains.")
                return

        status_label.config(text=f"Filter applied: {len(filtered_df)} rows remaining.")
        messagebox.showinfo("Filter Applied", f"Original rows: {len(df)}\n Filtered rows: {len(filtered_df)}")
    except Exception as error:
        messagebox.showerror("Filter Error", f"Could not filter the data.\n\n{error}")

def reset_filter():
    """Reset dataframe to original data."""
    global filtered_df

    if df is None:
        return

    filtered_df = df.copy()
    filter_value_entry.delete(0, tk.END)
    filter_column_dropdown.set("")
    operator_dropdown.set("==")

    status_label.config(text=f"Filter reset. Showing all {len(df)} rows.")

def plot_data(data, column_x, column_y, plot_type):
    """Generate selected plot type."""
    global canvas, current_figure

    if data is None or data.empty:
        raise ValueError("No data available for plotting.")

    if column_x not in data.columns or column_y not in data.columns:
        raise ValueError("Selected columns are not available.")

    if not pd.api.types.is_numeric_dtype(data[column_y]):
        raise ValueError(f"Y-axis column '{column_y}' must contain numeric data.")

    if canvas is not None:
        canvas.get_tk_widget().destroy()

    current_figure = Figure(figsize=(7, 4.5), dpi=100)
    ax = current_figure.add_subplot(111)

    if plot_type == "Line":
        ax.plot(data[column_x], data[column_y], marker="o")
    elif plot_type == "Bar":
        ax.bar(data[column_x].astype(str), data[column_y])
    elif plot_type == "Scatter":
        if not pd.api.types.is_numeric_dtype(data[column_x]):
            raise ValueError(f"For a Scatter Plot, X-axis column '{column_x}' must contain numeric data.")

        ax.scatter(data[column_x], data[column_y])
    else:
        raise ValueError("Unsupported plot type.")

    ax.set_title(f"{plot_type} Plot: {column_x} vs {column_y}")
    ax.set_xlabel(column_x)
    ax.set_ylabel(column_y)

    current_figure.tight_layout()

    canvas = FigureCanvasTkAgg(current_figure, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)

def handle_plot():
    """Generate selected plot."""
    if df is None:
        messagebox.showwarning("No Data", "Please upload a data file first.")
        return

    column_x = x_dropdown.get()
    column_y = y_dropdown.get()
    plot_type = plot_type_dropdown.get()

    if not column_x or not column_y:
        messagebox.showwarning("Missing Columns", "Please select both X-axis and Y-axis columns.")
        return

    if not plot_type:
        messagebox.showwarning("Missing Plot Type", "Please select a plot type.")
        return

    try:
        plot_data(filtered_df, column_x, column_y, plot_type)
        status_label.config(text=(f"{plot_type} plot generated using {len(filtered_df)} rows."))
    except Exception as error:
        messagebox.showerror("Plot Error", f"Could not generate plot.\n\n{error}")

def save_plot():
    """Save the current plot as an image."""
    if current_figure is None:
        messagebox.showwarning("No Plot", "Please generate a plot first.")
        return

    file_path = filedialog.asksaveasfilename(title="Save Plot", defaultextension=".png", filetypes=[("PNG Image", "*.png"), ("JPG Image", "*.jpg"), ("JPEG Image", "*.jpeg")])
    if not file_path:
        return

    try:
        current_figure.savefig(file_path, dpi=300, bbox_inches="tight")
        status_label.config(text=f"Plot saved successfully: {file_path}")
        messagebox.showinfo("Plot Saved", f"Plot saved successfully!\n\n{file_path}")
    except Exception as error:
        messagebox.showerror("Save Error", f"Could not save the plot.\n\n{error}")

root = tk.Tk()
root.title("Data Visualizer")
root.geometry("1000x800")
root.minsize(900, 700)

title_label = tk.Label(root, text="Data Visualizer", font=("Arial", 24, "bold"))
title_label.pack(pady=(15, 5))

subtitle_label = tk.Label(root, text="Upload, filter and visualize CSV or Excel data", font=("Arial", 10))
subtitle_label.pack(pady=(0, 10))

upload_button = tk.Button(root, text="Upload File", command=handle_file_upload)
upload_button.pack(pady=8)

selection_frame = tk.Frame(root)
selection_frame.pack(pady=10)

x_label = tk.Label(selection_frame, text="X-axis:")
x_label.grid(row=0, column=0, padx=5, pady=5)
x_dropdown = tk.StringVar()
x_menu = tk.OptionMenu(selection_frame, x_dropdown, "")
x_menu.grid(row=0, column=1, padx=5, pady=5)

y_label = tk.Label(selection_frame, text="Y-axis:")
y_label.grid(row=0, column=2, padx=5, pady=5)
y_dropdown = tk.StringVar()
y_menu = tk.OptionMenu(selection_frame, y_dropdown, "")
y_menu.grid(row=0, column=3, padx=5, pady=5)

plot_type_label = tk.Label(selection_frame, text="Plot Type:")
plot_type_label.grid(row=0, column=4, padx=5, pady=5)
plot_type_dropdown = tk.StringVar(value="Line")
plot_type_menu = tk.OptionMenu(selection_frame, plot_type_dropdown, "Line", "Bar", "Scatter")
plot_type_menu.grid(row=0, column=5, padx=5, pady=5)

filter_frame = tk.LabelFrame(root, text="Filter Data", padx=10, pady=10)
filter_frame.pack(fill="x", padx=20, pady=10)
filter_column_label = tk.Label(filter_frame, text="Column:")
filter_column_label.grid(row=0, column=0, padx=5, pady=5)
filter_column_dropdown = tk.StringVar()
filter_column_menu = tk.OptionMenu(filter_frame, filter_column_dropdown, "")
filter_column_menu.grid(row=0, column=1, padx=5, pady=5)

operator_label = tk.Label(filter_frame, text="Operator:")
operator_label.grid(row=0, column=2, padx=5, pady=5)
operator_dropdown = tk.StringVar(value="==")
operator_menu = tk.OptionMenu(filter_frame, operator_dropdown, "==", "!=", ">", "<", ">=", "<=", "contains")
operator_menu.grid(row=0, column=3, padx=5, pady=5)

filter_value_label = tk.Label(filter_frame, text="Value:")
filter_value_label.grid(row=0, column=4, padx=5, pady=5)
filter_value_entry = tk.Entry(filter_frame, width=20)
filter_value_entry.grid(row=0, column=5, padx=5, pady=5)
filter_button = tk.Button(filter_frame, text="Apply Filter", command=filter_data)
filter_button.grid(row=0, column=6, padx=5, pady=5)

reset_button = tk.Button(filter_frame, text="Reset Filter", command=reset_filter)
reset_button.grid(row=0, column=7, padx=5, pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

plot_button = tk.Button(button_frame, text="Generate Plot", command=handle_plot)
plot_button.pack(side="left", padx=5)

save_button = tk.Button(button_frame, text="Save Plot", command=save_plot)
save_button.pack(side="left", padx=5)

plot_frame = tk.Frame(root, bd=1, relief="sunken")
plot_frame.pack(fill="both", expand=True, padx=20, pady=10)

status_label = tk.Label(root, text="Please upload a CSV or Excel file.", anchor="w")
status_label.pack(fill="x", padx=20, pady=5)

root.mainloop()

# Done