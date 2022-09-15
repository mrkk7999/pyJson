import json
def readJson(fname):
    print("Opening sampleCovidData file")
    f = open(fname)
    print("File opened successfully")
    # print(f.read())
    global jsonData
    jsonData = json.load(f)
    # print(data)
    f.close()
    return jsonData
