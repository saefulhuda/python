import crud, mysql.connector, faker

class Mode:

	def __init__(self, name, email, password):
		self.name 		= name
		self.email 		= email
		self.password 	= password

		self.db = mysql.connector.connect(
			host='localhost',
			user='root',
			passwd='',
			database='oomph'
			)


	def dos(self):
		insert = crud.insert(self.db, self.name, self.email, self.password, 2)
		print(insert)
		if insert > 0:
			return 'Success'

	def mah(self):
		crud.insert(self.db, self.name, self.email, self.password, 1)

fake = faker.Faker()
for i in range(50):
	mode = Mode(fake.name(), fake.email(), fake.name())
	print(mode.dos())