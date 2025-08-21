import requests

def fetch_data():
   url = "https://data.cityofnewyork.us/resource/nc67-uf89.json"  # API Endpoint
   response = requests.get(url)

   if response.status_code == 200:
      try:
         data = response.json()  # If the response is JSON, try to make it a response.json object
         print("Successfully retrieved data")
         return data
      except ValueError as e:
         print(f"Error parsing JSON: {e}")
         return None
   else:
      raise RuntimeError(f"API request failed with status code {response.status_code}")


