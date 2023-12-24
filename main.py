import requests
import json

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'YOUR_API_KEY'

# API endpoint
url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=' + api_key

# Request headers
headers = {
    'Content-Type': 'application/json'
}
inp = "Give me 3 reasons to play chess"
# Request payload
payload = {
    'contents': [
        {
            'parts': [
                {
                    'text': inp
                }
            ]
        }
    ]
}

# Make POST request
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Extract and print only the "text" field
text = response.json()['candidates'][0]['content']['parts'][0]['text']
print(text)
