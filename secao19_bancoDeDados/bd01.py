import psycopg2
con = psycopg2.connect(host='database-1.cuf8rlopzxtf.us-east-1.rds.amazonaws.com', database='postgres',
                       user='postgres', password='12345678')
cur = con.cursor()
con.close()
