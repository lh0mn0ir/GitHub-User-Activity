import requests


def get_user(username):
    API_URL = f"https://api.github.com/users/{username}"
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            print(f"Fetching data for user: {username}")
            user = response.json()
            return user
        else:
            print(f"Error, {response.status_code} - {response.reason}")
            return None
    except requests.exceptions.ConnectionError as e:
        print(f"Error fetching API data: {e}")
        return None

if __name__ == "__main__":
    user = get_user("lh0mn0ir")
    if user:
        print(user)