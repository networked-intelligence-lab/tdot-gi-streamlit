import requests
from datetime import datetime
import pytz


def get_last_commit_time():
    owner, repo = "networked-intelligence-lab", "tdot-gi-streamlit"
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


def get_total_commits():
    owner, repo = "networked-intelligence-lab", "tdot-gi-streamlit"
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url, {'per_page': 1})

    if response.status_code == 200:
        # Check if the 'last' link is available in the response headers
        if 'last' in response.links:
            last_page_url = response.links['last']['url']
            last_page_num = int(last_page_url.split('=')[-1])
            return last_page_num
        else:
            # If there's no 'last' link, it means there's only one page
            return len(response.json())
    else:
        return f"Error: {response.status_code}"

