from github import Github

class GitHubClient:
    def __init__(self, token) -> None:
        # initialise PyGitHub with the token
        self.client = Github(token)

    def get_user_info(self):
        # get the authenticated user
        user = self.client.get_user()

        # return username & public_repos count
        return{
            'username': user.login,
            'public_repos': user.public_repos
        }