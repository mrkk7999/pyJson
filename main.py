import json


def readJson():
    print("Opening sampleCovidData file")
    f = open('sampleCovidData.json')
    print("File opened successfully")
    # print(f.read())
    global jsonData
    jsonData = json.load(f)
    # print(data)
    f.close()


def totalNoOfRec():
    count = 0
    for i in jsonData['records']:
        count = count + 1
        # print(i)
    return count


def allRec():
    global allRecList
    allRecList = []
    for i in jsonData['records']:
        tempDict = {}
        tempDict["dateRep"] = i["dateRep"]
        tempDict["cases"] = i["cases"]
        tempDict["deaths"] = i["deaths"]
        tempDict["countriesAndTerritories"] = i["countriesAndTerritories"]
        tempDict["popData2019"] = i["popData2019"]
        tempDict["continentExp"] = i["continentExp"]
        allRecList.append(tempDict)
    # totalCases = 0
    for j in allRecList:
        # totalCases = totalCases + j["cases"]
        print(j["cases"])
    # print("Total no of cases",totalCases)
    # print(allRecList)


def main():
    readJson()
    print("Total Number of Records are:", totalNoOfRec())
    print("Printing all record")
    allRec()


if __name__ == '__main__':
    main()
