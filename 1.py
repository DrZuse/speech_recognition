# google speech recognition
import speech_recognition as sr

r = sr.Recognizer()
#
file_path = "swartz.wav"

with sr.AudioFile(file_path) as source:
    audio = r.record(source)

try:
    text = r.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Could not understand audio.")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
