import matplotlib.pyplot as plt
import pandas as pd
import psycopg2
import os

def plotter():
    data = pd.read_csv('BSE_data.csv')
    data.plot(x='time', y='value')
    plt.show()

DATABASE_URI = 'postgres://bcsfswascxclov:93f19fe5cc89caddc6076b791f89d406acba6ce49230aa710c030bb4781481db@ec2-54-243-241-62.compute-1.amazonaws.com:5432/d32qpicp4tcgir'
conn = psycopg2.connect(DATABASE_URI, sslmode='require')
print('This is from scrapper file: ',os.environ['DATABASE_URL'])
#conn.query('INSERT INTO bse_trade (time, price) values ("01:00:00", 1234.00)')

def insert_into_db(data_time_price):
    sql = """INSERT INTO bse_trade(time, price) VALUES(%s,%s);"""
    try:
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, data_time_price)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def close_db():
    try:
        conn.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

