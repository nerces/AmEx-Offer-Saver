import requests
import re
from bs4 import BeautifulSoup

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

	print(detailedOfferList)









def main():

	offerList = getOfferList()

	getOfferDetails(offerList)

main()