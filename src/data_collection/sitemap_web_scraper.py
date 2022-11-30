from bs4 import BeautifulSoup
import requests
import langdetect

error_count=0
base_urls = ["https://www.foxnews.com/sitemap.xml","https://www.washingtonpost.com/wp-stat/sitemaps/index.xml","https://www.bbc.com/sitemaps/https-index-com-archive.xml"]
site=[]
author_names=[]
headline=[]
headline_date=[]
year_hrefs=[]

for url in base_urls:
    print(f"{url.split('.')[1]}\n")
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

        for index in range(len(submap_urls)):
            submap=submap_urls[index]
            date=submap_dates[index]
            if submap!=None:
                submap=submap.string.replace('amp;', '')
                # print(submap)
                page_r = requests.get(submap)
                page_soup = BeautifulSoup(page_r.content, 'html.parser')
                try:
                    if langdetect.detect(page_soup.find("h1").string)!="en":
                        print("skipped")
                        continue
                except langdetect.lang_detect_exception.LangDetectException:
                    print("skipped")
                    continue
                else:
                    headline.append(page_soup.find("h1").string)
                    headline_date.append(date.string[0:9])
                    print(f'{date.string[0:9]},{page_soup.find("h1").string}')
    dir_path = os.path.dirname(os.path.realpath(__file__))
    headline_data=open(dir_path+f"/data/{url.split('.')[1]}_headlines.csv", 'w')
    headline_data.write(f"{url.split('.')[1]}\n")
    for index in range(len(headline)):
        headline_data.write(headline_date[index])
        headline_data.write(headline[index]+"\n")
    headline_data.close()
    print(f"done {url}")
