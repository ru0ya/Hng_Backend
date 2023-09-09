#!/usr/bin/python3
from datetime import datetime


current_day = datetime.now().strftime('%A')
utc_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-5] + 'Z'


data = {
        "slack_name": "Victor Mwangi",
        "current_day": current_day,
        "utc_time": utc_time,
        "track": "backend",
        "github_file_url":
        "https://github.com/ru0ya/Hng_Backend/blob/main/stage_one/main.py",
        "github_repo_url": "https://github.com/ru0ya/Hng_Backend/tree/main/stage_one",
        "status_code": 200
        }
