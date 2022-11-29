import requests
from bs4 import BeautifulSoup
import re

#create base url and cases
base_url = "https://www.cnn.com/"
url = "https://www.cnn.com/sitemap.html"
page = requests.get(url)
site=[]
author_names=[]
headline=[]
headline_date=[]
year_hrefs=[]
# find page content
soup = BeautifulSoup(page.content, "html.parser")
# get all year urls
year_block=soup.find("ul", class_="sitemap-year")
year_links=year_block.find_all("a")

for link in year_links:
    href=link.get("href")
    year_hrefs.append(str(href))

#loop through years to collect data
for ytext in year_hrefs:
    month_hrefs=[]
    url=base_url+str(ytext)
    page = requests.get(url)
    # get all month urls per year
    month_block=soup.find("ul", class_="sitemap-month")
    month_links=month_block.find_all("a")

    for link in month_links:
        href=link.get("href")
        month_hrefs.append(str(href))
    #loop through months to collect data
    for mtext in month_href:
        headline_block=soup.find("li")
        headline_date.append(headline_block.find("span",class_="date").text)
        headline.append(headline_block.find("span",class_="sitemap-link").find("a").text)
#write data into csv    
headline_data=open('./date/headlines.csv', 'w')
headline_dates_data=open('./date/headlines_dates.csv', 'w')
for index in range(len(headline)):
    headline_data.write(headline[index]+"\n")
    headline_dates_data.write(headline_date[index]+"\n")
headline_data.close()
headline_dates_data.close()
