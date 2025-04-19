        # Lists and Real Estate Analyzer

import csv

    # Function to read entire file
def getDataInput():
    listRecords = []
    with open('RealEstateData.csv', 'r') as file:
        csvReader = csv.reader(file)
        next(csvReader)
        for row in csvReader:
            listRecords.append(row)
    return listRecords

    # Code a function that receives a list and returns a float
def getMedian(listPrice: list[float]) -> float:
    count = len(listPrice)
    if count % 2 == 1:
        return listPrice[count // 2]
    else:
        evenCount = count // 2
        return listPrice[evenCount] + listPrice[evenCount - 1] / 2

    # code a main that calls getDataInput to get info, code a loop that reads each record
def main():
    listRecords = getDataInput()
    listPrice = []
    dictType = {}
    dictZip = {}
    dictCity = {}

    # extract data using a loop
    for record in listRecords:
        sCity = record[1]
        sZip = record[2]
        sType = record[7]
        fPrice = float(record[8])
        listPrice.append(fPrice)

    # making sure there is only one entry
        if sCity not in dictCity:
            dictCity[sCity] = 0
        dictCity[sCity] += fPrice

        if sZip not in dictZip:
            dictZip[sZip] = 0
        dictZip[sZip] += fPrice

        if sType not in dictType:
            dictType[sType] = 0
        dictType[sType] += fPrice

    # sort prices than calculate Min, Max, Total, Avg, Median
    listPrice.sort()
    minPrice = min(listPrice)
    maxPrice = max(listPrice)
    totalPrice = sum(listPrice)
    avgPrice = totalPrice / len(listPrice)
    medPrice = getMedian(listPrice)

    # Output Min, Max, total, Avg, Median with 2 decimal positions
    print(f"Minimum:{' ':18s}{minPrice:16,.2f}")
    print(f"Maximum:{' ':18s}{maxPrice:16,.2f}")
    print(f"Sum:{' ':22s}{totalPrice:16,.2f}")
    print(f"Average:{' ':18s}{avgPrice:16,.2f}")
    print(f"Median:{' ':19s}{medPrice:16,.2f}")

    # Output summary by Property Type
    print("\n\t\tSummary by Property Type:")
    for propertyType, total in dictType.items():
        print(f"{propertyType:18s} {total:21,.2f}")

    # Output summary by City
    print("\n\t\tSummary by City:")
    for city, total in dictCity.items():
        print(f"{city:18s} {total:21,.2f}")

main()