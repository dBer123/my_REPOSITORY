import requests

url = r"https://api.airvisual.com/v2/city?city=Ramat Gan&state=Tel Aviv&country=Israel&key=106c3aac-89f8-48d0-a55a-ad283c2bb216"
response = requests.get(url)
print(response.json())