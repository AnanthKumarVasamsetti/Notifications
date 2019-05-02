from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import requests
import time

def scrape():
    now = datetime.now()
    today_12PM = now.replace(hour=13, minute=30, second=0)
    bse_df = pd.DataFrame()
    counter = 0

    while(now < today_12PM):
        page_link = "https://www.moneycontrol.com/india/stockpricequote/computers-software/tataconsultancyservices/TCS"
        page_response = requests.get(page_link)

        page_content = BeautifulSoup(page_response.content, 'html.parser')
        bse_value = page_content.find_all("span", id = "Bse_Prc_tick")[0].text
        bse_df = bse_df.append({'time': time.strftime("%H:%M:%S"), 'value': bse_value}, ignore_index=True)
        counter = counter + 1

        print(now)
        print(bse_value)
        print("============================")
        time.sleep(2)
        now = datetime.now()

    print("=========== Scarping finished ====================")
    bse_df.to_csv('BSE_data.csv')

scrape()