#
# This exercise is to practise the prompt development for an usecase of
# reviewing and summarising the product reviews
#

from google import genai
import openai
import os


#Gemini way starts here
client = genai.Client()

#provide a common function to call the model with an input prompt to generate response
def get_ai_response (prompt):
    response = client.models.generate_content(
    model = "gemini-2.5-flash", contents=prompt)
    return response

#Build a sample product review
prod_review = f"""
I've bought a Honeywell charging adapter that had two USB-C ports considering the fact that the latest
smart phones and smart watches are currently on USB-C based chargers and we can't carry multiple charging
adapters for multiple devices. The reason to purchase the Honeywell charger is because its an GaN based 
as well as little cheaper compared to other branded ones. Whereas my intention was always that Honeywell 
is a known brand and they do provide good customer support in case any issue comes. I bought this charger on 
Amazon India ecommerce website. This charger worked for me for only 6 months and not more than that. Naturally, 
I started looking for warranty in Amazon to get support of fixing the issue or replacement. To my surprise, Amazon 
did not provide any ability to provide the support mechanism either through them or Honeywell even though it was clear 
that the product was under warranty. This review is to enable and caution the potential future buyers to think before 
purchasing any product in Amazon as well as Honeywell charger. 
"""

#create a prompt providing a task to provide a summary of reviews on a product

prompt = f"""
Your task is to generate a short summary of a product review from an ecommerce site. Summarise the review below, delimited
by triple backticks, in at most 30 words.
Review: ```{prod_review}```
"""

res = get_ai_response(prompt)

print(res.text)


prompt = f"""
Your task is to extract relevant information from a product review from an ecommerce site to give 
feedback to the product brand. 

From the review below, delimited by triple quotes extract the information relevant to product. Limit to 30 words. 

Review: ```{prod_review}```
"""

res = get_ai_response(prompt)

print(res.text)