from subprocess import check_call, check_output
import time
import speech_recognition
import pyttsx

class Assistant(object):
	def __init__(self):
		self.speech_engine = pyttsx.init('espeak') # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
		self.speech_engine.setProperty('rate', 150)
	   	self.recognizer = speech_recognition.Recognizer()

	def speak(self, text):
	    self.speech_engine.say(text)
	    self.speech_engine.runAndWait()

	def listen(self):
	    with speech_recognition.Microphone(device_index=3, sample_rate = 48000) as source:
	        self.recognizer.adjust_for_ambient_noise(source)
	        audio = self.recognizer.listen(source)

	    try:
	        #return recognizer.recognize_sphinx(audio)
	        return self.recognizer.recognize_google(audio)
	    except speech_recognition.UnknownValueError:
	        print("Could not understand audio")
	    except speech_recognition.RequestError as e:
	        print("Recog Error; {0}".format(e))

	    return ""

	def request_handler(self):
	    self.speak("Hey! I am Jarvis, what can i do for you today")
	    while True:
	        request = self.listen().lower()
	        print request
	        if request == "shutdown":
	            check_call(["shutdown"])
	        elif request == "restart":
	            check_call(["restart"])
	        elif request == "wish birthday":
	            check_call("python ./task/wish_birthday.py")
	        elif request == "post in bulk":
	            check_call("python ./task/bulk_posting.py")
	        elif request == "reply birthday":
	         	check_call("python ./tasks/reply_birthday.py")
	        elif request == "download subtitle":
	        	check_call("python ./tasks/download_subtitle")
	        elif request == "play game":
	        	check_call("python ./tasks/2048/2048.py")
	        elif request == "exit":
	            speak("Bye! See you next time")
	            return
	        self.speak("How can i help you?")

if __name__ == '__main__':
	assistant = Assistant()
	assistant.request_handler()
