import requests
from collections import defaultdict
import re
import csv
from dotenv import load_dotenv
import os


load_dotenv()
token = os.getenv('GITHUB_TOKEN')  # Optional, if you are only interested in public repositories

# Configuration
REPOSITORY_OWNER = "<>"
REPOSITORY_NAME = "<>"
REPO_URL = f'https://api.github.com/repos/{REPOSITORY_OWNER}/{REPOSITORY_NAME}/commits'
HEADERS = {'Authorization': f'token {token}'}


def fetch_commits(url):
    """ Fetch commits from GitHub API """
    commits = []
    while url:
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            print('Data could not be fetched:', response.status_code)
            break
        data = response.json()
        commits.extend(data)
        if 'Link' in response.headers:
            links = response.headers['Link']
            next_link = [link.split(';')[0].strip('<>') for link in links.split(',') if 'rel="next"' in link]
            url = next_link[0] if next_link else None
        else:
            break
    return commits


def analyze_commits(commits):
    """Analyzes commit messages to categorize them according to conventional commit types."""
    types_count = defaultdict(int)
    pattern = r'^(\w+)(?:\(\w+\))?:'
    # feat(backend): Add new endpoint
    # feat: minor change in frontend
    # commit_type[(scope)]: message

    for commit in commits:
        message = commit['commit']['message'].split('\n', 1)[0]
        match = re.match(pattern, message)
        if match:
            commit_type = match.group(1)
            types_count[commit_type] += 1
        else:
            types_count['other'] += 1

    return types_count


def export_to_csv(data, filename='commit_types.csv'):
    """ Export to CSV file """
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Commit Type', 'Count'])
        for commit_type, count in data.items():
            writer.writerow([commit_type, count])
    print(f'Data has been saved in: {filename}')


if __name__ == "__main__":
    # Download and analyze commits
    commits = fetch_commits(REPO_URL)
    commit_analysis = analyze_commits(commits)

    # Display the results
    for commit_type, count in commit_analysis.items():
        print(f'{commit_type}: {count}')

    export_to_csv(commit_analysis)