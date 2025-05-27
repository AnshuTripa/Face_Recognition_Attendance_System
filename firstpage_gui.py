from tkinter import *
from datetime import datetime
from PIL import Image, ImageTk
import os

# Create the main tkinter window
root = Tk()
root.title("AUTOMATIC ATTENDANCE MANAGEMENT USING FACE RECOGNITION")
root.geometry("900x600")
root.resizable(False, False)

# Load background image
bg_image = Image.open("logo.jpg")
bg_image = bg_image.resize((900, 600), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Background label
bg_label = Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Main Frame
main_frame = Frame(root, bg="ivory4")
main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Title label
title_label = Label(main_frame, text="FACE RECOGNITION ATTENDANCE SYSTEM",
                    font=("times new roman", 20), bg="red4", fg="white", height=2)
title_label.grid(row=0, columnspan=2, padx=5, pady=5, sticky="ew")

# Load and place logo image
logo_image = Image.open("logo.jpg")
logo_image = logo_image.resize((150, 100), Image.Resampling.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)

logo_label = Label(main_frame, image=logo_photo, bg="ivory4")
logo_label.grid(row=1, columnspan=2, pady=5)

# Define functions
def c_dataset():
    os.system("python capture_database.py")

def write_e():
    os.system("python writing_in_excel.py")

def train_d():
    os.system("python training_dataset.py")

def m_attendance():
    os.system("python recognizer.py")

def v_attendance():
    os.startfile(os.getcwd()+"/Attendance_Files/attendance"+str(datetime.now().date())+'.xlsx')

def d_dataset():
    os.system("python delete_database.py")

def destroy():
    root.destroy()

# Buttons
Button(main_frame, text="Create Dataset", font=("times new roman", 16), bg="dodgerblue2", fg='white',
       command=c_dataset).grid(row=2, column=0, padx=10, pady=10, sticky="ew")

Button(main_frame, text="Write in Excel", font=("times new roman", 16), bg="dodgerblue2", fg='white',
       command=write_e).grid(row=2, column=1, padx=10, pady=10, sticky="ew")

Button(main_frame, text="Train Dataset", font=("times new roman", 16), bg="dodgerblue3", fg='white',
       command=train_d).grid(row=3, column=0, padx=10, pady=10, sticky="ew")

Button(main_frame, text="Mark Attendance", font=("times new roman", 16), bg="dodgerblue3", fg='white',
       command=m_attendance).grid(row=3, column=1, padx=10, pady=10, sticky="ew")

Button(main_frame, text="View Attendance Sheet", font=("times new roman", 16), bg="dodgerblue4", fg='white',
       command=v_attendance).grid(row=4, column=0, padx=10, pady=10, sticky="ew")

Button(main_frame, text="Delete Dataset", font=("times new roman", 16), bg="dodgerblue4", fg='white',
       command=d_dataset).grid(row=4, column=1, padx=10, pady=10, sticky="ew")

Button(main_frame, text="Exit", font=('times new roman', 16), bg="red4", fg="white",
       command=destroy).grid(row=5, columnspan=2, padx=10, pady=10, sticky="ew")

# Start the GUI loop
root.mainloop()
