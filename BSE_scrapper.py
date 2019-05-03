from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import requests
import time
import logging as log
import os

from scratch_pad import insert_into_db
from scratch_pad import close_db
from protocols import clean_slate_protocol

log.basicConfig(filename='example.log',level=log.DEBUG)

def scrape(environ, resp):
    print(environ)
    print("===============================================")
    print(resp)
    now = datetime.now()
    time_at_10AM = now.replace(hour=10, minute=00, second=0)
    time_at_6PM = now.replace(hour=18, minute=00, second=0)
    bse_df = pd.DataFrame()
    counter = 0
    sleep_time_inteval = 2
    page_link = "https://www.moneycontrol.com/india/stockpricequote/computers-software/tataconsultancyservices/TCS"
    
    while(now < time_at_10AM):
        now = datetime.now()
        time.sleep(sleep_time_inteval)

    while(now < time_at_6PM):
        page_response = requests.get(page_link)

        page_content = BeautifulSoup(page_response.content, 'html.parser')
        bse_value = page_content.find_all("span", id = "Bse_Prc_tick")[0].text
        
        bse_df = bse_df.append({'time': time.strftime("%H:%M:%S"), 'value': bse_value}, ignore_index=True)
        
        curr_time = time.strftime("%H:%M:%S")
        
        now = datetime.now()
        #log.info("Inserting for time: ",curr_time)
        print("Inserting for time: ",curr_time)
        insert_into_db((curr_time, bse_value))
        
        time.sleep(sleep_time_inteval)

    print("=========== Scarping finished ====================")
    close_db()
    bse_df.to_csv('BSE_data.csv')

#scrape()