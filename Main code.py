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


def collate(events):
    event_list = [event[0] for event in events]
    event_url = [event[1] for event in events]

    for event, url in zip(event_list, event_url):
        count = sum(1 for e, _ in events if e == event)

        print(f"Created {count} {event} events to {url}")    


def main():
    username = input("Hello, please enter the GitHub Username: ")
    
    test = get_api_url(username)
    if test:
        event_list = [event['type'] for event in test]
        event_url = [event['repo']['url'] for event in test]

        merged_list = list(zip(event_list, event_url))

        collate(merged_list)
    else:
        print("No data found")

if __name__ == "__main__":
    main()
