import csv 

data = {}
user={}
userLiking={}
genres=set([])

def get() :
	global data
	global genres
	with open("bookdbfinal2.csv") as db:
		reader = csv.DictReader(db)
		for row in reader:
			key = row['book_id']
			rowData = {"author_name":row['author_name'],"author_movement":row['author_movement'],"genre":row['genre'],"abstract":row['abstract'],"Avg_rating":row['Avg_Rating']}
			genres.add(row['genre'])
			value = rowData
			data[key] = value

def getUser() :
	global user
	with open("userCSV.csv") as db:
		reader = csv.DictReader(db)
		for row in reader:
			key = row['user_id']
			if not user.has_key(key):
				user[key]={}
			rowData = {row['genre']:row['like']}
			value = rowData
			#print user[key]
			user[key].update(value)
	for i in range(1, len(user)+1):
		key = str(i)
		for g in genres:
			if not user[str(i)].has_key(g):
				value = {g:0}
				user[key].update(value)
		#sorting genre-liking dictionary by key
		user[key]=sorted(user[key].items())


def getUserLiking():
	global userLiking
	for i in range(1, len(user)+1):
		temp=[]
		key = str(i)
		for l in user[key]:
			temp.append(int(l[1]))
		value={key:temp}
		userLiking.update(value)					

get()
getUser()
getUserLiking()
#print data['1']['genre']
#print len(user[str(1)])    --> Prints 194 i.e user 1 has 194 genres as we wanted
#print user
#print 'Absurdism' in user[str(1)]
print user
