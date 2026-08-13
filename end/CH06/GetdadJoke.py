import requests

url = "https://icanhazdadjoke.com/"
payload = {}
headers = {
        "Accept": "application/json"
}

response = requests.request("GET", url, headers=headers, data=payload)

data = response.json()

print(data["joke"])