# py_ai

Let's learn AI together

Python program to translate speech to text, Google to recognize audio, and ask chatgpt(OpenAI) a question. A verbal reponse will be provided on the asked question.
Your AI partner is stored in openAISpeech2Text.py. Install the packages and start asking questions on your linux machine.
Additionally, added a commandline version aiEnteractCmdLine.py.
Remember to install required packages, add api key, and name of AI. Tested on ubuntu.

# Add Variables
Add variables in openAISpeech2Text.py or add at runtime.
In checkAPIKey(), I commented out the env variable for my OpenAI API. Change if you would like.
In checkAIName, I commented out the name, jarvis. Change if you would like.
In checKAIModel(), I commented out the variable for the AI model (gpt-3.5-turbo). Change if you would like.

# Sources

[Python_ChatGPT](https://www.analyticsvidhya.com/blog/2023/05/how-to-use-chatgpt-api-in-python/)

[text2Speech_Python](https://www.geeksforgeeks.org/python-convert-speech-to-text-and-text-to-speech/)

# How to Use

For AI with audio
```bash
python3 openAISpeech2Text.py
```               
For AI on the cmdline
```bash
python3 aiEnteractCmdLine.py
```

# Install Requirements

To get python squared away:
```bash
sudo pip3 install speechrecognition pyttsx3 openai pandas pyfiglet
```
To get linux squared away:
```bash
sudo apt install espeak jackd2 python3-pyaudio
```
