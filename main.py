from github import Github
import os

# 🔑 Replace with your GitHub Personal Access Token
TOKEN = "your_personal_access_token"

# 📁 Folder you want to upload
FOLDER_PATH = "my_project"

# 📦 Repo name
REPO_NAME = "my-python-upload-repo"

# Connect to GitHub
g = Github(TOKEN)
user = g.get_user()

# Create repo
repo = user.create_repo(REPO_NAME, private=False)
print(f"✅ Repository '{REPO_NAME}' created!")

# Function to upload files
def upload_folder(folder_path, repo, base_path=""):
    for item in os.listdir(folder_path):
        full_path = os.path.join(folder_path, item)
        repo_path = os.path.join(base_path, item)

        if os.path.isfile(full_path):
            with open(full_path, "r", encoding="utf-8") as file:
                content = file.read()

            repo.create_file(
                repo_path,
                f"Add {repo_path}",
                content
            )
            print(f"📄 Uploaded: {repo_path}")

        elif os.path.isdir(full_path):
            upload_folder(full_path, repo, repo_path)

# Upload all files
upload_folder(FOLDER_PATH, repo)

print("🚀 All files uploaded successfully!")
