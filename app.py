from flask import Flask, request

app = Flask(__name__)

@app.route('/generate/', methods=['GET'])
def generate_content():
    return "API is working"

if __name__ == '__main__':
    app.run(debug=True)
