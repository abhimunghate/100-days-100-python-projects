# This is Day 64 project : PDF Merger Tool

import tkinter as tk
from gui import PDFMergerGUI

def main():
    root = tk.Tk()
    app = PDFMergerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    
# Done