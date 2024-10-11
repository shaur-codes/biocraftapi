from flask import Flask, request
import google.generativeai as genai

app = Flask(__name__)

@app.route('/generate/', methods=['GET'])
def generate_content():
    api_key = request.args.get('api_key')
    tone = request.args.get('tone')
    format = request.args.get('format')
    text = request.args.get('text')
    
    if not all([api_key, tone, format, text]):
        return "Missing parameters", 400
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    query = f"i am trying to create my bio for my profile on a social media platform, modify the given introduction in {tone} tone and make sure to answer only what is asked and only in plain text as your response will be sent directly through an API also try to make it {format}, here is the intro:"
    response = model.generate_content(f"{query} {text}")
    
    return response.text

if __name__ == '__main__':
    app.run(debug=True)
