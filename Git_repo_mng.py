from git import Repo

# Clone a repository
repo_url = "https://github.com/pranjalkatkar11/Python_Script"
repo = Repo.clone_from(repo_url, "/tmp/repo")
print(f"Cloned: {repo_url}")