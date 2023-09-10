#!/usr/bin/python3
"""
Flask app that takes two GET request parameters
"""
from flask import Flask, request, jsonify
from datetime import datetime


app = Flask(__name__)


@app.route("/api", methods=['GET'])
def get_details():
    """
    Function that gets users slack name and track
    """
    slack_name = request.args.get('slack_name',)
    track = request.args.get('track',)

    current_day = datetime.now().strftime("%A")
    utc_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    data = {
            "slack_name": slack_name,
            "current_day": current_day,
            "utc_time": utc_time,
            "track": track,
            "github_file_url": "https://github.com/ru0ya/Hng_Backend/blob/main/stage_one/main.py",
            "github_repo_url": "https://github.com/ru0ya/Hng_Backend/tree/main/stage_one",
            "status_code": 200
            }

    if not slack_name or not track:
        return jsonify({'error': 'Two arguments are required'}), 400

    if slack_name == data['slack_name'] and track == data['track']:
        return jsonify(data), 200
    else:
        return jsonify({'error': 'One or both parameters not found'}), 404


if __name__ == "__main__":
    
    app.run(debug=True)
