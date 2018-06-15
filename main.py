import requests
import re
from bs4 import BeautifulSoup

def getOfferList:
	
	page = requests.get("https://www.americanexpress.com/au/network/shopping.html")

	soup = BeautifulSoup(page.content, 'html.parser')

	offerList = []

	for elem in soup.find_all('a', href=re.compile("offer=")):
		offerList.append(elem['trackingid'])
	
	return offerList

def getOfferDetails:
	
	offerTitles = []
	offerDescriptions = []

	for i in offerList:
		page = requests.get("https://www.americanexpress.com/au/network/shopping/doe-offer-detail.html?offer=" + i)
		soup = BeautifulSoup(page.content, 'html.parser')
		print(soup)
		print("-------------------------------------------------------------------")








def main():

	offerList = getOfferList

	getOfferDetails(offerList)