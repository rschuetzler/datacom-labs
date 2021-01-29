import requests
import pprint  # Pretty printing for Python dictionaries

# Get user input
city = input("Enter a city: ")
print(city)

# Using a Python f-string to put the city in the URL
url = f"https://api.teleport.org/api/cities/?search={city}"

# Getting the results and converting it to a Python dictionary
results = requests.get(url).json()
print("Raw\n")
print(results)  # Raw results
print("Formatted:\n")  # Leave an extra line

pp = pprint.PrettyPrinter(indent=2)
pp.pprint(results)  # Formatted for easy reading

# Getting what I want out of the results
#
full_city = results["_embedded"]["city:search-results"][0]["matching_full_name"]
print("\nFull city name\n")
print(full_city)
