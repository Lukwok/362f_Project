import mysql.connector

def database(query):
  db = mysql.connector.connect(user='root',password='root',
                              host='127.0.0.1',database='362f')
  print("Connect to Database Sucessful")
  cursor = db.cursor()
  cursor.execute(query)
  data = cursor.fetchall()
  cursor.close()
  db.commit()
  return data
