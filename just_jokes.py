from random import choice
import requests


#get user input for API request
user_input = input("What kind of jokes are you looking for? ").lower()
url = "http://icanhazdadjoke.com/search"

#get response from API request based on user input in JSON format
res = requests.get(
        url, 
        headers={"Accept": "application/json"}, 
        params={"term": user_input},
).json()

num_jokes = res["total_jokes"]
results = res["results"]

#print out custom response based on how many results found using user input
if num_jokes > 1:
    print(f"Whoa, {num_jokes} jokes were found for your search query of \'{user_input}\'. Here is a couple of them.")
    print()
    for i in range(2):
        print("++++")
        print(choice(results)["joke"])
        print("++++")
        print()
elif num_jokes == 1:
    print(f"Well, only one joke for \'{user_input}\'. And here it is.")
    print()
    print(results[0]["joke"])
else:
    print(f"Sorry, no jokes for \'{user_input}\' here.")


