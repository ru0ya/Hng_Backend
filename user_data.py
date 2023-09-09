#!/usr/bin/python3
from datetime import datetime


utc_time = datetime.utcnow()
current_day = utc_time.strftime('%A')


data = {
        "slack_name": "Victor Mwangi",
        "current_day": current_day,
        "utc_time": utc_time,
        "track": "backend",
        "github_file_url":
