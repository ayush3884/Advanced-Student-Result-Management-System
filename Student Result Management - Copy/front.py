import tkinter as tk
from PIL import Image, ImageTk
import os

# ----------- Functions -----------
def open_student_section():
    os.system("python report.py")  # Student section file open karega

def open_teacher_section():
    os.system("python register.py")  # Teacher section file open karega

# ----------- Main Window -----------
root = tk.Tk()
root.title("Student Result Management System")
root.geometry("600x400")
root.config(bg="#f0f0f0")

# ----------- Title -----------
title_label = tk.Label(root, text="Student Result Management System",
                       font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=10)

# ----------- Image Placeholder -----------
try:
    img = Image.open("images/aa.jpg")  # Apni image ka path yaha do
    img = img.resize((150, 150))
    photo = ImageTk.PhotoImage(img)
    img_label = tk.Label(root, image=photo, bg="#f0f0f0")
    img_label.image = photo
    img_label.pack(pady=5)
except:
    img_label = tk.Label(root, text="[Image Placeholder]", font=("Arial", 12, "italic"), 
                         bg="#f0f0f0", fg="gray")
    img_label.pack(pady=5)

# ----------- Question Label -----------
question_label = tk.Label(root, text="Are you a Student or Teacher?",
                          font=("Arial", 14), bg="#f0f0f0", fg="#333")
question_label.pack(pady=15)

# ----------- Buttons -----------
btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack()

student_btn = tk.Button(btn_frame, text="Student", font=("Arial", 12, "bold"),
                         bg="#4CAF50", fg="white", width=12, command=open_student_section)
student_btn.grid(row=0, column=0, padx=20, pady=10)

teacher_btn = tk.Button(btn_frame, text="Teacher", font=("Arial", 12, "bold"),
                         bg="#2196F3", fg="white", width=12, command=open_teacher_section)
teacher_btn.grid(row=0, column=1, padx=20, pady=10)

# ----------- Run Window -----------
root.mainloop()
