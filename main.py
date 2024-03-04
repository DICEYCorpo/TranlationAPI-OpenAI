from deep_translator import GoogleTranslator
import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

textInp1 = input("Please enter the text you want to translate: ")



client = OpenAI(
    api_key=os.getenv("OPENAIAPI")
)

with open("systemPromptParagraph.txt", "r") as f:
  systemPromptParagraph = f.read()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": systemPromptParagraph
    },
    {
      "role": "user",
      "content": textInp1
    }

  ],
  temperature=1,
  max_tokens=4096,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
textInp1 = response.choices[0].message.content

translatedInp1 = (GoogleTranslator(source='auto', target='es').translate(textInp1))
with open("systemPrompt.txt", "r") as f:
    systemPrompt = f.read()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": systemPrompt
    },
    {
      "role": "user",
      "content": "Spanish:\n\n\"" + translatedInp1 + "\"\n\nEnglish:\n\n\"" + textInp1 + "\"\n\n"
    }

  ],
  temperature=1,
  max_tokens=4096,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response.choices[0].message.content)