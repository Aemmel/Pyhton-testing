__author__ = 'Emil Donkersloot'

import copy

class DataBase:
	"""Till now very limited, only the first prototype"""
	def __init__(self, path):
		self.path = path
		self.file = self.loadFile(path)
		self.list = []
		self.loadDB()

	def loadFile(self, path):
		"""open a file from path for reading and writing"""
		return open(path, 'r+')

	def printFile(self):
		"""print the raw file"""
		print(self.file.read())

	def loadDB(self):
		"""Load the database from the file and put it in self.list"""
		line = {
			'name': "",
			'age': int,
			'country': "",
			'sex': bool # == is Male. if sex == true sex == male, if sex == false sex == female
		}

		var_from = 0
		var_to = 0

		for x in self.file:
			var_from = x.find(":") + 1
			var_to = x.find("!")
			line['name'] = x[var_from:var_to]

			var_from = x.find(":", var_from) + 1
			var_to = x.find("!", var_from)
			line['age'] = int(x[var_from:var_to]) #error handling needed

			var_from = x.find(":", var_from) + 1
			var_to = x.find("!", var_from)
			line['country'] = x[var_from:var_to]

			var_from = x.find(":", var_from) + 1
			var_to = x.find("!", var_from)
			line['sex'] = x[var_from:var_to].lower() == "male" #error handlig needed

			self.list.append(copy.deepcopy(line))


	def searchForName(self, name):
		"""get the line by searching for the name"""
		pass

	def printDB(self):
		"""print the DB in the following order: name, age, country, sex"""
		for x in self.list:
			print("Name: " + x['name'], end=' ')
			print("Age: {}".format(x['age']), end=' ')
			if x['sex']:
				print("Sex: male", end=' ')
			else:
				print("Sex: female", end=' ')
			print("Country: " + x['country'])



def main():
	db = DataBase("C:/Users/Emil Donkersloot/Desktop/db_1.txt") #load the file
	db.printDB() #print the whole database  (not raw)


if __name__ == '__main__':
	main()
