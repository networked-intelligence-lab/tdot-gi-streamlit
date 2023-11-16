import requests
from datetime import datetime
import pytz

def get_last_commit_time(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()
        if commits:
            # Parse the date string
            date_str = commits[0]['commit']['committer']['date']
            date_obj_utc = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')

            # Convert to UTC and then to EST/EDT
            utc_zone = pytz.timezone('UTC')
            est_zone = pytz.timezone('America/New_York')
            date_obj_utc = utc_zone.localize(date_obj_utc)
            date_obj_est = date_obj_utc.astimezone(est_zone)

            # Format the date
            formatted_date = date_obj_est.strftime('%b %d, %Y %I:%M%p %Z')
            return formatted_date
        else:
            return "No commits found"
    else:
        return f"Error: {response.status_code}"
