from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from datetime import*
import time
from math import*
import pymysql
from tkinter import messagebox,ttk
import subprocess
import sys

class Clock:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")
        # title = Label(self.root, text='Welcome Digital Clock',font=("times new roman", 50, "bold"), bg="#46B1BB", fg="white")
        # title.place(x=0, y=50, relwidth=1)

        ##=====Background Color========
        left_lbl=Label(self.root,bg="#08A3D2",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)

        right_lbl=Label(self.root,bg="#031F36",bd=0)
        right_lbl.place(x=600,y=0,relheight=1,relwidth=1)
        #======Frame=======
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=250,y=100,width=800,height=500)

        title=Label(login_frame,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="white",fg="#08A3D2").place(x=250,y=50)
        email=Label(login_frame,text="EMAIL ADDRESS",font=("times new roman",15,"bold"),bg="white",fg="GRAY").place(x=250,y=150)
        self.txt_email=Entry(login_frame,font=("times new roman",15,"bold"),bg="lightgray")
        self.txt_email.place(x=250,y=180,width=350,height=35)
        pass_=Label(login_frame,text="PASSWORD",font=("times new roman",15,"bold"),bg="white",fg="GRAY").place(x=250,y=250)
        self.txt_pass_=Entry(login_frame,font=("times new roman",15,"bold"),bg="lightgray")
        self.txt_pass_.place(x=250,y=280,width=350,height=35)

        btn_reg=Button(login_frame,text="Register new account ?",command=self.register_window,font=("times new roman",14),bg="white",bd=0,fg="#B00867").place(x=250,y=320)
        btn_forget=Button(login_frame,text="Forget Password ?",command=self.forget_password_window,font=("times new roman",14),bg="white",bd=0,fg="red").place(x=450,y=320)
        btn_login=Button(login_frame,text="Login",font=("times new roman",20,"bold"),command=self.login,fg="white",bd=0,bg="#B00857",cursor="hand2").place(x=250,y=380,width=180,height=40)

        
        #=========Clock=========
        self.lbl = Label(self.root,text="\nDigital Clock",font=("Book Antique",25,"bold"),fg="white",compound=BOTTOM,bg="#081923",bd=0)
        self.lbl.place(x=90, y=120, height=450, width=350)
        self.working()

    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_pass.set("")
        self.txt_answer.set("")
        self.txt_pass_.set("")
        self.txt_email.set("")

        # self.clock_image()
    def forget_password(self):
        if self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_new_pass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root2)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee")
                cur=con.cursor()
                cur.execute("Select * from employee1 where email=%s and question=%s and answer=%s",(self.txt_email.get(),self.cmb_quest.get(),self.txt_answer.get()))
                row=cur.fetchone()
                if row==None:
                   messagebox.showerror("Error","Please Select the Correct Security Question / Enter Answer",parent=self.root2)
                else:
                    cur.execute("update employee1 set password=%s where email=%s",(self.txt_new_pass.get(),self.txt_email.get()))
                    con.commit()
                    con.close()
                    self.reset()
                    messagebox.showinfo("Success","Your Password has been reset, Please login with new password",parent=self.root2)

            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)



    def forget_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset your password",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee")
                cur=con.cursor()
                cur.execute("Select * from employee1 where email=%s",self.txt_email.get())
                row=cur.fetchone()
                if row==None:
                   messagebox.showerror("Error","Please enter the valid email address to reset your password",parent=self.root)
                else:
                    con.close()
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("350x400+495+150")
                    self.root2.config(bg='white')
                    self.root2.focus_force()
                    self.root2.grab_set()
                    t=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=0,y=10,relwidth=1)
                    # -------Forget Password
                    Label(self.root2, text="Security Question", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=100)
                    self.cmb_quest = ttk.Combobox(self.root2, font=("times new roman", 13), state='readonly', justify=CENTER)
                    self.cmb_quest['values'] = ("Select", "Your First Pet Name", "Your Birth Place", "Your Best Friend Name")
                    self.cmb_quest.place(x=50, y=130, width=250)
                    self.cmb_quest.current(0)

                    # Security Answer
                    Label(self.root2, text="Answer", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=180)
                    self.txt_answer = Entry(self.root2, font=("times new roman", 15), bg="lightgray")
                    self.txt_answer.place(x=50, y=210, width=250)
                    # New Password
                    Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=260)
                    self.txt_new_pass = Entry(self.root2, font=("times new roman", 15), bg="lightgray")
                    self.txt_new_pass.place(x=50, y=290, width=250)

                    btn_change_password=Button(self.root2,text="Reset Password",command=self.forget_password,bg="green",fg="white",font=("timew new roman",15,"bold")).place(x=90,y=340)
                   
               
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

    
    def register_window(self):
        self.root.destroy()
        subprocess.Popen([sys.executable, "register.py"])

    def login(self):
        if self.txt_email.get() == "" or self.txt_pass_.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="employee",port=3307)
                cur = con.cursor()
                cur.execute(
                    "SELECT * FROM employee1 WHERE email=%s AND password=%s",
                    (self.txt_email.get(), self.txt_pass_.get())
                )
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid USERNAME & PASSWORD", parent=self.root)
                else:
                    messagebox.showinfo("Success", "Welcome", parent=self.root)
                    self.root.destroy()
                    subprocess.Popen([sys.executable, "dashboard.py"])
                con.close()

            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)

    def clock_image(self,hr,min_,sec_):
        # Create a blank white image
        clock = Image.new("RGB", (400, 400), (8,25,35))
        draw = ImageDraw.Draw(clock)
        ##==========For Clock Image
        # Load and paste background image
        bg = Image.open("images/c.png")
        bg = bg.resize((300, 300), Image.Resampling.LANCZOS)
        clock.paste(bg, (50, 50))
        # Formula to rotate the clock
        # anagle_in_radians=angle_in_degree * math.pi/180
        # line.length=100
        # center_x=250
        # center_y=250
        # end_x=center_x+line_length * math.cos(angle_in_radians)
        # end_y=center_y-line_length * math.sin(angle_in_radians)

        # Save and display image
        
        #========Hours Line image=====
        origin=200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="#DF005E",width=4)
        #========min Line image=====
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="blue",width=3)
        #========second Line image=====
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="yellow",width=2)
        draw.ellipse((195,195,210,210),fill="#1Ad5D5")
        clock.save("clock_new.png")

        self.img = ImageTk.PhotoImage(clock)
        self.lbl.config(image=self.img)

    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second
        # print(h,m,s)
        # print(hr,min_,sec_)
        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360
        self.clock_image(hr,min_,sec_)
        self.img=ImageTk.PhotoImage(file="clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)
root = Tk()
obj = Clock(root)
root.mainloop()
