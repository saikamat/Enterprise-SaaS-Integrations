from github import Github
from src.config import GITHUB_TOKEN
from src.integrations.github_client import GitHubClient

def main():
    print("Testing GitHub integration...")

    # create client
    client = GitHubClient(GITHUB_TOKEN)

    # get user info
    user_info = client.get_user_info()

    # display results
    print(f"✓ Successfully connected to GitHub")
    print(f"Username: {user_info['username']}")
    print(f"Public Repos: {user_info['public_repos']}")

if __name__ == "__main__":
    main()