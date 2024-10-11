from flask import Flask, request, jsonify, render_template_string
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

        # Display a help page if no parameters are provided
        if not any([tone, format, text]):
            html_content = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>API Guide - Social Bio Generator</title>
                <style>
                    body { font-family: Arial, sans-serif; color: #333; background-color: #f4f8fb; text-align: center; padding: 50px; }
                    h1 { color: #4a90e2; }
                    .container { max-width: 600px; margin: auto; background: #fff; padding: 20px; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); }
                    code { background-color: #f1f1f1; padding: 2px 5px; border-radius: 5px; }
                    .example { background-color: #eef9ff; padding: 10px; border-radius: 10px; margin-top: 20px; color: #4a90e2; }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Welcome to the Social Bio Generator API!</h1>
                    <p>Generate custom bios for social media profiles with a specific tone and format.</p>
                    <h3>How to use this API:</h3>
                    <p>Send a GET request to <code>/generate/</code> with the following parameters:</p>
                    <ul style="text-align: left;">
                        <li><code>tone</code>: The desired tone for your bio (e.g., <em>professional, funny</em>).</li>
                        <li><code>format</code>: The preferred format for your bio (e.g., <em>short, captivating</em>).</li>
                        <li><code>text</code>: The introductory text you want to modify.</li>
                    </ul>
                    <div class="example">
                        <h3>Example Request:</h3>
                        <p><code>/generate/?tone=professional&format=short&text=I%20am%20a%20web%20developer</code></p>
                    </div>
                    <p>Enjoy crafting the perfect bio!</p>
                </div>
            </body>
            </html>
            """
            return render_template_string(html_content)

        # Check for missing parameters
        if not all([tone, format, text]):
            return jsonify({"error": "Missing parameters"}), 400

        # Generate content
        model = genai.GenerativeModel('gemini-pro')
        query = f"Modify this intro in {tone} tone as {format}:"
        response = model.generate_content(f"{query} {text}")

        return jsonify({"text": response.text})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
