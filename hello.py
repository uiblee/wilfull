import os
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def homepage():
	title = "Wilful.ly"
	paragraph = ["free, easy wills online"]
	
	return render_template("index.html", title = title, paragraph = paragraph)

@app.route('/about')
def aboutpage():
	
	title = "About Wilful.ly"
	paragraph = ["Everyone needs a will"]
	
	pageType = 'about'

	return render_template("index.html", title = title, paragraph = paragraph, pageType = pageType)

@app.route('/contact')
def contact():
	
	title = "Contact us"
	paragraph = ["uiblee@gmail.com"]
	
	pageType = 'about'

	return render_template("index.html", title = title, paragraph = paragraph, pageType = pageType)


if __name__ == "__main__":
	app.run(debug=True)
