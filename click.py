import mysql.connector
import time
f = open('py-connect.txt','r')
v = f.read()
cnx = mysql.connector.connect(user='root', password='0000',
                              host='127.0.0.1',
                              database='seabattles')
restart = 0;
try:
   print("in try")
   while (restart == 0):
      print("in while")
      cursor = cnx.cursor()
      cnx.autocommit=True
      #cnx.autocommit(True)# for Python 3+
      cursor.execute("""
         select * from server
      """)
      print("in for")
      result = cursor.fetchall()
      for row in result:
          speed=row[1]
          if speed != speed:
              speed = speed
          print(speed)
      restart = 1        
finally:
    cnx.close()    
print("hello")
print(v)
