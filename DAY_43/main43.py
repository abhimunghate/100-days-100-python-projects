# This is Day 43 project : Matrix Calculator

import json
import numpy as np
import tkinter as tk
from tkinter import messagebox, filedialog

def matrix_addition(A, B):
    if A.shape != B.shape:
        raise ValueError("Matrices must have the same dimensions.")
    return A + B

def matrix_subtraction(A, B):
    if A.shape != B.shape:
        raise ValueError("Matrices must have the same dimensions.")
    return A - B

def matrix_multiplication(A, B):
    if A.shape != B.shape:
        raise ValueError("Matrices must have the same dimensions for element-wise multiplication.")
    return A * B

def matrix_dot_product(A, B):
    if A.shape[1] != B.shape[0]:
        raise ValueError("Number of columns in Matrix A must equal number of rows in Matrix B.")
    return np.dot(A, B)

def matrix_determinant(A):
    if A.shape[0] != A.shape[1]:
        raise ValueError("Determinant requires a square matrix.")
    return np.linalg.det(A)

def matrix_inverse(A):
    if A.shape[0] != A.shape[1]:
        raise ValueError("Inverse requires a square matrix.")
    return np.linalg.inv(A)

def scalar_multiply(A, scalar):
    return A * scalar

def scalar_add(A, scalar):
    return A + scalar

def scalar_subtract(A, scalar):
    return A - scalar

def scalar_divide(A, scalar):
    if scalar == 0:
        raise ValueError("Cannot divide by zero.")
    return A / scalar

def vector_addition(A, B):
    return np.add(A, B)

def vector_subtraction(A, B):
    return np.subtract(A, B)

def vector_dot_product(A, B):
    return np.dot(A, B)

def vector_cross_product(A, B):
    if len(A) != 3 or len(B) != 3:
        raise ValueError("Cross product is supported only for 3D vectors.")
    return np.cross(A, B)

def vector_magnitude(A):
    return np.linalg.norm(A)

def save_matrix(matrix, filename):
    data = {
        "rows": matrix.shape[0],
        "columns": matrix.shape[1],
        "data": matrix.tolist()
    }

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def load_matrix(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
    matrix = np.array(data["data"], dtype=float)
    return matrix

def text_to_matrix(text):
    try:
        rows = text.strip().split("\n")
        matrix = []

        for row in rows:
            values = list(map(float, row.split()))
            matrix.append(values)
        if not matrix:
            raise ValueError("Matrix cannot be empty.")
        column_count = len(matrix[0])

        for row in matrix:
            if len(row) != column_count:
                raise ValueError("All rows must have the same number of columns.")
        return np.array(matrix)

    except ValueError:
        raise ValueError("Enter valid numbers separated by spaces.")

def matrix_to_text(matrix):
    return "\n".join(" ".join(f"{value:g}" for value in row)
        for row in matrix)

class MatrixCalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Matrix Calculator")
        self.root.geometry("850x650")
        self.matrix_a = None
        self.matrix_b = None

        title = tk.Label(root, text="Matrix Calculator", font=("Arial", 22, "bold"))
        title.pack(pady=10)

        input_frame = tk.Frame(root)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Matrix A", font=("Arial", 12, "bold")).grid(row=0, column=0)
        self.matrix_a_text = tk.Text(input_frame, width=30, height=8)
        self.matrix_a_text.grid(row=1, column=0, padx=10)

        tk.Label(input_frame, text="Matrix B", font=("Arial", 12, "bold")).grid(row=0, column=1)
        self.matrix_b_text = tk.Text(input_frame, width=30, height=8)
        self.matrix_b_text.grid(row=1, column=1, padx=10)

        scalar_frame = tk.Frame(root)
        scalar_frame.pack(pady=5)
        tk.Label(scalar_frame, text="Scalar:").pack(side=tk.LEFT)
        self.scalar_entry = tk.Entry(scalar_frame, width=10)
        self.scalar_entry.pack(side=tk.LEFT, padx=5)

        operation_frame = tk.Frame(root)
        operation_frame.pack(pady=10)
        buttons = [
            ("A + B", self.add_matrices),
            ("A - B", self.subtract_matrices),
            ("A ⊙ B", self.multiply_matrices),
            ("A · B", self.dot_matrices),
            ("Transpose A", self.transpose_a),
            ("Transpose B", self.transpose_b),
            ("Determinant A", self.determinant_a),
            ("Determinant B", self.determinant_b),
            ("Inverse A", self.inverse_a),
            ("Inverse B", self.inverse_b),
        ]

        for index, (text, command) in enumerate(buttons):
            row = index // 5
            column = index % 5
            tk.Button(operation_frame, text=text, command=command, width=14).grid(row=row, column=column, padx=3, pady=3)

        scalar_operation_frame = tk.Frame(root)
        scalar_operation_frame.pack(pady=5)
        tk.Label(scalar_operation_frame, text="Scalar Operations:", font=("Arial", 10, "bold")).pack(side=tk.LEFT)
        tk.Button(scalar_operation_frame, text="Multiply", command=self.scalar_multiply_operation).pack(side=tk.LEFT, padx=3)
        tk.Button(scalar_operation_frame, text="Add", command=self.scalar_add_operation).pack(side=tk.LEFT, padx=3)
        tk.Button(scalar_operation_frame, text="Subtract", command=self.scalar_subtract_operation).pack(side=tk.LEFT, padx=3)
        tk.Button(scalar_operation_frame, text="Divide", command=self.scalar_divide_operation).pack(side=tk.LEFT, padx=3)

        vector_frame = tk.Frame(root)
        vector_frame.pack(pady=5)
        tk.Label(vector_frame, text="Vector Operations:", font=("Arial", 10, "bold")).pack(side=tk.LEFT)
        tk.Button(vector_frame, text="Vector Add", command=self.vector_add).pack(side=tk.LEFT, padx=3)
        tk.Button(vector_frame, text="Vector Subtract", command=self.vector_subtract).pack(side=tk.LEFT, padx=3)
        tk.Button(vector_frame, text="Dot Product", command=self.vector_dot).pack(side=tk.LEFT, padx=3)
        tk.Button(vector_frame, text="Cross Product", command=self.vector_cross).pack(side=tk.LEFT, padx=3)
        tk.Button(vector_frame, text="Magnitude A", command=self.vector_magnitude_a).pack(side=tk.LEFT, padx=3)

        file_frame = tk.Frame(root)
        file_frame.pack(pady=10)
        tk.Button(file_frame, text="Save Matrix A", command=self.save_a).pack(side=tk.LEFT, padx=5)
        tk.Button(file_frame, text="Load Matrix A", command=self.load_a).pack(side=tk.LEFT, padx=5)
        tk.Button(file_frame, text="Save Matrix B", command=self.save_b).pack(side=tk.LEFT, padx=5)
        tk.Button(file_frame, text="Load Matrix B", command=self.load_b).pack(side=tk.LEFT, padx=5)

        tk.Label(root, text="Result", font=("Arial", 12, "bold")).pack()
        self.result_text = tk.Text(root, width=90, height=10)
        self.result_text.pack(padx=10, pady=5)

    def get_matrices(self):
        A = text_to_matrix(self.matrix_a_text.get("1.0", tk.END))
        B = text_to_matrix(self.matrix_b_text.get("1.0", tk.END))
        self.matrix_a = A
        self.matrix_b = B
        return A, B

    def display_result(self, result):
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, str(result))

    def add_matrices(self):
        try:
            A, B = self.get_matrices()
            result = matrix_addition(A, B)
            self.display_result(result)
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def subtract_matrices(self):
        try:
            A, B = self.get_matrices()
            result = matrix_subtraction(A, B)
            self.display_result(result)
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def multiply_matrices(self):
        try:
            A, B = self.get_matrices()
            result = matrix_multiplication(A, B)
            self.display_result(result)
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def dot_matrices(self):
        try:
            A, B = self.get_matrices()
            result = matrix_dot_product(A, B)
            self.display_result(result)
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def transpose_a(self):
        try:
            A, _ = self.get_matrices()
            self.display_result(A.T)
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def transpose_b(self):
        try:
            _, B = self.get_matrices()
            self.display_result(B.T)
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def determinant_a(self):
        try:
            A, _ = self.get_matrices()
            result = matrix_determinant(A)
            self.display_result(result)
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def determinant_b(self):
        try:
            _, B = self.get_matrices()
            result = matrix_determinant(B)
            self.display_result(result)
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def inverse_a(self):
        try:
            A, _ = self.get_matrices()
            result = matrix_inverse(A)
            self.display_result(result)
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def inverse_b(self):
        try:
            _, B = self.get_matrices()
            result = matrix_inverse(B)
            self.display_result(result)
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def get_scalar(self):
        try:
            return float(self.scalar_entry.get())
        except ValueError:
            raise ValueError("Enter a valid scalar.")

    def scalar_multiply_operation(self):
        try:
            A, _ = self.get_matrices()
            scalar = self.get_scalar()
            self.display_result(scalar_multiply(A, scalar))
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def scalar_add_operation(self):
        try:
            A, _ = self.get_matrices()
            scalar = self.get_scalar()
            self.display_result(scalar_add(A, scalar))
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def scalar_subtract_operation(self):
        try:
            A, _ = self.get_matrices()
            scalar = self.get_scalar()
            self.display_result(scalar_subtract(A, scalar))
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def scalar_divide_operation(self):
        try:
            A, _ = self.get_matrices()
            scalar = self.get_scalar()
            self.display_result(scalar_divide(A, scalar))
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def get_vectors(self):
        A, B = self.get_matrices()
        if not (A.shape[0] == 1 or A.shape[1] == 1):
            raise ValueError("Matrix A must be a row or column vector.")
        if not (B.shape[0] == 1 or B.shape[1] == 1):
            raise ValueError("Matrix B must be a row or column vector.")
        A = A.flatten()
        B = B.flatten()
        if len(A) != len(B):
            raise ValueError("Vectors must have the same dimensions.")
        return A, B

    def vector_add(self):
        try:
            A, B = self.get_vectors()
            self.display_result(vector_addition(A, B))
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def vector_subtract(self):
        try:
            A, B = self.get_vectors()
            self.display_result(vector_subtraction(A, B))
        except Exception as error:
            messagebox.showerror("Error", str(error))
    def vector_dot(self):
        try:
            A, B = self.get_vectors()
            self.display_result(vector_dot_product(A, B))
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def vector_cross(self):
        try:
            A, B = self.get_vectors()
            self.display_result(vector_cross_product(A, B))
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def vector_magnitude_a(self):
        try:
            A, _ = self.get_vectors()
            self.display_result(vector_magnitude(A))
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def save_a(self):
        try:
            A, _ = self.get_matrices()
            filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
            if filename:
                save_matrix(A, filename)
                messagebox.showinfo("Success", "Matrix A saved successfully.")
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def save_b(self):
        try:
            _, B = self.get_matrices()
            filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
            if filename:
                save_matrix(B, filename)
                messagebox.showinfo("Success", "Matrix B saved successfully.")
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def load_a(self):
        try:
            filename = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
            if filename:
                matrix = load_matrix(filename)
                self.matrix_a_text.delete("1.0", tk.END)
                self.matrix_a_text.insert(tk.END, matrix_to_text(matrix))
                messagebox.showinfo("Success", "Matrix A loaded successfully.")
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def load_b(self):
        try:
            filename = filedialog.askopenfilename(
                filetypes=[("JSON files", "*.json")])
            if filename:
                matrix = load_matrix(filename)
                self.matrix_b_text.delete("1.0", tk.END)
                self.matrix_b_text.insert(tk.END, matrix_to_text(matrix))
                messagebox.showinfo("Success", "Matrix B loaded successfully.")
        except Exception as error:
            messagebox.showerror("Error", str(error))
    
if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixCalculatorGUI(root)
    root.mainloop()
    
# Done