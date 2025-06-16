Face Recognition Attendance System
 An AI-powered attendance system that uses facial recognition to automatically mark attendance using Python and machine learning libraries.
📌 Project Overview
  This project automates the attendance-taking process using face recognition technology. The system identifies faces in real-time using a webcam, matches them with pre-       stored images, and logs attendance with the current date and time in a CSV file.
🧰 Tech Stack
 Language: Python
    •Libraries Used:
    •OpenCV – for capturing images and video stream
    •face_recognition – for face encoding and comparison
    •NumPy – numerical operations
    •Pandas – attendance logging in CSV
    •datetime – to log current date and time
🚀 Features
  •Real-time face detection and recognition
  •Attendance logging with name, date, and time
  •Duplicate prevention (one attendance per day)
  •CSV report generation
  •Simple code structure and easy deployment
📂 Project Structure

Face_Recognition_Attendance_System/
├── dataset/              # Registered face images
├── attendance/           # Saved attendance records (CSV)
├── encode_faces.py       # Encodes faces from dataset
├── main.py               # Runs the webcam and attendance logic
├── requirements.txt      # Required Python libraries
├── README.md             # Documentation
└── assets/
    └── output.JPG                                                                                                                                                                                                                                                                                                         
                                                                                                                                        

🛠️ Installation
1. Clone the repository:
git clone https://github.com/YourUsername/Face_Recognition_Attendance_System.git
cd Face_Recognition_Attendance_System
2. Install required libraries:
pip install -r requirements.txt
3. Register Faces:
- Add face images (with names) in the dataset/ folder.
4. Encode Faces:
python encode_faces.py

5. Run Attendance System:
python main.py
📸 Sample Output
Below is the GUI of the system showing all the functional buttons:



 
📈 Future Enhancements
•Add GUI using Tkinter or PyQt
•Multiple face detection for group settings
•Cloud database integration

🙋‍♂️ Author
Anshu Tripathi
MCA Graduate | Python Developer | Machine Learning Enthusiast

