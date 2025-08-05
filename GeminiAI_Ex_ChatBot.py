#
# This exercise is to practise the prompt development for an usecase of
# exploring to utilise chat format to have extended conversation with chatbots for
# specific tasks or behaviors
#

from google import genai
from google.genai import types
import os


#Gemini way starts here
client = genai.Client()

# #provide a common function to call the model with an iterative mode of input to response model
# def get_ai_response_for_prompts (prompts, messages):
#     # response = client.models.generate_content(
#     # model = "gemini-2.5-flash", contents=prompts, config={'temperature':temperature})
#     response = client.models.generate_content(
#     model = "gemini-2.5-flash", contents=prompts, config=types.GenerateContentConfig(system_instruction=messages))
#     return response

# #Build some sample messages for Bot to learn and prepare as assistant

# messages =  [  
# {'role':'system', 'content':'You are an assistant that speaks like Shakespeare.'},    
# {'role':'user', 'content':'tell me a joke'},   
# {'role':'assistant', 'content':'Why did the chicken cross the road'},   
# {'role':'user', 'content':'I don\'t know'}  ]



# res = get_ai_response_for_prompts("Helo there", messages)
# print(res.text)


# client = genai.Client()
chat = client.chats.create(model="gemini-2.5-flash")

response = chat.send_message("I have 2 dogs in my house.")
print(response.text)

response = chat.send_message("How many paws are in my house?")
print(response.text)

for message in chat.get_history():
    print(f'role - {message.role}',end=": ")
    print(message.parts[0].text)

