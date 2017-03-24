import mysql.connector
import time
f = open('py-connect.txt','r')
v = f.read()
cnx = mysql.connector.connect(user='root', password='0000',
                              host='127.0.0.1',
                              database='seabattles')
restart = 0;
try:
   #print("in try")
   while (restart == 0):
      #print("in while")
      cursor_serv = cnx.cursor()
      cnx.autocommit=True
      query_serv = """
         select * from server
      """ 
      cursor_serv.execute(query_serv)
      result_serv = cursor_serv.fetchall()
      for row_serv in result_serv:
          #restart=row[1]
          if restart != row_serv[1]:
              restart = row_serv[1]
              print(restart)

      cursor_players = cnx.cursor()
      #cnx.autocommit=True
      query_players = """
         select * from players
      """
      cursor_players.execute(query_players)
      result_players = cursor_players.fetchall()
      for row_players in result_players:
          gold=row_players[3]+1
          print(gold)
          query_player_update = """
             UPDATE players SET gold=%s WHERE player_id=%s
          """
          t = (gold, row_players[0])
          cursor_players.execute(query_player_update, t)
           #update players set gold=
      #restart = 1        
finally:
    cnx.close()
print("server has been stopped")

