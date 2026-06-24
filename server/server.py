import requests
import json
import asyncio
import datetime
from flask import *

app = Flask(__name__)

@app.route("/credits", methods=["GET"])
def get_credits_info():

    api_key = request.args.get("key")

    url = "https://openrouter.ai/api/v1/credits"

    headers = {"Authorization": f"Bearer {api_key}"}

    response = requests.get(url, headers=headers)

    return response.text


@app.route("/ask_ai", methods=["GET"])
def ask_ai():
    message = request.args.get("message")
    api_key = request.args.get("key")

    prompt = f"""
Current time: {datetime.datetime.now()}

If the user asks about the weather, your response must look like this:

GLASS_WEATHER_QUESTION
<temperature in the city mentioned by the user (degrees Celsius)>

Example:

GLASS_WEATHER_QUESTION
16

If the user asks to solve a math problem, your response must look like this:

GLASS_SOLVE_MATH
<answer>

Example:

GLASS_SOLVE_MATH
12

If the user asks to translate text, respond like this:

GLASS_TRANSLATE_TEXT
<target language>
<original text>
<translated text>

Example:

GLASS_TRANSLATE_TEXT
English
привет как дела
hello how are you

If the user asks to convert currency from one to another, respond like this:

GLASS_CONVERT_MONEY
<original currency>
<conversion result>

Example:

GLASS_CONVERT_MONEY
10 USD
28 BYN

If the user asks to take a picture, respond only with:

GLASS_TAKE_A_PICTURE

If the user asks to open a camera app, respond only with:

GLASS_TAKE_A_PICTURE

If the user asks to record a video, respond with:

GLASS_RECORD_A_VIDEO

You may answer any other questions normally. For any other question, respond like this:

<answer>

Example:

Google Glass is glasses that ...

Respond ONLY in the same language the user is using.

Do not write "Understood" or "As you requested" — act normal. Also, the GLASS_... tag and the response must be on separate lines.

User's message: {message}
"""
    
    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    },
    data=json.dumps({
        "model": "google/gemini-3.1-flash-lite",
        "messages": [
        {
            "role": "user",
            "content": [
            {
                "type": "text",
                "text": prompt
            }
            ]
        }
        ]
    })
    )
    try:

        response_data = response.json()
        content = response_data['choices'][0]['message']['content']

        
        return json.loads(response.text)['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error Code: {e}")
        print(f"Response: {response.text}")
        print(f"User question: {message}")
        return "Error while processing your request!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)