import requests

# get API URL and do things with it
# e.g. https://api.github.com/users/kamranahmedse/events

base_url = "https://api.github.com/users/"

def get_api_url(username):
    url = f"{base_url}{username}/events"
    response = requests.get(url)

    if response.status_code == 200:
        git_data = response.json()
        return git_data
    else:
        print("Error: ", response.status_code)

    

def main():
    opening = "Hello, please enter the GitHub Username: "
    username = input(opening)
    
    test = get_api_url(username)
    if test:
        for event in test:
            print(f"Event: {event['type']}")
            print(f"URL: {event['repo']['url']}\n")
    else:
        print("No data found")



if __name__ == "__main__":
    main()
