import requests
url="https://uselessfacts.jsph.pl/api/v2/facts/random"
try:
    res=requests.get(url=url)
    res.raise_for_status()
    data=res.json()
    print(data['text'])
except requests.exceptions.RequestException as e:
    print("Error generating fact:",e)
