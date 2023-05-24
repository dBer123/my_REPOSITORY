import json
import requests
import pandas as pd


QUERY = """
query {
  characters{
    results{
      name
      episode{
        name
      }
    }
  }
}
"""
URL = r"https://rickandmortyapi.com/graphql"
response = requests.post(URL, json={'query': QUERY})
json_data = json.loads(response.text)

df_data = json_data["data"]["characters"]["results"]
for characters in df_data:
    print(characters['name'])
    print(len(characters['episode']))
    
# עוד דרך כי למה לא
df = pd.DataFrame(df_data)
df.sort_values('episode',key=lambda x:x.str.len())    
print(df)    