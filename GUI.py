import tkinter as tk
from authentication import load_file, authenticate_user, speak_message
from voice_control import voice_command


def submit_action():
    username = entry_username.get()
    password = entry_password.get()
    message = authenticate_user(username, password, history)
    label_message.config(text=message)
    speak_message(message)
    name = username

    if "Hello" in message or f"New user added, welcome !!! {name}" in message:
        open_voice_command_window()


def open_voice_command_window():
    voice_command_window = tk.Toplevel(root)
    voice_command_window.title("Voice Command Control")
    voice_command_window.geometry("600x400")  # Larger window

    vc_button = tk.Button(
        voice_command_window, text="Start Voice Command",
        command=voice_command, font=font_large
    )
    vc_button.pack(pady=pad_large)


history = load_file()

# GUI Setup for Authentication
root = tk.Tk()
root.title("User Authentication")
root.geometry("400x300")

# Style Configuration
font_large = ('Arial', 12)
pad_large = 10

# sign up text
text_content = "To signup as a new user \n just type in your username and password"
text_widget = tk.Text(root, wrap=tk.WORD, height=2.5, width=40)
text_widget.insert(tk.END, text_content)
text_widget.config(state=tk.DISABLED)  # Set the text widget to read-only
text_widget.pack(padx=10, pady=5)
# Username Entry
label_username = tk.Label(root, text="Username:", font=font_large)
label_username.pack(pady=pad_large)
entry_username = tk.Entry(root, font=font_large)
entry_username.pack(pady=(0, pad_large))

# Password Entry
label_password = tk.Label(root, text="Password:", font=font_large)
label_password.pack(pady=(0, pad_large))
entry_password = tk.Entry(root, show='*', font=font_large)
entry_password.pack(pady=(0, pad_large))

# Submit Button
submit_button = tk.Button(
    root, text="Submit", command=submit_action, font=font_large)
submit_button.pack(pady=pad_large)

# Message Label 
label_message = tk.Label(root, text="", font=font_large)
label_message.pack(pady=pad_large)

root.mainloop()
