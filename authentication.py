# import json
# import hashlib
# import pyttsx3


# def hash_password(password):
#     return hashlib.sha256(password.encode('utf-8')).hexdigest()


# def load_file():
#     try:
#         with open('user_history.json', 'r') as file:
#             return json.load(file)
#     except FileNotFoundError:
#         return {}


def save_file(history):
    with open('user_history.json', 'w') as file:
        json.dump(history, file)


def log_to_file_and_speak(message):
    with open('log.txt', 'a') as file:
        file.write(message + '\n')
    print(message)  # Optional: if you still want to print to console
    speak_message(message)


def speak_message(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()


def authenticate_user(name, password, history):
    hashed_password = hash_password(password)

    if name in history:
        if history[name] == hashed_password:
            return "Hello " + name
        else:
            return "Incorrect password."
    else:
        history[name] = hashed_password
        save_file(history)
        return f"New user added, welcome !!! {name}"
