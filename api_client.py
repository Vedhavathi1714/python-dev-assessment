import requests

def fetch_and_display_users(num_users):
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        if not isinstance(num_users, int) or isinstance(num_users, bool):
            raise ValueError("num_users must be an integer.")

        if num_users < 0:
            raise ValueError("num_users cannot be negative.")

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        users = response.json()

        if not isinstance(users, list):
            raise ValueError("Unexpected JSON structure.")

        for user in users[:num_users]:
            if not isinstance(user, dict):
                raise ValueError("Unexpected user data structure.")

            name = user["name"]
            email = user["email"]
            address = user["address"]
            city = address["city"]

            print("Name:", name)
            print("Email:", email)
            print("City:", city)
            print("-" * 30)

        return users[:num_users]

    except requests.exceptions.RequestException as error:
        print(f"Network error while fetching users: {error}")
        return None

    except (ValueError, KeyError, TypeError) as error:
        print(f"Error: Invalid or unexpected API data: {error}")
        return None


if __name__ == "__main__":
    fetch_and_display_users(4)
    fetch_and_display_users(16)
