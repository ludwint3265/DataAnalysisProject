import requests

url = "https://data.cityofnewyork.us/resource/nc67-uf89.json"  # Replace with your actual endpoint
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # If the response is JSON
    print(data)
else:
    print(f"Error: {response.status_code}")
   
