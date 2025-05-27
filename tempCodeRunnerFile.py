import sqlite3 as sql
import win32com.client as win32
import os
from datetime import datetime

# Define file path
excel_file_path = os.path.join(os.getcwd(), 'Attendance_Files', f'Attendance{str(datetime.now().date())}.xlsx')

# Remove existing file if needed
if os.path.exists(excel_file_path):
    os.remove(excel_file_path)

# Connect to database
conn = sql.connect('database/database.db')
c = conn.cursor()

# Create instance of Excel
excelApp = win32.gencache.EnsureDispatch("Excel.Application")

# Create folder if not exists
if not os.path.exists('Attendance_Files'):
    os.makedirs("Attendance_Files")

# Create or open Excel workbook
ExcelWrkbook = excelApp.Workbooks.Add()
ExcelWrkbook.SaveAs(excel_file_path)

# Get the worksheet
Excelwrksheet = ExcelWrkbook.ActiveSheet

# Set Excel header
ExcelHeaderRange = Excelwrksheet.Range(Excelwrksheet.Cells(1, 1), Excelwrksheet.Cells(1, 3))
ExcelHeaderRange.Value = ('UID', 'Name', 'Attendance')

# Fetch student data
def get_data():
    c.execute("SELECT * FROM students ORDER BY student_name")
    return c.fetchall()

students = get_data()

# Write data to Excel
RowLength = len(students[0])
ColLength = len(students)
ExcelRange = Excelwrksheet.Range(Excelwrksheet.Cells(2, 1), Excelwrksheet.Cells(1 + ColLength, RowLength))
ExcelRange.Value = students

# Save and close Excel
ExcelWrkbook.Close(True)

# ✅ DO NOT RESET ATTENDANCE HERE ❌
# If you want to reset it later, do it in a separate script safely

# Launch next GUI if needed
os.system("python message_gui.py")

# Close DB connection
conn.close()
