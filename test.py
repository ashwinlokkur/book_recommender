from flask import Flask
from flask import render_template,request
import csv
# import similarity

app = Flask(__name__)

top_10 = ['Adventure','Biography','Comedy','Drama','Fiction','History','Literature','Mythology','Suspense','Thriller']
genres = []
sel = [1,2,3,4,5]
selected_genres =[]

with open("bookdbfinal2.csv") as db:
		reader = csv.DictReader(db)
		for row in reader:
			m = row['genre'].decode("utf-8")
			if m not in genres:
				genres.append(m)		

@app.route('/', methods =['GET','POST'])
def generate():
    return render_template('index.html',genres=genres, top_10 =top_10,sel = sel)


@app.route("/forward/", methods=['GET','POST'])
def foo():

	for i in range(5):
		n = "top"+str(i+1)
		selected_genres.append(request.form[n])

	for i in range(2):
		n = "genres"+str(i+1)
		selected_genres.append(request.form[n])	
	print selected_genres	
	return render_template('index.html',genres=genres, top_10 =top_10,sel = sel)
		
	

if __name__ == '__main__':
    app.run(debug = True, port = 5000)


