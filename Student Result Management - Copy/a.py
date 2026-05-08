from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import smtplib, random, pymysql

class RegisterScreen(Screen):
    def __init__(self, **kwargs):
        super(RegisterScreen, self).__init__(**kwargs)
        self.generated_otp = ""
        self.otp_verified = False

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.fname = TextInput(hint_text="First Name")
        self.email = TextInput(hint_text="Email")
        self.password = TextInput(hint_text="Password", password=True)
        self.cpassword = TextInput(hint_text="Confirm Password", password=True)

        send_otp_btn = Button(text="Send OTP", on_press=self.send_otp)
        register_btn = Button(text="Register", on_press=self.register_user)

        layout.add_widget(self.fname)
        layout.add_widget(self.email)
        layout.add_widget(self.password)
        layout.add_widget(self.cpassword)
        layout.add_widget(send_otp_btn)
        layout.add_widget(register_btn)

        self.add_widget(layout)

    def send_otp(self, instance):
        if self.fname.text == "" or self.email.text == "":
            self.show_popup("Error", "Please enter Name and Email")
            return

        self.generated_otp = str(random.randint(100000, 999999))
        try:
            sender = "your-email@gmail.com"
            password = "your-app-password"
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender, password)
            message = f"Subject: OTP Verification\n\nYour OTP is: {self.generated_otp}"
            server.sendmail(sender, self.email.text, message)
            server.quit()

            self.show_otp_popup()

        except Exception as e:
            self.show_popup("Email Error", str(e))

    def show_otp_popup(self):
        box = BoxLayout(orientation='vertical', padding=10, spacing=10)
        otp_input = TextInput(hint_text="Enter OTP", multiline=False)
        verify_btn = Button(text="Verify OTP")

        def verify(instance):
            if otp_input.text == self.generated_otp:
                self.otp_verified = True
                popup.dismiss()
                self.show_popup("Success", "OTP Verified")
            else:
                self.show_popup("Error", "Invalid OTP")

        box.add_widget(Label(text="Enter the OTP sent to your email"))
        box.add_widget(otp_input)
        box.add_widget(verify_btn)
        verify_btn.bind(on_press=verify)

        popup = Popup(title="OTP Verification", content=box, size_hint=(None, None), size=(300, 200))
        popup.open()

    def register_user(self, instance):
        if not self.otp_verified:
            self.show_popup("Error", "Please verify OTP first")
            return
        if self.password.text != self.cpassword.text:
            self.show_popup("Error", "Passwords do not match")
            return

        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="employee")
            cur = con.cursor()
            cur.execute("SELECT * FROM employee1 WHERE email=%s", (self.email.text,))
            if cur.fetchone():
                self.show_popup("Error", "User already exists")
            else:
                cur.execute("INSERT INTO employee1 (f_name, email, password) VALUES (%s, %s, %s)",
                            (self.fname.text, self.email.text, self.password.text))
                con.commit()
                self.show_popup("Success", "Registered Successfully")
            con.close()
        except Exception as e:
            self.show_popup("DB Error", str(e))

    def show_popup(self, title, message):
        popup = Popup(title=title,
                      content=Label(text=message),
                      size_hint=(None, None), size=(300, 150))
        popup.open()

class RegisterApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(RegisterScreen(name="register"))
        return sm

if __name__ == "__main__":
    RegisterApp().run()
