# this generates a similarity matrix

import readers
import numpy as np
import math

n = len(readers.userLiking)

userLiking1 = {}
simMatrix = np.zeros((n,n))

for i in sorted(readers.userLiking.keys()):
	userLiking1[i] = ''.join(str(e) for e in readers.userLiking[i])

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
	print simMatrix

similarityMatrix()

ip = raw_input("What user do you want to find similarity to? please eneter between 1 and "+ str(n) +"\n")
 
if ip not in readers.userLiking.keys():
	print("invalid input")


k = (sorted(readers.userLiking.keys()))
k.remove(ip)

y = "" 
x = 1
for i in k:
	if(x > simMatrix[int(ip)-1,int(i)-1]):
		x = simMatrix[int(ip)-1,int(i)-1]
		y = i

print("user "+ip+" is similar to user "+y)		