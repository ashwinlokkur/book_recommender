import csv
def recommendbook(genere , user):
	books = []
	with open('bookdbfinal2.csv') as f:
		reader = csv.reader(f)
		for row in reader:
			if(row[5]== genere):
				books.append(row)
		
	books = sorted(books , key = lambda x : float(x[-1]))	
	print(books[0]);

recommendbook('Adventure'," ")	
	
