import requests
import json

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
    listed = set(events)
    for event in listed:
        count = sum(1 for e in events if e == event)
        #Had to look this up, but this is a good way of finding out the amount of times 
        #an even occurs. Now I need to find a way to print this out so that it looks like:
        # - Pushed 3 commmits to URL.
        #Hmm
        print(f"{event}: {count}")
    


def main():
    opening = "Hello, please enter the GitHub Username: "
    username = input(opening)
    
    test = get_api_url(username)
    if test:
        event_list = [event['type'] for event in test]
        collate(event_list)
        

            #print(f"Event: {event['type']}")
            #print(f"URL: {event['repo']['url']}\n")
    else:
        print("No data found")

    # So far, this creates a program that takes a username and returns the events and url of 
    # the user. This is OK, but I now need to make a list of the things that are happening
    # and then collate them into a much easier to read format. OK.



if __name__ == "__main__":
    main()
