import csv 

data = {}

def fill() :
	with open("bookdbfinal2.csv") as db:
		reader = csv.DictReader(db)
		for row in reader:
			key = row['book_id']
			value = row['Avg_Rating']
			data[key] = value

fill()
# print(data)	