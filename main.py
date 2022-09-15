import readJSON
import covidDataOperations
import apiJsonDataOperations
# declaring constant variable below is a constant variable
FILENAME = 'sampleCovidData.json'
URL = 'https://apps.who.int/gho/athena/api/?format=json'

def main():
    covidJsonData = readJSON.readJson(FILENAME)
    print("Performing operations on covid data")
    print("Total Number of Records are:", covidDataOperations.totalNoOfRec(covidJsonData))
    print("Printing all record")

    print("Performing operations on data fetched from the api")
    covidDataOperations.allRec(covidJsonData)
    data = apiJsonDataOperations.getJSON(URL)
    # print(data)
    apiJsonDataOperations.operations(data)


if __name__ == '__main__':
    main()
