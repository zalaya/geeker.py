import requests

def show_information(user):
  for key, value in user.items():
    key = key.replace("_", " ").capitalize()

    print(f"{key}: {value}")

def main():
  username = input("GitHub username: ")
  response = requests.get(f"https://api.github.com/users/{username}")

  if (response.status_code == 200):
    show_information(response.json())
  else:
    print(f"No users found with the username: {username}")
    