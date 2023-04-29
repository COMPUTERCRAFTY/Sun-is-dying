from bs4 import  BeautifulSoup
import requests
import time 
import csv

START_URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser= webdriver.Chrome("/path/to/chromedriver")
browser.get(START_URL)
time.sleep(10)
def scrape():
    headers = ["Name","Distance","Mass","Radius"]
    stars_data = []
    for i in range(0,99):
        soup=BeautifulSoup(browser.page_source,"html_parser")
        for trtags in soup.find_all("tr",attrs={"class":"stars"}):
            tdtags=trtags.find_all("td")
            temp_list=[]
            for index, tdtag in enumerate(tdtags):
                if index==0:
                    temp_list.append(tdtag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(tdtag.contents[0])
                    except:
                        temp_list.append("")
            stars_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/span[2]/a').click()

scrape()

