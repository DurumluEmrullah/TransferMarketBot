from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import csv


driver=webdriver.Chrome()

#url="https://twitter.com/search?q=lang%3Atr%20until%3A2020-09-22%20since%3A2020-07-01%20%23transfer&src=typed_query"
url ="https://www.transfermarkt.com"
driver.get(url)
dosya = open ("futbolcuTest.txt","r",encoding="utf-8")
futbolcuAdlari=dosya.readlines()
file =open("denemeler.csv","w",encoding="utf-8")
writer=csv.writer(file)
writer.writerow(["Ad","Kulubu","Degeri"])
driver.maximize_window()
tikla =driver.find_element_by_css_selector(".icon-detailsuche")



i=0
while i<len(futbolcuAdlari):
   # print(futbolcuAdlari[i])

    
    
    searchInput=driver.find_element_by_name("query")
    searchInput.send_keys(futbolcuAdlari[i])
    #searchInput.send_keys(Keys.ENTER)
    #searchInput.clear()
   
    
    pageSource =driver.page_source
    soup=BeautifulSoup(pageSource,"html.parser")
    futbolcu =tweets=soup.find_all("tr",attrs={"class":"odd"})
    for element in futbolcu:
        try:
            adi=element.find("a",attrs={"class":"spielprofil_tooltip tooltipstered"}).text
            kulubu=element.find("a",attrs={"class":"vereinprofil_tooltip tooltipstered"}).text
            degeri=element.find("td",attrs={"class":"rechts hauptlink"}).text
            writer.writerow([adi,kulubu,degeri])
            print(adi)
            print(kulubu)
            print(degeri)
            
        except:
            print("Hata var !!")
    

    driver.get(url)
    time.sleep(1)
    i+=1
    #result = driver.find_elements_by_xpath("//*[@id='yw0']/table/tbody/tr[1]/td[1]/table")
    #result= driver.find_elements_by_css_selector(".items tbody .odd .inline-table td.hauptlink a")
    #resultValue = driver.find_elements_by_css_selector(".items tbody .odd .rechts.hauptlink")
    #resultTeam =driver.find_elements_by_css_selector(".items tbody .odd .inline-table a.vereinprofil_tooltip.tooltipstered")
    #for element in result:
    #    f.write(element.text +"\n")

    #for element2 in resultValue:
    #    print(element2.text)

    #for element3 in resultTeam:
    #    print(element3.text)
    #a=0
    #while a < len(result):
    #    a+=1
    #    f.write(result.pop(0).text +"\t"+resultTeam.pop(0).text+"\t"+resultValue.pop(0).text+"\n")



driver.close()