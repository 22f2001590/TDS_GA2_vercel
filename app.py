from flask import Flask, request, jsonify
import json
from urllib.parse import unquote

app = Flask(__name__)

@app.route('/<path:data>/api')
def process_data(data):
    try:
        # Decode and parse the JSON from the URL
        decoded_data = unquote(data)
        json_data = json.loads(decoded_data)

        # Get names from query parameters
        names = request.args.getlist('name')  # Multiple 'name' parameters

        # Extract marks for matching names
        marks = [item["marks"] for item in json_data if item["name"] in names]

        return jsonify({"marks": marks})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

