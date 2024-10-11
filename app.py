from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

@app.route('/generate/', methods=['GET'])
def generate_content():
    try:
        api_key = os.getenv('GOOGLE_API_KEY')
        genai.configure(api_key=api_key)

        tone = request.args.get('tone')
        format = request.args.get('format')
        text = request.args.get('text')

        if not all([tone, format, text]):
            return jsonify({"error": "Missing parameters"}), 400

        model = genai.GenerativeModel('gemini-pro')
        query = f"Modify this intro in {tone} tone as {format}:"
        response = model.generate_content(f"{query} {text}")

        return jsonify({"text": response.text})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
