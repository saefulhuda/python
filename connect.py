import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="oomph"
)

if db.is_connected():
  print("Berhasil terhubung ke database")

  request = db.cursor() #prepare request ke db
  #create_table = "CREATE TABLE users (id int(11), name varchar(255), email varchar(255), password varchar(255))
  #insert = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
  # data = ("jaka", "jaka@email.com", "jaka")

  # request.execute(insert, data) #query execute
  show = "SELECT * FROM users"
  request.execute(show) #query execute
  # result = request.fetchall()
  # result = request.fetchone()
  result = request.fetchmany(2)
  for row in result:
  	print(row)
  # db.commit() #require DML dipakai jika eksekusi DDL insert, delete, update
  # print("{} data ditambahkan".format(len(data)))
  db.close()