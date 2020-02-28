import mysql.connector

db = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "",
	database = "oomph"
	)
if db.is_connected():
	print("Tehubung ke database")
else:
	print("Gagal terhubung")