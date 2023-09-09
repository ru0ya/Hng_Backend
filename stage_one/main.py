#!/usr/bin/python3
"""
Flask app that takes two GET request parameters
"""
from flask import Flask, request, jsonify

from user_data import data


app = Flask(__name__)


@app.route("/api", methods=['GET'])
def get_details():
    """
    Function that gets users slack name and track
    """
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    if not slack_name or not track:
        return jsonify({'error': 'Two arguments are required'}), 400

    if slack_name == data['slack_name'] and track == data['track']:
        return jsonify(data), 200
    else:
        return jsonify({'error': 'One or both parameters not found'}), 404


if __name__ == "__main__":
    app.run(debug=True)
