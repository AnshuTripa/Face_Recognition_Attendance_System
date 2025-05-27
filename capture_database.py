# === capture_database.py ===
import cv2
import sqlite3
import os
from tkinter import *
from tkinter import messagebox

# === Check if cv2.face module is available ===
try:
    recognizer = cv2.face.LBPHFaceRecognizer_create()
except AttributeError:
    raise ImportError("❌ 'cv2.face' not found. Install it with:\n\npip install opencv-contrib-python")

# === Function to create DB and table if not exist ===
def setup_database():
    if not os.path.exists("database"):
        os.makedirs("database")
    conn = sqlite3.connect('database/database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS students (
            UID TEXT PRIMARY KEY,
            student_name TEXT,
            attendance TEXT
        )
    ''')
    conn.commit()
    return conn, c

# === GUI to get user input ===
def get_user_input():
    def submit_action():
        if uid_val.get() and name_val.get():
            val1.set(uid_val.get())
            val2.set(name_val.get())
            root.destroy()
        else:
            messagebox.showerror("Input Error", "Please fill both fields!")

    root = Tk()
    root.title("Register New Face")
    root.geometry("400x200")

    val1 = StringVar()
    val2 = StringVar()

    Label(root, text="Enter Unique ID:", font=('Arial', 12)).grid(row=0, column=0, padx=10, pady=10, sticky=W)
    uid_val = Entry(root, width=30)
    uid_val.grid(row=0, column=1)

    Label(root, text="Enter Full Name:", font=('Arial', 12)).grid(row=1, column=0, padx=10, pady=10, sticky=W)
    name_val = Entry(root, width=30)
    name_val.grid(row=1, column=1)

    Button(root, text="Submit", command=submit_action, bg="green", fg="white").grid(row=3, columnspan=2, pady=20)
    root.mainloop()

    return val1.get(), val2.get()

# === Ensure dataset folder exists ===
def assure_path_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

# === Main Function ===
def main():
    conn, c = setup_database()
    face_id, name = get_user_input()

    if not face_id or not name:
        print("[ERROR] Missing ID or Name.")
        return

    try:
        c.execute("INSERT OR IGNORE INTO students(UID, student_name, attendance) VALUES (?, ?, ?)",
                  (face_id, name, 'Absent'))
        conn.commit()
    except Exception as e:
        print("[ERROR] Database error:", e)
        return

    print(f"[INFO] Starting face capture for {name} (ID: {face_id})...")
    cam = cv2.VideoCapture(0)
    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    count = 0
    assure_path_exists("dataset")

    while True:
        ret, img = cam.read()
        if not ret:
            print("[ERROR] Webcam not available.")
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            count += 1
            face_img = gray[y:y + h, x:x + w]
            cv2.imwrite(f"dataset/User.{face_id}.{count}.jpg", face_img)
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.imshow('Capturing Face', img)

        if count >= 30:
            print("[INFO] Face capture complete.")
            break
        if cv2.waitKey(100) & 0xFF == ord('q'):
            print("[INFO] Capture interrupted.")
            break

    cam.release()
    cv2.destroyAllWindows()
    conn.close()

    # Optional success message
    print(f"[SUCCESS] Face data for {name} stored.")

# === Run ===
if __name__ == "__main__":
    main()
