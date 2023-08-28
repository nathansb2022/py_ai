#!/bin/usr/env python3
#
#Let's learn AI together
#
# Python program to translate
# speech to text, Google to recognize audio and ask chatgpt(OpenAI) a question.
# After reponse has been requested, verbally respond with the answer.
# Install the packages and start asking questions on your linux machine
# Remember to install required packages, add api key, and name of AI
# Tested on ubuntu
# Sources
# https://www.analyticsvidhya.com/blog/2023/05/how-to-use-chatgpt-api-in-python/
# https://www.geeksforgeeks.org/python-convert-speech-to-text-and-text-to-speech/
#
# In checkAPIKey(), I commented out the env variable for my OpenAI API. Change if you would like
# In checkAIName, I commented out the name, jarvis. Change if you would like
# In checKAIModel(), I commented out the variable for the AI model (gpt-3.5-turbo). Change if you would like
#
# INSTALL
# pip3 install speechrecognition pyttsx3 openai pandas pyfiglet
# sudo apt install espeak jackd2 python3-pyaudio
#
# import these libraries, may have to use pip3 install for many of them (above command)
import speech_recognition as sr, pyttsx3, openai, os, time, pandas as pd, warnings, pyfiglet

warnings.filterwarnings('ignore')

# Initialize the recognizer
r = sr.Recognizer()

# Opening art
def art():

	ascii_banner = pyfiglet.figlet_format("PY A.I.\n")
	print(ascii_banner)

# check if the api has been input
def checKAPIKey():
	# input your Open AI API key here
	OKEY = ""
	#OKEY = os.environ.get('OKEY')
	if not OKEY:
		OKEY = input("Please input the Open API key: \n")

		return OKEY
	else:

		return OKEY

# check if the name has been input
def checKAIName():
	# input the name of your AI below
	name = ""
	#name = "jarvis"
	if not name:
		name = input("Please input the name of your AI: \n")

		return name
	else:

		return name

# check if the model has been input
def checKAIModel():
	# input the model
	flavor = ""
	#flavor = "gpt-3.5-turbo"
	if not flavor:
		flavor = input("Please input the model of your AI, i.e. gpt-3.5-turbo : \n")

		return flavor
	else:

		return flavor

# reach out and get the response from chatgpt
def get_completion(prompt, flavor):

	messages = [{"role": "user", "content": prompt}]
	response = openai.ChatCompletion.create(
		model=flavor,
		messages=messages,
		temperature=0,
		)
	return response.choices[0].message["content"]
 
# Function to convert text to
# speech
def SpeakText(command):
	 
	# Initialize the engine
	engine = pyttsx3.init()
	engine.setProperty('rate', 150)
	engine.say(command)
	engine.runAndWait()

# introduction function
def milliDollarQuestion(name):    

	ask = "Hello! This is " + name + ". What would you like to ask"
	print('')
	print('')
	print("Hello! This is " + name + ". What would you like to ask?\n")
	SpeakText(ask)

# Loops waiting for the keyword jarvis then asks chatgpt your question utilizing google trans. and
# responds
def interact(r):
	# art
	art()
	# get AI model
	flavor = checKAIModel()
	# input put your api key below if not set above
	OKEY = checKAPIKey()	
	openai.api_key = OKEY
	# Find out what you named your AI
	name = checKAIName()

	milliDollarQuestion(name)
	# Loops waiting for the request then asks chatgpt your question utilizing google trans. and
	# responds
	while(1):   
		# Exception handling to handle
		# exceptions at the runtime
		try:
			# use the microphone as source for input.
			with sr.Microphone() as source2:
				 
				# wait for a second to let the recognizer
				# adjust the energy threshold based on
				# the surrounding noise level
				r.adjust_for_ambient_noise(source2, duration=0.2)
				 
				# listens for the user's input
				audio2 = r.listen(source2)
				 
				# Using google to recognize audio
				MyText = r.recognize_google(audio2)
				MyText = MyText.lower()
				response = get_completion(MyText, flavor)
				print('')
				print('')
				# if you hear these exit the program
				if "exit" in str(MyText) or "bye" in str(MyText) or "sleep" in str(MyText):
					SpeakText("Ok bye")
					exit()
				# reference for what was asked
				print("Did you ask ",MyText)
				print('')
				print('')
				# print response from chatgpt
				print(response)
				# now speak it
				SpeakText(response)
				print('')
				print('')
				 
		except sr.RequestError as e:
			print("Could not request results; {0}".format(e))
			 
		except sr.UnknownValueError:
			print("unknown error occurred\n")
			
if __name__ == "__main__":
	interact(r)

	 
