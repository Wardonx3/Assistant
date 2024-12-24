import speech_recognition as sr
import webbrowser
import tkinter as tk
from tkinter import messagebox

# Function definitions for opening websites
def open_facebook():
    webbrowser.open("https://www.facebook.com")

def open_google():
    webbrowser.open("https://www.google.com")

def open_youtube():
    webbrowser.open("https://www.youtube.com")

def start_listening():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            messagebox.showinfo("Listening", "Speak your command...")
            # Adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio, language="en-US").lower()

            # Process the command
            if "facebook" in command:
                open_facebook()
                messagebox.showinfo("Success", "Opened Facebook!")
            elif "google" in command:
                open_google()
                messagebox.showinfo("Success", "Opened Google!")
            elif "youtube" in command:
                open_youtube()
                messagebox.showinfo("Success", "Opened YouTube!")
            else:
                messagebox.showerror("Error", "Command not recognized. Try again!")
        except sr.UnknownValueError:
            messagebox.showerror("Error", "Sorry, I could not understand the command.")
        except sr.RequestError as e:
            messagebox.showerror("Error", f"Request failed; {e}")

# GUI setup
def setup_gui():
    app = tk.Tk()
    app.title("Voice Command Assistant")

    label = tk.Label(app, text="Click 'Start' and give a voice command.", font=("Arial", 14))
    label.pack(pady=20)

    start_button = tk.Button(app, text="Start Listening", command=start_listening, font=("Arial", 12))
    start_button.pack(pady=10)

    exit_button = tk.Button(app, text="Exit", command=app.quit, font=("Arial", 12))
    exit_button.pack(pady=10)

    app.geometry("400x200")
    app.mainloop()

# Main function
if __name__ == "__main__":
    setup_gui()
