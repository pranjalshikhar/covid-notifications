from plyer import notification
import requests
import time
from bs4 import BeautifulSoup

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "covid_icon.ico",
        timeout = 10
    )

def getData(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    while True:
        myHTMLData = getData('https://www.mohfw.gov.in/')

        soup = BeautifulSoup(myHTMLData,'html.parser')
        #print(soup.prettify())
        myDataStr = ""
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            myDataStr += tr.get_text()
        myDataStr = myDataStr[1:]
        itemList = myDataStr.split("\n\n")

        states = ['Maharashtra', 'Tamil Nadu', 'Delhi', 'Karnataka', 'Gujarat', 'Uttar Pradesh', 'Telangana',
                  'Andhra Pradesh', 'West Bengal', 'Rajasthan', 'Haryana', 'Bihar', 'Assam', 'Madhya Pradesh', 'Odisha',
                  'Jammu and Kashmir', 'Kerala', 'Punjab', 'Jharkhand', 'Chattisgarh', 'Uttarakhand', 'Goa', 'Tripura',
                  'Puducherry', 'Manipur', 'Himachal Pradesh', 'Ladakh', 'Nagaland', 'Chandigarh',
                  'Dadra and Nagar Haveli and Daman and Diu', 'Arunachal Pradesh', 'Meghalaya', 'Mizoram', 'Sikkim',
                  'Anadaman and Nicobar Islands']
        for item in itemList[0:34]:
            datalist = item.split('\n')
            if datalist[1] in states:
                print(datalist)
                nTitle = 'Cases of Covid-19 as of now'
                nText = f"State : {datalist[1]} \nTotal Cases : {datalist[5]}\nActive : {datalist[2]}\nCured : {datalist[3]}\nDeaths : {datalist[4]}"
                notifyMe(nTitle,nText)
                time.sleep(2)
        time.sleep(3600)  #change as required 60 value for 1 min
