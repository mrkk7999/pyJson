import requests
def getJSON(URL):
    r = requests.get(url=URL)
    data = r.json()
    return data

def operations(data):
    print("Print dimension from data")
    print(data["dimension"])