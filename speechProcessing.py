import speech_recognition
from gtts import gTTS
from playsound import playsound

recognizer = speech_recognition.Recognizer()

def say(text):
    ausgabe = gTTS(text=text, lang="de", slow=False)
    ausgabe.stream()
    ausgabe.save("tts.mp3")
    playsound("tts.mp3")

def recognizeLanguage():
    with speech_recognition.Microphone() as micro:
        print("Bitte jetzt sprechen...")
        recording = recognizer.record(micro, duration=5)
        print("...")
        try:
            text = recognizer.recognize_google(recording, language="de-DE")
            return text
        except speech_recognition.UnknownValueError:
            return ["error"]



