from subprocess import check_call, check_output
import time
import speech_recognition
import pyttsx

speech_engine = pyttsx.init('espeak') # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
speech_engine.setProperty('rate', 150)

def speak(text):
    speech_engine.say(text)
    speech_engine.runAndWait()

recognizer = speech_recognition.Recognizer()

def listen():
    with speech_recognition.Microphone(device_index=3, sample_rate = 48000) as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        #return recognizer.recognize_sphinx(audio)
        return recognizer.recognize_google(audio)
    except speech_recognition.UnknownValueError:
        print("Could not understand audio")
    except speech_recognition.RequestError as e:
        print("Recog Error; {0}".format(e))

    return ""

def process():
    speak("Hey! I am Jarvis, what can i do for you today")
    while True:
        request = listen().lower()
        print request
        if request == "shutdown":
            check_call(["shutdown"])
        elif request == "what is the time":
            print time.ctime()
        elif request == "exit":
            speak("Bye! See you next time")
            return
        speak("How can i help you?")

if __name__ == '__main__':
    process()
