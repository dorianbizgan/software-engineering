from flask import Flask, render_template, request, redirect, url_for, jsonify, json
import random
app = Flask(__name__)

books = [{'title': 'Software Engineering', 'id': '1'}, \
		 {'title': 'Algorithm Design', 'id':'2'}, \
		 {'title': 'Python', 'id':'3'}]


@app.route('/book/JSON')
def bookJSON():
	r = json.dumps(books)
	return (r)


@app.route('/')
def homepage():
	return(render_template("showPage.html", books=books))

####################
@app.route('/book/')
def showBook():
	return("showBook function")
####################


@app.route('/book/new/', methods=['GET', 'POST'])
def newBook():


	data = request.form.get('book_name', None)
	new_id = 0
	unique = False

	if request.method == "GET":
		return(render_template("newBook.html"))

	if request.method == "POST":
		while unique == False:
			for i in books:
				if int(i['id']) == int(new_id):
					new_id += 1
					break
				else:
					if i == books[-1]:
						unique = True
		books.append({'title':data, 'id':new_id})
		return(redirect(url_for('homepage')))


	print(request.method)
	if request.method == "GET":
		return(render_template("newBook.html"))


@app.route('/book/<int:book_id>/edit/', methods=['GET','POST'])
def editBook(book_id):
	book = None
	data = request.form.get('book_name', None)
	for i in books:
		print(i)
		print(book_id)
		print(int(i['id']) == int(book_id))
		print(request.method)
		if int(i['id']) == int(book_id):
			book = i
			print("THIS IS THE BOOK NAME",book)
	print(request.method)
	if request.method == "GET":
		return(render_template("editBook.html", book=book))

	print(data)
	if request.method == "POST":
		book['title'] = str(data)
		return(redirect(url_for('homepage')))

	
@app.route('/book/<int:book_id>/delete/', methods = ['GET', 'POST'])
def deleteBook(book_id):
	book = None
	for i in books:
		print(i, "full book detail")
		print(i['id'], "book id name in dictionary")
		print(book_id, "given book id to look for")
		print(int(book_id) == int(i['id']))
		if int(book_id) == int(i['id']):
			book = i

	if request.method == "GET":
		if book == None:
			return(redirect(url_for('homepage')))
		return(render_template("deleteBook.html", book=book))

	elif request.method == "POST":
		books.remove(book)
		return redirect(url_for('homepage'))


if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)
	

