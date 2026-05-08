from tkinter import *
from PIL import Image, ImageTk  # Make sure pillow is installed: pip install pillow
from datetime import datetime
from course import CourseClass
from student import StudentClass
from result import resultClass
from report import reportClass

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1366x768+0+0")
        self.root.config(bg="white")

        # ======= Icons ======
        self.logo_dash = ImageTk.PhotoImage(file="images/logo_p.png")  # Make sure this path is correct

        # ======= Title ======
        title = Label(
            self.root,
            text="Student Result Management System",
            padx=10,
            compound=LEFT,
            image=self.logo_dash,
            font=("goudy old style", 20, "bold"),
            bg="#033054",
            fg="white"
        ).place(x=0, y=0, relwidth=1, height=50)
        #===========Title========
        #=========Menus======
        M_frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white",)
        M_frame.place(x=10,y=70,width=1350,height=76)
        #==========Menus=====
        #========Button======
        btn_course=Button(M_frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)
        btn_student=Button(M_frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=240,y=5,width=200,height=40)
        btn_result=Button(M_frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=460,y=5,width=200,height=40)
        btn_view_student_result=Button(M_frame,text="View Student Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=680,y=5,width=200,height=40)
        btn_logout=Button(M_frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=900,y=5,width=200,height=40)
        btn_exit=Button(M_frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=1120,y=5,width=200,height=40)
        #======Button========

        #===========Content Window
        
        self.bg_image=Image.open("images/bg.png")
        self.bg_image=self.bg_image.resize((920,350),Image.Resampling.LANCZOS)
        self.bg_image=ImageTk.PhotoImage(self.bg_image)
        self.lbl_bg=Label(self.root,image=self.bg_image).place( x=400,y=180,width=920,height=350)

        #=========Update details
        self.lbl_students=Label(self.root,text="Total Students\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_students.place(x=400,y=530,width=300,height=100)


        self.lbl_course=Label(self.root,text="Total Course\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
        self.lbl_course.place(x=710,y=530,width=300,height=100)


        self.lbl_results=Label(self.root,text="Total Results\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white")
        self.lbl_results.place(x=1020,y=530,width=300,height=100)


        # ======= Clock Section =======
        self.clock_frame = Frame(self.root, bg="#041d33", bd=0, relief=RIDGE)
        self.clock_frame.place(x=20, y=200, width=340, height=180)

        Label(
            self.clock_frame,
            text="Digital Clock",
            font=("goudy old style", 18, "bold"),
            bg="#041d33",
            fg="#7bdff2"
        ).pack(pady=(15, 5))

        self.lbl_clock_time = Label(
            self.clock_frame,
            text="--:--:--",
            font=("goudy old style", 34, "bold"),
            bg="#041d33",
            fg="#f6f7f8"
        )
        self.lbl_clock_time.pack()

        self.lbl_clock_date = Label(
            self.clock_frame,
            text="",
            font=("goudy old style", 16),
            bg="#041d33",
            fg="#ced4da"
        )
        self.lbl_clock_date.pack(pady=(5, 15))

        self.update_clock()

        #========Footer=======
        title = Label(
            self.root,
            text="SRMS-Student Result Management System | Developed by Ayush Vishwakarma\nContact us for any Technical Issue: 8960819513",
            padx=10,
            font=("goudy old style", 15),
            bg="#262626",
            fg="white"
        ).pack(side=BOTTOM,fill=X)


    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)    
    
    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=StudentClass(self.new_win)  

    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)   

    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)   

    def update_clock(self):
        now = datetime.now()
        self.lbl_clock_time.config(text=now.strftime("%I:%M:%S %p"))
        self.lbl_clock_date.config(text=now.strftime("%A, %d %B %Y"))
        self.root.after(1000, self.update_clock)


if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
