allRecList = []


def totalNoOfRec(json_data):
    count = 0
    for i in json_data['records']:
        count = count + 1
        # print(i)
    return count


def allRec(json_data):
    global allRecList
    allRecList = []
    for i in json_data['records']:
        temp_dict = {}
        temp_dict["dateRep"] = i["dateRep"]
        temp_dict["cases"] = i["cases"]
        temp_dict["deaths"] = i["deaths"]
        temp_dict["countriesAndTerritories"] = i["countriesAndTerritories"]
        temp_dict["popData2019"] = i["popData2019"]
        temp_dict["continentExp"] = i["continentExp"]
        allRecList.append(temp_dict)
    # totalCases = 0
    for j in allRecList:
        # totalCases = totalCases + j["cases"]
        print(j["cases"])
    # print("Total no of cases",totalCases)
    # print(allRecList)
