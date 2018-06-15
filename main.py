import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver

def getOfferList():
	
	page = requests.get("https://www.americanexpress.com/au/network/shopping.html")

	soup = BeautifulSoup(page.content, 'html.parser')

	offerList = []

	for elem in soup.find_all('a', href=re.compile("offer=")):
		offerList.append(elem['trackingid'])
	return offerList

def getOfferDetails(offerList):
	
	offerCodes = []
	offerTitles = []
	offerDescriptions = []

	for i in offerList:
		offerCodes.append(i)
		page = requests.get("https://www.americanexpress.com/au/network/shopping/doe-offer-detail.html?offer=" + i)
		soup = BeautifulSoup(page.content, 'html.parser')
		
		for title in soup.find_all("h1", class_="supplier"):
			offerTitles.append(title.text.strip())

		for description in soup.find_all("div", class_="offer-details"):
			des = description.find('h2')
			offerDescriptions.append(des.text.strip())

	detailedOfferList = []
	detailedOfferList.append(offerCodes)
	detailedOfferList.append(offerTitles)
	detailedOfferList.append(offerDescriptions)

	return detailedOfferList

def selectOffers(detailedOfferList):

	print("The current active offers are:\n")
	
	for i in range(0,len(detailedOfferList[0])):
		print("Offer " + str(i + 1) + ":")
		print(detailedOfferList[1][i])
		print(detailedOfferList[2][i])
		print("\n")

	offerNumber = input("Please enter the number of the offer you would like to registers your cards for: ")

	offerID = detailedOfferList[0][int(offerNumber) - 1]

	return offerID

def registerCards(offerID)




def main():

	offerList = getOfferList()

	detailedOfferList = getOfferDetails(offerList)

	offerNumber = selectOffers(detailedOfferList)

	registerCards(offerID)



main()