import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
	try:
		return "Hello World!"
	except: Exception, e:
		return str(e)

if __name__ == "__main__"
	app.run()
