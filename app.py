#!/usr/bin/python3
"""
Flask app that takes two GET request parameters
"""
from flask import Flask, request


app = Flask(__name__)


@app.route("/api", methods=['GET'])
def get_details():
    """
    Function that gets users slack name and track
    """
    try:
        slack_name = request.args.get('slack_name')
        track = request.args.get('track')



if __name__ == "__main__":
    app.run(debug=True)
