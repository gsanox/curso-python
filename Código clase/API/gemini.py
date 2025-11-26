from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

# print(os.getenv("GOOGLE_GEMINI_API_KEY"))
# print(os.getenv("OPENAI_API_KEY"))

client = genai.Client(api_key=os.getenv("GOOGLE_GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash", 
    contents="Una lista de 5 escritores españoles del siglo 19"
)
print(response.text)

# response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "user", "content": "Hola, ¿qué tal?"}
#     ]
# )

# print(response.choices[0].message["content"])