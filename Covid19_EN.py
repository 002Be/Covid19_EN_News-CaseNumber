#Import
import re
import time
import urllib
import requests
from os import remove
from bs4 import BeautifulSoup

def covidCaSeDataShooting():
    #File
    file = open("KoronaCase.txt","a",encoding="utf-8")
    #Website
    url = 'https://news.google.com/covid19/map?hl=en-US&gl=US&ceid=US%3Aen'
    html = requests.get(url).content
    soup = BeautifulSoup(html, "html.parser")
    list = soup.find_all("tr",{"class":"sgXwHf wdLSAe YvL7re"})
    list2 = soup.find_all("div",{"class":"UvMayb"})
    l1 = list2[0].text
    l2 = list2[1].text
    l3 = list2[2].text

    print(f"\nIn the whole world: Total number of cases {l1} | Number of new cases (14 days) {l2} | Number of deaths {l3}\n")

    #Search on the site 
    for i in list:
        #Country name
        countryName = i.find("div",{"class":"pcAJd"})
        countryName = countryName.text

        #Number of sick people
        totalNumberOfCases = i.find_all("td")
        t1 = totalNumberOfCases[0].text
        t2 = totalNumberOfCases[1].text
        t3 = totalNumberOfCases[-2].text
        t4 = totalNumberOfCases[-1].text

        #Record
        file.write(f"{countryName} | Total number of cases: {t1} | New cases: {t2} | Number of cases per 1 million people: {t3} | Number of deaths: {t4} \n")
    file.close()

    print("Press the 'q' key to exit.")

    #Search
    while True:
        searchFile = open("KoronaCase.txt", "r", encoding ="utf-8")
        searchWanted = input("Enter the country you want to search ➢  ").capitalize()
        searchWantedIsThere = searchFile.read().find(searchWanted)
        searchFile.close()
        if searchWantedIsThere != -1:
            searchFile1  = open("KoronaCase.txt", "r", encoding ='utf-8')
            searchS = searchFile1.read()
            searchItems = re.findall(searchWanted+".*$",searchS,re.MULTILINE)
            searchFile1.close()
            for searchX in searchItems:
                print(searchX,"\n")
        elif searchWanted == "Q":
            break
        else:
            print("Incorrect country name!\n")
    remove("KoronaCase.txt")

def covidNewsDataShooting():
    url = 'https://news.google.com/rss/search?q=kovid+19&hl=en-US&gl=US&ceid=US:en'
    decomposition = urllib.request.urlopen(url)
    page = decomposition.read()
    decomposition.close()
    pageData = BeautifulSoup(page,"xml")
    source = pageData.findAll("item")

    timeSettings = int(input("Set how many seconds the news will remain on the screen ➢  "))

    for information in source:
        newsTime = information.pubDate.text
        newsTitle = information.title.text
        newsLink = information.link.text
        newsBracket = 100 * "▁"
        time.sleep(timeSettings)
        print(f"News headline: {newsTitle} \nNews time: {newsTime} \nNews link: {newsLink} \n {newsBracket} \n")

while True:
    select = input("1- News about Covid 19 \n2- Number of covid 19 cases by country \n3- Exit\n\n ➢  ")
    if select == "1":
        covidNewsDataShooting()
    elif select == "2":
        covidCaSeDataShooting()
    else:
        print("Exit")
        break