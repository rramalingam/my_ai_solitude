#
# This exercise is to practise the prompt development for an usecase of
# exploring usage of LLM for text transformation tasks such as language translation, spelling and
# grammar checking, tone adjustment and format conversion
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

#Build some sample texts and prompts for language translation process

#Translation
prompt = f"""
Translate the following English text to Telugu:  
```Hi, I would like to order a blender```
"""

prompt_1 = f"""
Tell me which language this is:  
```హాయ్, నేను ఒక మిక్సీ ఆర్డర్ చేయాలనుకుంటున్నాను.```
"""

prompt_2 = f"""
Translate the following text to Tamil in both the \
formal and informal forms: 
'హాయ్, నేను ఒక మిక్సీ ఆర్డర్ చేయాలనుకుంటున్నాను.'
"""
#res = get_ai_response(prompt_2)

#print(res.text)

#Multi-language translation
user_messages = [
  "La performance du système est plus lente que d'habitude.",  # System performance is slower than normal         
  "Mi monitor tiene píxeles que no se iluminan.",              # My monitor has pixels that are not lighting
  "Il mio mouse non funziona",                                 # My mouse is not working
  "Mój klawisz Ctrl jest zepsuty",                             # My keyboard has a broken control key
  "我的屏幕在闪烁"                                               # My screen is flashing
]

# for issue in user_messages:
#     prompt_multi = f"Tell me what language this is: ```{issue}```"
#     lang = get_ai_response(prompt_multi)
#     print(f"Original message ({lang.text}): {issue}")

#     prompt_multi = f"""
#     Translate the following  text to English \
#     and Korean: ```{issue}```
#     """
#     response = get_ai_response(prompt_multi)
#     print(response.text, "\n")

#Tone Transformation
prompt_tone = f"""
Translate the following from slang to a business letter: 
'Dude, This is Joe, check out this spec on this standing lamp.'
"""
# res = get_ai_response(prompt_tone)

# print(res.text)


#Format conversion
data_json = { "resturant employees" :[ 
    {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},
    {"name":"Bob", "email":"bob32@gmail.com"},
    {"name":"Jai", "email":"jai87@gmail.com"}
]}

prompt_format = f"""
Translate the following python dictionary from JSON to an HTML 
table with column headers and title: {data_json}
"""
#res = get_ai_response(prompt_format)

#print(res.text)

#from IPython.display import display, Markdown, Latex, HTML, JSON
#display(HTML(res.text))


#spellcheck / grammar check
text = [ 
  "The girl with the black and white puppies have a ball.",  # The girl has a ball.
  "Yolanda has her notebook.", # ok
  "Its going to be a long day. Does the car need it’s oil changed?",  # Homonyms
  "Their goes my freedom. There going to bring they’re suitcases.",  # Homonyms
  "Your going to need you’re notebook.",  # Homonyms
  "That medicine effects my ability to sleep. Have you heard of the butterfly affect?", # Homonyms
  "This phrase is to cherck chatGPT for speling abilitty"  # spelling
]
# for t in text:
#     prompt_spell = f"""Proofread and correct the following text
#     and rewrite the corrected version. If you don't find
#     and errors, just say "No errors found". Don't use 
#     any punctuation around the text:
#     ```{t}```"""
#     res = get_ai_response(prompt_spell)
#     print(res.text)

text = f"""
Got this for my daughter for her birthday cuz she keeps taking 
mine from my room.  Yes, adults also like pandas too.  She takes 
it everywhere with her, and it's super soft and cute.  One of the 
ears is a bit lower than the other, and I don't think that was 
designed to be asymmetrical. It's a bit small for what I paid for it 
though. I think there might be other options that are bigger for 
the same price.  It arrived a day earlier than expected, so I got 
to play with it myself before I gave it to my daughter.
"""
prompt_correct = f"proofread and correct this review: ```{text}```"

# res = get_ai_response(prompt_correct)
# print(res.text)

from IPython.display import display, Markdown, Latex, HTML, JSON
from redlines import Redlines

# diff = Redlines(text,res.text)
# display(Markdown(diff.output_markdown))


prompt_rewrite = f"""
proofread and correct this review. Make it more compelling. 
Ensure it follows APA style guide and targets an advanced reader. 
Output in markdown format.
Text: ```{text}```
"""

res = get_ai_response(prompt_rewrite)
print(res.text)

display(Markdown(res.text))