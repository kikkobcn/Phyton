# Truzz Blogg - Youtube link: https://youtu.be/q-N6IcgCqCE
# Speech recognition in Python ::: How to convert an Audio File to Text

import speech_recognition as sr
import time
import subprocess
subprocess.call(["ffmpeg", "-i", "audio\\1.1-concepto-basico-de-scrum.mp3","audio\\1.1-concepto-basico-de-scrum.wav"])

r = sr.Recognizer()

with sr.AudioFile("audio\\1.1-concepto-basico-de-scrum.wav") as source:
    # print("Say Something...")
    audio = r.listen(source)

    try:
        print("Reading audio file. Please, wait a moment...")
        text = r.recognize_google(audio, language='es-ES')
        time.sleep(1.5)
        print(text)
    except:
        print("I am sorry! I can not understand!")