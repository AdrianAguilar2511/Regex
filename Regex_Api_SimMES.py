import pandas as pd
import os

os.system('cls')



import requests
import pandas as pd

url = "https://api.thingspeak.com/channels/9/feeds.json"

response = requests.get(url)

data = response.json()

feeds = data["feeds"]

df = pd.DataFrame(feeds)

print(df.head())
