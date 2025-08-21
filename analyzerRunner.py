from dataPull import fetch_data
from dataAnalyzer import convert_to_DataFrame

def main():
   try:
      rawData = fetch_data()  # fetch json data from API link
      readable = convert_to_DataFrame(rawData)  # convert json data to DataFrame
      if readable.empty:
         print("No valid data available for analysis.")
      else:
         print(readable.head(5))
   finally:
      print("If no data provided, please try again.")

if __name__ == "__main__":
   main()
