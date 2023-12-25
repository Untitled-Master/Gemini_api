<div align="center">
      <h1> <img src="https://miro.medium.com/v2/resize:fit:720/format:webp/1*uUFFjzaVmE_1RrfcVbx2QQ.jpeg" width="80px"><br/>Gemini Api</h1>
     </div>
<p align="center"> <a href="https://github.com/Untitled-Master" target="_blank"><img alt="" src="https://img.shields.io/badge/Website-EA4C89?style=normal&logo=dribbble&logoColor=white" style="vertical-align:center" /></a> <a href="https://twitter.com/untitledmaster0" target="_blank"><img alt="" src="https://img.shields.io/badge/Twitter-1DA1F2?style=normal&logo=twitter&logoColor=white" style="vertical-align:center" /></a> <a href="https://www.instagram.com/untitledmaster/" target="_blank"><img alt="" src="https://img.shields.io/badge/Instagram-E4405F?style=normal&logo=instagram&logoColor=white" style="vertical-align:center" /></a> <a href="}" target="_blank"><img alt="" src="https://img.shields.io/badge/LinkedIn-0077B5?style=normal&logo=linkedin&logoColor=white" style="vertical-align:center" /></a> </p>

# Description
Gemini is a new model developed by Google, and Bard is becoming usable again. With Gemini, it is now possible to get almost perfect answers to your queries by providing them with images, audio, and text.

# Features
Gemini is a new model developed by Google, and Bard is becoming usable again. With Gemini, it is now possible to get almost perfect answers to your queries by providing them with images, audio, and text.

- This api uses the request method to get Gemini responses in a fast and easy-to-understand method.

I would like to highlight the fact that this is NOT the official way to use Gemini but it is one of the easiest.

# Tech Used
 ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
      
# Generative Language API Client

This Python script provides a simple interface to interact with the Generative Language API, specifically the Gemini Pro model. The code sends a request to generate content based on the input provided and prints the generated text.

## Getting Started

Follow these steps to set up and use the Generative Language API client:

### Prerequisites

- **API Key**: Replace 'YOUR_API_KEY' with your actual API key. You can obtain an API key by following the instructions on the [AI Google Dev](https://ai.google.dev/tutorials/setup).

### How to Setup

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/Untitled-Master/Gemini_api.git
    ```

2. Open the script in a text editor and replace 'YOUR_API_KEY' with your actual API key.

3. Run the script:

    ```bash
    python main.py
    ```

### API References

The script uses the following API endpoint:

- **Endpoint**: `https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent`
- **Method**: POST
- **Headers**: 
  - Content-Type: application/json
- **Request Payload**:
  ```json
  {
      "contents": [
          {
              "parts": [
                  {
                      "text": "Your input text here"
                  }
              ]
          }
      ]
  }
  ```

### Example

```python
inp = "Give me 3 reasons to play chess"
text = generative_language_api_client.generate_content(inp)
print(text)
```

## Additional Information

Feel free to customize and integrate this script into your projects. If you encounter any issues or have suggestions for improvements, please [open an issue](https://github.com/Untitled-Master/Gemini_api/issues).

Enjoy!
<!-- </> with 💛 by readMD (https://readmd.itsvg.in) -->
    
