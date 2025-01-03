import json
from datetime import datetime

def event_durations(json_str):
    events = json.loads(json_str)
    durations = []
    for event in events:
        start_date = datetime.strptime(event['start_date'], '%Y-%m-%d')
        end_date = datetime.strptime(event['end_date'], '%Y-%m-%d')
        duration = (end_date - start_date).days
        durations.append(duration)
    return durations
