import connection

db = connection.db
limit = 20

def delete_queue(id):
	request = db.cursor()
	query = "DELETE FROM queue WHERE id=%s"
	value = (id,)
	req = request.execute(query, value)
	db.commit()
	if req:
		return 1
	else:
		return 0

def insert_premium(row):
	request = db.cursor()
	query = "INSERT INTO log_premium (msisdn, price) VALUES (%s, %s)"
	value = (row[1], row[4])
	request.execute(query, value)
	req = db.commit()
	if req:
		return 1
	else:
		return 0

def insert_log(row):
	request = db.cursor()
	query = "INSERT INTO log (msisdn, price) VALUES (%s, %s)"
	value = (row[1], row[4])
	req = request.execute(query, value)
	db.commit()
	if req:
		return 1
	else:
		return 0

def get_queue(limit):
	request = db.cursor()
	query 	= "SELECT * FROM queue"
	req = request.execute(query)
	data = request.fetchmany(limit)
	if request.rowcount > 0:
		for row in data:
			if row[4] <= 2000:
				insert = insert_log(row)
				if insert == 0:
					print("Success insert into log : ",row[1])
				else:
					print("Not good")
					delete_queue(row[0])
			else:
				insert = insert_premium(row)
				if insert == 0:
					print("Success insert into premium : ",row[1])
				else:
					print("Failed insert")
					delete_queue(row[0])
	else:
		print("Data not found")


get_queue(limit)
# delete_queue(msisdn)