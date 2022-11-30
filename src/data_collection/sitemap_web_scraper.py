from bs4 import BeautifulSoup
import requests

error_count=0
base_urls = ["https://www.foxnews.com/sitemap.xml"]
site=[]
author_names=[]
headline=[]
headline_date=[]
year_hrefs=[]

for url in base_urls:
    r = requests.get(url)
    xml = r.text
    soup = BeautifulSoup(xml,"xml")
    sitemap_urls = soup.find_all("loc")
    for sitemap in sitemap_urls:
        sitemap=sitemap.string.replace('amp;', '')
        print(sitemap)
        if "type=articles&" not in sitemap:
            continue
        submap_r = requests.get(sitemap)
        submap_xml = submap_r.text
        submap_soup = BeautifulSoup(submap_xml,"xml")
        submap_urls = submap_soup.find_all("loc")
        submap_dates=submap_soup.find_all("lastmod")
        print(f"{len(submap_urls)}")
        print(f"{len(submap_dates)}")

        for (submap, date) in (submap_urls,submap_dates):
            submap=submap.string.replace('amp;', '')
            page_r = requests.get(submap)
            page_soup = BeautifulSoup(page_r,"xml")
            headline.append(page_soup.find("h1",class_="header").string)
            headline_date.append(date.string[0:9])
            print(f'{date.string[0:9]},{page_soup.find("h1",class_="header").string}')
