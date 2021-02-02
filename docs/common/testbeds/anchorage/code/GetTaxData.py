import sys
import os
from selenium import webdriver

#Starting the browser
options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome(chrome_options=options) 
url = "https://www.muni.org/pw/public.html"
browser.get(url)

#Range
startParcel = sys.argv[1]
endParcel = sys.argv[2]

if(not os.path.exists("Html")):
    os.mkdir("Html")

outDir = "Html/Parcels{}-{}".format(startParcel, endParcel)
if(not os.path.exists(outDir)):
    os.mkdir(outDir)

#Fill parcel with zero

parcelBox1 = browser.find_element_by_name("PAR1")
parcelBox1.send_keys(startParcel)

#Click on Submit
submitButton = browser.find_element_by_name("submitbtn") 
submitButton.click()

#while True:

for i in range(1,3):
    
    print("Processing results page {}".format(i))
    
    #Finding the table with XPath
    parcelsTable = browser.find_elements_by_xpath("//table[1]/tbody/tr[2]/td/table[5]/tbody/tr")
    parcelsCount = len(parcelsTable)

    for i in range(1, parcelsCount):
        parcelRow = browser.find_element_by_xpath("//table[1]/tbody/tr[2]/td/table[5]/tbody/tr[{}]".format(i+1))
        parcelIdCell = parcelRow.find_element_by_xpath(".//td[1]")
        if parcelIdCell is not None:
            parcelId = parcelIdCell.text
            if (parcelId[0:3] >= endParcel):
                browser.close()
                os._exit(0)

            print(parcelId)
            parcelIdCell.click()
            root = browser.find_element_by_xpath("//*")
            source = root.get_attribute("outerHTML")

            f = open('{}/{}.html'.format(outDir, parcelId), 'w+')
            f.write(source.encode('utf-8'))
            f.close()
            backButton = browser.find_element_by_name("backbtn")
            backButton.click()
           
    nextButton = browser.find_element_by_name("nextbtn")
    nextButton.click()
