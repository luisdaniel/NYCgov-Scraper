from BeautifulSoup import BeautifulSoup
import re
import urllib2
import json
import csv
import requests
from requests.exceptions import HTTPError

csvwriter = csv.writer(open("pressReleaseLinksRestoreAbandoned.csv", "w"))
csvwriter.writerow(["year", "url"])
blogLinks = []

baseURL  = "http://www.nyc.gov/html/om/html/"


start = [170, 180, 173, 257, 228, 221, 258, 304, 295, 235, 250, 149] #b starts here
end = [345, 379, 366, 501, 455, 486, 512, 568, 530, 460, 493, 149]
for i in range(2002, 2014):
	l = start[i - 2002]
	u = end[i - 2002]
	#-----------------------------A-----------------
	variant = "a/"
	for j in range(1, l +1):
		prNum = "pr" + str(j).zfill(3) + "-" + str(i-2000).zfill(2) + ".html"
		url = baseURL + str(i)+variant + prNum
		try: 
			page = urllib2.urlopen(url).read()
		except:
			continue
		print url
		page = urllib2.urlopen(url).read()
		soup = BeautifulSoup(page)
		content = soup.findAll(['p'])
		text = ''
		for node in content:
			text += ''.join(node.findAll(text=True))
		if 'restore' in text.lower() and 'abandon' in text.lower():
			year = str(i)
			print "Adding: " + url
			newRow = [year, url]
			csvwriter.writerow(newRow)

	#---------------------B-------------------
	variant = "b/"
	for j in range(l, u+1):
		prNum = "pr" + str(j).zfill(3) + "-" + str(i-2000).zfill(2) + ".html"
		url = baseURL + str(i)+variant + prNum
		try: 
			page = urllib2.urlopen(url).read()
		except:
			continue
		print url
		page = urllib2.urlopen(url).read()
		soup = BeautifulSoup(page)
		content = soup.findAll(['p'])
		text = ''
		for node in content:
			text += ''.join(node.findAll(text=True))
		if 'restore' in text.lower() and 'abandon' in text.lower():
			year = str(i)
			print "Adding: " + url
			newRow = [year, url]
			csvwriter.writerow(newRow)			

