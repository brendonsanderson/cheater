import schedule
import time
import random
from datetime import datetime
from github import Github

# GitHub credentials
github_token = 'YOUR_GITHUB_TOKEN'  # Replace with your GitHub personal access token
repo_owner = 'your_username'
repo_name = 'your_repo_name'

# Function to update the GitHub repository
def update_github_repo():
    # Create a GitHub instance using the access token
    g = Github(github_token)

    # Get the repository
    repo = g.get_user(repo_owner).get_repo(repo_name)

    # Update the repository with a new commit or other desired changes
    # For example, you can create a new file or update an existing one
    # Replace this with your specific update logic

    # Create a new file with a timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_content = f"Update at {timestamp}"
    file_path = "update_file.txt"

    # Get the default branch (assuming it's 'main')
    default_branch = repo.get_branch(repo.default_branch)
    
    repo.create_file(file_path, f"Auto-update at {timestamp}", file_content, branch="main")

    print(f"Repository updated at {timestamp}")

# Schedule the job to run 0-4 times a day with some variability
for _ in range(random.randint(0, 4)):
    # Randomly choose a time to run the job
    hours = random.randint(0, 23)
    minutes = random.randint(0, 59)
    schedule.every().day.at(f"{hours:02d}:{minutes:02d}").do(update_github_repo)

# Run the scheduled job continuously
while True:
    schedule.run_pending()
    time.sleep(1)
