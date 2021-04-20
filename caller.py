import requests
import json
import beautifulsoup

url = "https://paulserian.pythonanywhere.com/"
data = requests.get(url).text

print(data)
