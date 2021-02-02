import sys
import os
import geocoder
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import re
import math
import csv

#
# mapping function for occupancy
#

def MapOccupancy(parcelHeader):
    if 'Residential' in parcelHeader:
        if '1-Family' in parcelHeader or 'Sfr' in parcelHeader:
            return [1, 'Residential Single Family']
        elif '2-Family' in parcelHeader:
            return [2, 'Residential Town-Home']
        elif 'Condo' in parcelHeader or '3-Family':
            return [3, 'Residential Multi-Family']
        elif 'Mixed' in parcelHeader:
            return [12, 'Mixed Use Residential']

    elif 'Commercial' in parcelHeader:
        if 'Office' in parcelHeader:
            return [4, 'Office']
        elif 'Hotel' in parcelHeader:
            return [5, 'Hotel']
        elif 'Condo' in parcelHeader or 'Apartments' in parcelHeader:
            return [3, 'Residential Multi-Family']
        elif 'Mixed' in parcelHeader:
            return [14, 'Mixed Use Office']
        elif 'Parking Garage' in parcelHeader:
            return [15, 'Parking']
        elif 'Retail' in parcelHeader or 'Restaurant' in parcelHeader:
            return [10, 'Retail']
        elif '1-Family' in parcelHeader or 'Sfr' in parcelHeader or 'Res Struct' in parcelHeader:
            return [1, 'Residential Single Family']
        elif '2-Family' in parcelHeader:
            return [2, 'Residential Town-Home']
        elif 'Religious' in parcelHeader or 'Correctional' in parcelHeader :
            return [4, 'Office']
        elif 'High Rise Apartmen' in parcelHeader:
            return [12, 'Mixed Use Residential']
        elif 'Manufacturing/Proc' in parcelHeader:
            return [7, 'Industrial']
        elif 'Boarding/Rooming H' in parcelHeader:
            return [5, 'Hotel']
        elif 'Bank' in parcelHeader:
            return [4, 'Office']
        elif 'Senior Housing' in parcelHeader:
            return [3, 'Residential Multi-Family']
        elif 'Shopping' in parcelHeader or 'Food' in parcelHeader or 'Dinner':
            return [10, 'Retail']
        elif 'Auto Service Garag' in parcelHeader:
            return [7, 'Industrial']
        elif 'Warehouse' in parcelHeader:
            return [8, 'Warehouse']
        elif 'School' in parcelHeader:
            return [8, 'School']

    if('Vacant' in parcelHeader or 'Vac/Land' in parcelHeader or 'Leasehold' in parcelHeader or 'Parking Lots' in parcelHeader or 'DEACTIVATED' in parcelHeader):
        return [0, 'Unknown']
    print("Unknown Occupancy: {}", parcelHeader)

#
# some regular expressions for extractiung data
#

storyHtRegex = re.compile(".+Story Ht : ([0-9.]+).+")
yearBuiltRegex = re.compile(".+\nYear Built : ([0-9]+).+")
yrBltRegex = re.compile(".+Yr Blt:\s+([0-9]+)\n.+")
BldgAreaRegex = re.compile(".+Bldg Area:\s+([0-9,]+).+")


id = 0
numParcels = 0
numResidential = 0
numResidentialFailed = 0
numCommerical = 0
numCommericalFailed = 0
numVacant = 0
numParkingLots = 0
numLeasehold = 0
numDeactivated = 0

buildingsFile = open('AnchorageBuildings.csv', 'w')
buildingsWriter = csv.writer(buildingsFile)
buildingsWriter.writerow(["ID", "Area", "Stories", "Year Built", "Type ID", "Occupancy", "ParcelId"])


#Starting the browser and opening tax assessor's data website for Anchorage
browser = webdriver.Chrome() 
url = "https://www.muni.org/pw/public.html"
browser.get(url)

#Fill parcel search box with zero
parcelBox1 = browser.find_element_by_name("PAR1")
parcelBox1.send_keys('0')

#Click on Submit
submitButton = browser.find_element_by_name("submitbtn") 
submitButton.click()

for i in range(1,4):
    print("Processing results page {}".format(i))
    #Finding the parcels table with XPath
    parcelsTable = browser.find_elements_by_xpath("//table[1]/tbody/tr[2]/td/table[5]/tbody/tr")
    parcelsCount = len(parcelsTable)

    #Looping through the parcels table rows
    for i in range(1, parcelsCount):
        #extracting the parcel id
        parcelRow = browser.find_element_by_xpath("//table[1]/tbody/tr[2]/td/table[5]/tbody/tr[{}]".format(i+1))
        parcelIdCell = parcelRow.find_element_by_xpath(".//td[1]")
        if parcelIdCell is not None:
            parcelId = parcelIdCell.text
            
            parcelAddressCell = parcelRow.find_element_by_xpath(".//td[3]")
            parcelAddress = ""
            if parcelAddressCell is not None:
                parcelAddress = parcelAddressCell.text
                g = geocoder.google("{}, Anchorage Alaska".format(parcelAddress))
                print(g.latlng)

            print("Id: {} Adress {}".format(parcelId, parcelAddress))


                
            
            #Clinking on the parcel to open the parcel details
            parcelIdCell.click()
            WebDriverWait(browser, 10)

            occupancy = 'unknown'
            #We can now parse the parcel details
            #e.g. let's find the occupancy
            try:
                parcelSoup = BeautifulSoup(browser.page_source, "html.parser")

                #We will assume the header is always the seventh table row (maybe using trial and error)
                parcelHeader = parcelSoup.findAll('tr')[7].text
                [occupancyId, occupancy] = MapOccupancy(parcelHeader)

                if("Vacant" in parcelHeader):
                    numVacant = numVacant + 1
                    # print("VACANT {}".format(partcelId))
                elif("Leasehold Master" in parcelHeader):
                    numLeasehold = numLeasehold + 1
                    # print("LEASEHOLD MASTER {}".format(parcelId))                    
                elif("Parking Lots" in parcelHeader):
                    numParkingLots = numParkingLots + 1
                    # print("PARKING {}".format(parcelId))
                    
                elif("Residential" in parcelHeader or ""):

                    numResidential = numResidential + 1
                    if not parcelSoup.findAll('tr')[12].text == 'IMPROVEMENT DATA':
                        numResidentialFailed = numResidentialFailed + 1
                        print("Parcel: {} Failed to parse Residential!".format(parcelId))
                        continue

                    improvementData = parcelSoup.findAll('tr')[13].text
                    numStories = int(math.floor(float((storyHtRegex.match(improvementData).group(1)))))
                    yearBuilt = int(yearBuiltRegex.match(improvementData).group(1))

                    improvementArea = parcelSoup.findAll('tr')[15].text
                    area = float(improvementArea.rstrip().splitlines()[-1].split(' ')[-1])

                    
                    id = id + 1 
                    buildingsWriter.writerow([id, area, numStories, yearBuilt, occupancyId, occupancy, parcelId, parcelAddress ])
                    print("Resid Parcel: {} is {} and id is {}".format(parcelId, occupancy, occupancyId))
                    
                elif("Condominium" in parcelHeader or "Condo/Hoa" in parcelHeader):
                    print('Begining Condo')
                    numCommerical = numCommerical + 1
                    if parcelSoup.findAll('tr')[12].text == 'ASSESSMENT HISTORY':
                        buildingData = parcelSoup.findAll('tr')[17].text

                        floors = []
                        for floorLine in parcelSoup.findAll('tr')[19].text.splitlines()[2:]:
                            if not floorLine:
                                continue
                            floorRange = floorLine.split()[0].split('/')
                            for floorNo in floorRange:
                                if floorNo.isdigit():
                                    floors.append(int(floorNo))

                        numStories = 1
                        if len(floors) > 0:
                            numStories = max(floors)

                        yearBuilt = int(yrBltRegex.match(buildingData).group(1))
                        area = float(BldgAreaRegex.match(buildingData).group(1).replace(',',''))
                    else:
                        improvementData = parcelSoup.findAll('tr')[13].text
                        numStories = int(math.floor(float((storyHtRegex.match(improvementData).group(1)))))
                        yearBuilt = int(yearBuiltRegex.match(improvementData).group(1))

                        improvementArea = parcelSoup.findAll('tr')[15].text
                        area = float(improvementArea.rstrip().splitlines()[-1].split(' ')[-1])

                    parcelAddressCell = parcelRow.find_element_by_xpath(".//td[3]")
                    parcelAddress = parcelAddressCell.text
                    print("Id: {} Adress {}".format(parcelId, parcelAddress))
                    
                    id = id + 1 
                    buildingsWriter.writerow([id, area, numStories, yearBuilt, occupancyId, occupancy, parcelId, parcelAddress ])
                    print("Condo Parcel: {} is {} and id is {}".format(parcelId, occupancy, occupancyId))

                elif("Commercial" in parcelHeader):
                    print('Begining Commercial')
                    numCommerical = numCommerical + 1
                    if len(parcelSoup.findAll('tr')) < 20:
                        print("Parcel {} Commercial Parsing Failed!".format(partcelId))
                        numCommericalFailed = numCommericalFailed + 1
                        continue

                    buildingData = parcelSoup.findAll('tr')[17].text

                    floors = []
                    for floorLine in parcelSoup.findAll('tr')[19].text.splitlines()[2:]:
                        if not floorLine:
                            continue
                        floorRange = floorLine.split()[0].split('/')
                        for floorNo in floorRange:
                            if floorNo.isdigit():
                                floors.append(int(floorNo))

                    numStories = 1
                    if len(floors) > 0:
                        numStories = max(floors)

                    yearBuilt = int(yrBltRegex.match(buildingData).group(1))
                    area = float(BldgAreaRegex.match(buildingData).group(1).replace(',',''))

                    parcelAddressCell = parcelRow.find_element_by_xpath(".//td[3]")
                    parcelAddress = parcelAddressCell.text
                    print("Id: {} Adress {}".format(parcelId, parcelAddress))
                    
                    id = id + 1
                    buildingsWriter.writerow([id, area, numStories, yearBuilt, occupancyId, occupancy, parcelId, parcelAddress ])
                    print("Commercial Parcel: {} is {} and id is {}".format(parcelId, occupancy, occupancyId))
            
                elif("DEACTIVATED" in parcelHeader):
                    numDeactivated = numDeactivated + 1
                    print("DEACTIVATED")
                else:
                    print("Parcel: {} Unkown Parcel: {}".format(parcelID,parcelHeader))
                        
                print("Parcel: {} is {} and id is {}".format(parcelId, occupancy, occupancyId))
                
                
            except:
                "Error: Failed to process parcel: " + parcelId


            #clicking on the back button
            backButton = browser.find_element_by_name("backbtn")
            backButton.click()
    #Going to next page in the search results       
    nextButton = browser.find_element_by_name("nextbtn")
    nextButton.click()



#Excercise 4: Can we extract more information about these buildings
#e.g. number of stories, year built, area...etc.
