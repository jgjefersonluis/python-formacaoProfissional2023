import psycopg2
con = psycopg2.connect(host='database-1.cuf8rlopzxtf.us-east-1.rds.amazonaws.com', database='inventario',
                       user='postgres', password='12345678')
con.autocommit = True
cur = con.cursor()
cur.execute("delete from arquivos" )
con.commit()
con.close()
