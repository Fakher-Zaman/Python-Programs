# pip install pyttsx3
# pip install playsound

import smtplib
import speech_recognition as sr
from email.message import EmailMessage
import pyttsx3

listener = sr.Recognizer()
tts = pyttsx3.Engine()

def talking_tom(text):
    tts.say(text)
    tts.runAndWait()

def mic():
    with sr.Microphone() as source:
        print("Program is listening...")
        voice = listener.listen(source)
        data = listener.recognize_google(voice)
        print(data)
        return data.lower()

# Reciever Info
dict = {"fakhar zaman":"fakharzaman@gmail.com.com"}

def send_mail(receiver, subject, body):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("034851fakherzaman@gmail.com", "AutoGeneratePass")
    email = EmailMessage()
    email["From"] = "034851fakherzaman@gmail.com"
    email["To"] = receiver 
    email["Subject"] = subject
    email.set_content(body)
    server.send_message(email)

def main_poc():
    talking_tom("To show do you want to send this email?")
    name = mic()
    receiver = dict[name]
    talking_tom("Speak the subject of the email")
    subject = mic()
    talking_tom("Speak the message of the email")
    body = mic()
    send_mail(receiver, subject, body)
    print("Your email has been sent!")

main_poc()