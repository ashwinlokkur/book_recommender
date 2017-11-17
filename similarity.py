# this generates a similarity matrix

import readers
import numpy as np
import math
import csv

n = len(readers.userLiking)

userLiking1 = {}
simMatrix = np.zeros((n,n))

for i in sorted(readers.userLiking.keys()):
	userLiking1[i] = ''.join(str(e) for e in readers.userLiking[i])

def getgenre(user1):
	genre = set();
	with open('userCSV.csv') as f:
		read = csv.reader(f);
		#print(read)
		for row in read:
			if(row[0] == 'user_id'):
				continue;
			if(int(row[0]) == int(user1)):
				genre.add(row[2]);
			
	return genre;
			
		
def recommendbook(genre , user2):
	  
	books = []
	with open('bookdbfinal2.csv') as f:
		reader = csv.reader(f)
		for row in reader:
			if(row[5]== genre):
				books.append(row)
		
	books = sorted(books , key = lambda x : float(x[-1]))
	if(len(books) > 0):
		print "      " + books[0][2] ;
	

def dif(i,j):
	m = len(userLiking1[i])
	diff = 0
	for k in range(m):
		diff += (int(userLiking1[i][k]) - int(userLiking1[j][k]))**2
	return math.sqrt(diff)

def similarityMatrix():
	for i in sorted(readers.userLiking.keys()):
		for j in sorted(readers.userLiking.keys()):
			simMatrix[int(i)-1,int(j)-1] = (dif(i,j))/9.7 	
	np.set_printoptions(precision=2)		
	print simMatrix

similarityMatrix()

ip = raw_input("What user do you want to find similarity to? please eneter between 1 and "+ str(n) +"\n")
 
if ip not in readers.userLiking.keys():
	print("INVALID INPUT")


k = (sorted(readers.userLiking.keys()))
k.remove(ip)

y = "" 
x = 1
for i in k:
	if(x > simMatrix[int(ip)-1,int(i)-1]):
		x = simMatrix[int(ip)-1,int(i)-1]
		y = i

print("user "+ip+" is similar to user "+y);
print

def getbooks(user1,user2):
	gen = getgenre(user2);
	print "Recommended books from user "+user2+" :"
	for i in gen:
		recommendbook(i,user2);
getbooks(ip , y);
		



	
