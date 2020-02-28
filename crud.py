import os
import hashlib
import mysql.connector

db = mysql.connector.connect(
	host='localhost',
	user='root',
	passwd='',
	database='oomph'
	)

def insert(db):
	nama		= input("Masukan nama : ")
	email		= input("Masukan email : ")
	passw 		= input("Masukan password : ")
	password	= hashlib.md5(passw.encode('utf-8')).hexdigest()
	value 	= (nama, email, password)
	request = db.cursor()
	insert 	= "INSERT INTO users (name, email, password) VALUE (%s, %s, %s)"
	request.execute(insert, value)
	db.commit()
	print("{} data berhasil disimpan". format(request.rowcount))

def  read(db):
	request = db.cursor()
	select = "SELECT * FROM users"
	request.execute(select)
	result = request.fetchall()
	if request.rowcount > 0:
		for row in result:
			print(row)
	else:
		print("Data not found")

def update(db):
	iD = input("ID>")
	nama 		= input("Masukan nama : ")
	email 		= input("Masukan email : ")
	passw 		= input("Masukan password : ")
	password 	= hashlib.md5(passw.encode('utf-8')).hexdigest()
	request = db.cursor()
	update 	= "UPDATE users SET name=%s, email=%s, password=%s WHERE id=%s"
	value 	= (nama, email, password, iD)
	request.execute(update, value)
	db.commit()
	print("{} data berhasil di update".format(request.rowcount))

def delete(db):
	iD = input("ID>")
	request = db.cursor()
	delete = "DELETE FROM users WHERE id=%s"
	value = (iD,)
	request.execute(delete, value)
	db.commit()
	print("Data berhasil dihapus")

def search(db):
	key = input("Key : ")
	request = db.cursor()
	search = "SELECT * FROM users WHERE name=%s OR email=%s"
	value = (key, key)
	request.execute(search, value)
	result = request.fetchall()
	for row in result:
		print(row)

def menu(db):
	print("=== APLIKASI CRUDS PYTHON ===")
	print("1. Create ")
	print("2. Read ")
	print("3. Update ")
	print("4. Delete ")
	print("5. Search ")
	print("0. Keluar ")
	print("--------------------")

	select = input("Pilih menu>")

	os.system("cls")

	if select == "1":
		insert(db)
	elif select == "2":
		read(db)
	elif select == "3":
		update(db)
	elif select == "4":
		delete(db)
	elif select == "5":
		search(db)
	elif select == "0":
		exit()
	else:
		print("Invaild select menu")

if __name__=="__main__":
	while (True):
		menu(db)