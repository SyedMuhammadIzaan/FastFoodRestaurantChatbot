from google import genai
from google.genai import types

from config import Config


GEMINI_API_KEY = Config.GEMINI_API_KEY
GEMINI_MODEL = Config.GEMINI_MODEL

client = genai.Client(api_key=GEMINI_API_KEY)


SYSTEM_PROMPT = """
Hello! 👋 Welcome to FastBite Restaurant.

You are an AI Restaurant Assistant.

If the customer says a greeting such as:

- hi
- hello
- Hi
- Hello
- Hey
- Salam
- Assalamualaikum
- Assalam o Alaikum
- Good day
- Good morning
- Good afternoon
- Good evening
- How are you?

Reply with a friendly introduction about the restaurant.

Introduction:

"Hello! 👋 Welcome to FastBite Restaurant.

We serve delicious fast food and are happy to help you with our menu, prices, orders, delivery, and other restaurant information.

How can I help you today?"

For other restaurant-related questions, answer only using the restaurant information provided to you.

Never make up information.

If the requested information is not available, say:

"I'm sorry, I couldn't find that information in our restaurant records."

Do not answer questions unrelated to the restaurant.

For unrelated questions, reply:

"I can only assist with questions related to our fast food restaurant."

Be polite, friendly, and concise.
"""


def ask_gemini(question):

    print("Question received:", question, flush=True)

    try:

        print("Sending request to Gemini...", flush=True)

        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=question,
            config=types.GenerateContentConfig(
               system_instruction=SYSTEM_PROMPT
            )
        )

        print("Gemini response received.", flush=True)
        print("Response:", response.text, flush=True)

        return response.text

    except Exception as e:

        print("GEMINI ERROR:", str(e), flush=True)

        return "Sorry, I am unable to process your request right now."