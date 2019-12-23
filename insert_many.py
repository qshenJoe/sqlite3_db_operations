import sqlite3

# cursor.execute('''CREATE TABLE STUDENT(
#   ID INT PRIMARY KEY NOT NULL,
#   NAME TEXT NOT NULL,
#   AGE INT NOT NULL,
#   MARKS INT);''')

def insert_multiple(db_name, data, sql):
  conn = sqlite3.connect(db_name)
  c = conn.cursor()
  print('Connection successfully established.')
  c.executemany(sql, data)
  conn.commit()
  conn.close()
  print('Connection successfully disconnected.')

def main():
  sql = 'INSERT INTO STUDENT VALUES(?,?,?,?);'
  db_name = 'my_database.sqlite'
  data = [
    (20191223005, 'Kevin', 21, 580),
    (20191223006, 'Emerald', 23, 560),
    (20191223007, 'Lucy', 22, 620),
    (20191223008, 'Jane', 20, 570)]
  insert_multiple(db_name, data, sql)

if __name__=="__main__":
  main()
