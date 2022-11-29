import requests
from bs4 import BeautifulSoup
import re

#create base url and cases
base_url = "https://www.cnn.com"
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
    #generate year_url
    year_url=base_url+str(ytext)
    year_page = requests.get(year_url)
    # get all month urls per year
    year_soup = BeautifulSoup(year_page.content, "html.parser")
    # print(ytext)
    # print(year_soup)
    month_block=year_soup.find("ul", class_="sitemap-month")
    # print(month_block)
    month_links=month_block.find_all("a")

    for link in month_links:
        href=link.get("href")
        month_hrefs.append(str(href))
    #loop through months to collect data
    for mtext in month_hrefs:
        #generate month_url
        month_url=base_url+str(mtext)
        month_page = requests.get(month_url)
        # get all month urls per year
        month_soup = BeautifulSoup(month_page.content, "html.parser")
        # print(month_soup)
        headline_block=month_soup.find_all("div", class_="sitemap-entry")[1]
        # print(headline_block)

        indv_headlines=headline_block.find_all("li")
        for item in indv_headlines:
            print(f'{str(item.find("span",class_="date").string)},{str(item.find("span",class_="sitemap-link").string)}')
            d=headline_date.append(str(item.find("span",class_="date").string))
            h=headline.append(str(item.find("span",class_="sitemap-link").string))
#write data into csv
headline_data=open('headlines.csv', 'w')
headline_dates_data=open('headlines_dates.csv', 'w')
headline_data.write("CNN\n")
headline_dates_data.write("CNN\n")
for index in range(len(headline)):
    headline_data.write(headline[index]+"\n")
    headline_dates_data.write(headline_date[index]+"\n")
headline_data.close()
headline_dates_data.close()
