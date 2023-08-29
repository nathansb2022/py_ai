#!/usr/bin/env python3
#
#Let's learn AI together

import openai, os, time, pandas as pd 
#input api key
openai.api_key = os.environ.get('OKEY')

def get_completion(prompt, model="gpt-3.5-turbo"):

	messages = [{"role": "user", "content": prompt}]
	response = openai.ChatCompletion.create(
		model=model,
		messages=messages,
		temperature=0,
		)
	return response.choices[0].message["content"]

while(1):
	print('')
	prompt = input('What would you like to ask? (q to exit) ')
	if prompt.lower() == 'q':
		break
	else:
		print('')
		response = get_completion(prompt)
		print(response)
