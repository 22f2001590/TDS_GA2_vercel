# write a flask app

from flask import Flask, request, jsonify
from flask_cors import CORS

import json

app = Flask(__name__)

CORS(app)  # Enable CORS for cross-origin requests (CORS)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/api')
def home():
    file_path = "q-vercel-python.json"
    names = request.args.getlist('name')  # Extract list of names from query params

    marks = []
    with open(file_path, "r") as file:
        data = json.load(file)

        for name in names:
            mark = next((d["marks"] for d in data if d["name"] == name), None)
            marks.append(mark if mark is not None else "Not Found")

    return jsonify({'marks': marks})  # Return a proper JSON response



if __name__ == '__main__':
    app.run(debug=True)

