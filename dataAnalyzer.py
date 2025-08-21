import pandas as pd

#converts the JSON of requests.get object to a DataFrame into a readable format
def convert_to_DataFrame(data):
   if data == None:
      print("No data was retrieved, returning empty DataFrame")
      return pd.DataFrame() # return an empty DataFrame object
   try:
      df = pd.DataFrame(data)
      return df
   except Exception as e:
      print(f"Error converting to DataFrame: {e}")
      return pd.DataFrame()  # Return an empty DataFrame on error
