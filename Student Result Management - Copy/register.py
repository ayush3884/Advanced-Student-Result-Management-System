from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import smtplib
import random
import pymysql
import subprocess
import sys
class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # Variables
        self.var_fname = StringVar()
        self.var_otp = StringVar()
        self.otp_verified = False
        self.generated_otp = None

        # =======Background Image=======
        self.bg = ImageTk.PhotoImage(file="images/b2.jpg")
        bg = Label(self.root, image=self.bg).place(x=250, y=0, relwidth=1, relheight=1)

        # =======Left Image=======
        self.left = ImageTk.PhotoImage(file="images/side.png")
        bg = Label(self.root, image=self.left).place(x=80, y=100, width=400, height=500)

        # =======Register Frame=======
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=550)
        title = Label(frame1, text="REGISTER HERE", font=("times new roman", 20, "bold"), bg="white", fg="blue").place(x=50, y=30)

        # First Name
        Label(frame1, text="First Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=100)
        self.txt_fname = Entry(frame1, font=("times new roman", 15), bg="lightgray", textvariable=self.var_fname)
        self.txt_fname.place(x=50, y=130, width=250)

        # Last Name
        Label(frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=100)
        self.txt_lname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_lname.place(x=370, y=130, width=250)

        # Contact
        Label(frame1, text="Contact No.", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=170)
        self.txt_contact = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_contact.place(x=50, y=200, width=250)

        # Email
        Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=170)
        self.txt_email = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=370, y=200, width=250)

        # Send OTP Button
        Button(frame1, text="Send OTP", font=("Arial", 9), bg="sky blue", command=self.send_otp).place(x=625, y=200)

        # Security Question
        Label(frame1, text="Security Question", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=240)
        self.cmb_quest = ttk.Combobox(frame1, font=("times new roman", 13), state='readonly', justify=CENTER)
        self.cmb_quest['values'] = ("Select", "Your First Pet Name", "Your Birth Place", "Your Best Friend Name")
        self.cmb_quest.place(x=50, y=270, width=250)
        self.cmb_quest.current(0)

        # Security Answer
        Label(frame1, text="Answer", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=240)
        self.txt_answer = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_answer.place(x=370, y=270, width=250)

        # Password
        Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=310)
        self.txt_password = Entry(frame1, font=("times new roman", 15), bg="lightgray", show="*")
        self.txt_password.place(x=50, y=340, width=250)

        # Confirm Password
        Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=310)
        self.txt_cpassword = Entry(frame1, font=("times new roman", 15), bg="lightgray", show="*")
        self.txt_cpassword.place(x=370, y=340, width=250)

        # Terms
        self.var_chk = IntVar()
        Checkbutton(frame1, text="I Agree the Terms & Condition", variable=self.var_chk, onvalue=1, offvalue=0,
                    bg="white", font=("times of roman", 12)).place(x=50, y=410)

        # Register Button Image
        self.btn_img = ImageTk.PhotoImage(file="images/register.png")
        Button(frame1, image=self.btn_img, bd=0, cursor="hand2", command=self.register_data).place(x=50, y=450)

        # Sign In Button
        Button(self.root, text="Sign In",command=self.login_window, font=("times new roman", 20), bd=0, cursor="hand2").place(x=200, y=500, width=180)

    # ===== Send OTP =====
    def send_otp(self):
        name = self.txt_fname.get().strip()
        receiver_email = self.txt_email.get().strip()

        if not name or not receiver_email:
            messagebox.showwarning("Input Error", "Please fill in both Name and Email.", parent=self.root)
            return

        self.generated_otp = str(random.randint(100000, 999999))

        sender_email = "vishwakarmaayush3884@gmail.com"
        sender_password = "hrpx saud dlmu jkvl"  # App password from Google

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, sender_password)

            subject = "OTP Verification - Student Result Portal"
            body = f"""Hello {name},

Your OTP is: {self.generated_otp}
Valid for next 5 minutes.

- Student Result System"""
            message = f"Subject: {subject}\n\n{body}"

            server.sendmail(sender_email, receiver_email, message)
            server.quit()

            messagebox.showinfo("Success", "OTP Sent Successfully!", parent=self.root)
            self.open_otp_window()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to send OTP.\n{e}", parent=self.root)

    # ===== Open OTP Window =====
    def open_otp_window(self):
        self.otp_window = Toplevel(self.root)
        self.otp_window.title("OTP Verification")
        self.otp_window.geometry("300x150")
        self.otp_window.resizable(False, False)
        self.otp_window.grab_set()  # Disable main window

        Label(self.otp_window, text="Enter OTP sent to your email", font=("Arial", 10)).pack(pady=10)
        Entry(self.otp_window, font=("Arial", 12), textvariable=self.var_otp).pack(pady=5)
        Button(self.otp_window, text="Verify", command=self.verify_otp_popup, bg="green", fg="white").pack(pady=10)

    # ===== Verify OTP =====
    def verify_otp_popup(self):
        entered_otp = self.var_otp.get().strip()
        if entered_otp == self.generated_otp:
            messagebox.showinfo("Success", "OTP Verified!", parent=self.otp_window)
            self.otp_window.destroy()
            self.otp_verified = True
        else:
            messagebox.showerror("Error", "Incorrect OTP", parent=self.otp_window)

    def login_window(self):
        self.root.destroy()
        subprocess.Popen([sys.executable, "login.py"])




    ##==========Clear========
    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.cmb_quest.current(0)

    # ===== Final Registration Validation =====
    def register_data(self):
        if self.var_fname.get() == "" or self.txt_contact.get() == "" or self.txt_email.get() == "" or \
           self.cmb_quest.get() == "Select" or self.txt_answer.get() == "" or \
           self.txt_password.get() == "" or self.txt_cpassword.get() == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        elif self.txt_password.get() != self.txt_cpassword.get():
            messagebox.showerror("Error", "Password & Confirm Password should be same", parent=self.root)
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error", "Please Agree to our Terms & Conditions", parent=self.root)
        elif not self.otp_verified:
            messagebox.showerror("Error", "Please verify your OTP first", parent=self.root)
        else:
            try:
                # Use the same connection settings (including port) as the login flow.
                con=pymysql.connect(host="localhost", user="root", password="", database="Employee", port=3307)
                cur=con.cursor()
                cur.execute("select * from employee1 where email=%s",self.txt_email.get())
                row=cur.fetchone()
                print(row)
                if row!=None:
                    messagebox.showerror("Error","User already Exist, Please try with another email",parent=self.root)
                else:
                    cur.execute("insert into employee1 (f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                                    (
                                        self.txt_fname.get(),
                                        self.txt_lname.get(),
                                        self.txt_contact.get(),
                                        self.txt_email.get(),
                                        self.cmb_quest.get(),
                                        self.txt_answer.get(),
                                        self.txt_password.get()
                                    ) )
                con.commit()
                con.close()
                self.clear()
                messagebox.showinfo("Success", "Registered Successfully", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Error due to{str(es)}",parent=self.root)
           

# ==== Run App ====
if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()
