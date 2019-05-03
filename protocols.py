import psycopg2

def clean_slate_protocol():
    print("------------- WARNING THIS CAN EARSE THE ENTIRE DATABSAE -------------")
    user_descision = input("Are you sure [y/n]: ")

    if(user_descision.lower() == 'y'):
        try:
            DATABASE_URI = os.environ.get('DATABASE_URL') #'postgres://bcsfswascxclov:93f19fe5cc89caddc6076b791f89d406acba6ce49230aa710c030bb4781481db@ec2-54-243-241-62.compute-1.amazonaws.com:5432/d32qpicp4tcgir'
            conn = psycopg2.connect(DATABASE_URI, sslmode='require')

            sql_query = """DROP SCHEMA public CASCADE;
            CREATE SCHEMA public;
            """
            cur = conn.cursor()
            cur.execute(sql_query)
            cur.commit()
        except(Exception, psycopg2.DarabaseError) as error:
            print(error)
        finally:
            cur.close()
            conn.close()

        