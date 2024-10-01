from flask import Flask, request
import google.generativeai as genai

app = Flask(__name__)

@app.route('/<api_key>/', methods=['GET'])
def generate_content(api_key):
    tone = request.args.get('tone')
    format = request.args.get('format')
    text = request.args.get('text')

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    query=f"i am trying to create my bio for my profile on a social media platform,modify the given introduction in {tone} tone and make sure to answer only what is asked and only in plane text as your response will be sent directly through an API also try to make it {format}, here is the intro:"
    response = model.generate_content(f"{query} {text}")
    print(f"{query} {text}")
    return response.text

if __name__ == '__main__':
    app.run(debug=True)


#http://127.0.0.1:5000/<API goes here>/?tone=professional-and-funny&format=short-and-captivating&text=i%20am%20shaurya%20mishra%20and%20i%20am%20the%20ceo%20of%20quickbio.net%20i%20am%20interested%20in%20cybersecurity%20and%20automation
