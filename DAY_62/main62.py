# This is Day 62 project : Automated Backup Tool

import tkinter as tk

from gui import BackupToolGUI

def main():
    root = tk.Tk()
    app = BackupToolGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    
# Done