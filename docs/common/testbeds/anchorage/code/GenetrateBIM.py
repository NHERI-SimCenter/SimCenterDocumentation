import os
import sys
import shutil
import glob
import urllib2
from bs4 import BeautifulSoup
import re
import math
import csv


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
    print "Unknown Occupancy: " + parcelHeader


storyHtRegex = re.compile(".+Story Ht : ([0-9.]+).+")
yearBuiltRegex = re.compile(".+\nYear Built : ([0-9]+).+")
yrBltRegex = re.compile(".+Yr Blt:\s+([0-9]+)\n.+")
BldgAreaRegex = re.compile(".+Bldg Area:\s+([0-9,]+).+")


with open('AnchorageBuildings.csv', 'wb+') as buildingsFile:
    buildingsWriter = csv.writer(buildingsFile)
    buildingsWriter.writerow(["ID", "Area", "Stories", "Year Built", "Type ID", "Occupancy", "ParcelId"])
    parcelsHtml = glob.glob('.\\Html\\*\\*.html')
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
    
    for parcelFile in parcelsHtml:
        numParcels = numParcels + 1
        if numParcels % 100 == 0:
            print '\nParcels: {}'.format(numParcels)
            print 'Residential: {} (Failed: {})'.format(numResidential, numResidentialFailed)
            print 'Commercial: {} (Failed: {})'.format(numCommerical, numCommericalFailed)
            print 'Vacant: {}'.format(numVacant)
            print 'ParkingLots: {}'.format(numParkingLots)
            print 'Leasehold Master: {}'.format(numLeasehold)
            print 'Deactivated: {}'.format(numDeactivated)

        parcelId = os.path.splitext(parcelFile)[0].split('\\')[-1]
        #if parcelId < '020':
        #    continue
        url = os.path.abspath(parcelFile)

        try:
            parcelSoup = BeautifulSoup(open(parcelFile), "html.parser")

            parcelHeader = parcelSoup.findAll('tr')[7].text
            [occupancyId, occupancy] = MapOccupancy(parcelHeader)
            
            if("Vacant" in parcelHeader):
                numVacant = numVacant + 1
                #print "Vacant"
            elif("Leasehold Master" in parcelHeader):
                numLeasehold = numLeasehold + 1
                #print "Leasehold Master"
            elif("Parking Lots" in parcelHeader):
                numParkingLots = numParkingLots + 1
                #print "Parking Lots"
            elif("Residential" in parcelHeader or ""):
                numResidential = numResidential + 1
                if not parcelSoup.findAll('tr')[12].text == 'IMPROVEMENT DATA':
                    numResidentialFailed = numResidentialFailed + 1
                    print 'Failed to parse Residential!'
                    continue

                improvementData = parcelSoup.findAll('tr')[13].text
                numStories = int(math.floor(float((storyHtRegex.match(improvementData).group(1)))))
                #print numStories
                yearBuilt = int(yearBuiltRegex.match(improvementData).group(1))
                #print yearBuilt

                improvementArea = parcelSoup.findAll('tr')[15].text
                area = float(improvementArea.rstrip().splitlines()[-1].split(' ')[-1])
                #print area
                id = id + 1 
                buildingsWriter.writerow([id, area, numStories, yearBuilt, occupancyId, occupancy, parcelId ])
            elif("Condominium" in parcelHeader or "Condo/Hoa" in parcelHeader):
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
                    #print numStories
                    yearBuilt = int(yearBuiltRegex.match(improvementData).group(1))
                    #print yearBuilt

                    improvementArea = parcelSoup.findAll('tr')[15].text
                    area = float(improvementArea.rstrip().splitlines()[-1].split(' ')[-1])

            
                #print area
                id = id + 1 
                buildingsWriter.writerow([id, area, numStories, yearBuilt, occupancyId, occupancy, parcelId ])
            elif("Commercial" in parcelHeader):
                numCommerical = numCommerical + 1
                if len(parcelSoup.findAll('tr')) < 20:
                    print 'Commercial Parsing Failed!'
                    numCommericalFailed = numCommericalFailed + 1
                    continue

                id = id + 1
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


                buildingsWriter.writerow([id, area, numStories, yearBuilt, occupancyId, occupancy, parcelId ])
            elif("DEACTIVATED" in parcelHeader):
                numDeactivated = numDeactivated + 1
                #print "DEACTIVATED"
            else:
                print "!!!Unkown Parcel: " + parcelHeader

        except:
            "Error: Failed to process parcel: " + parcelId
