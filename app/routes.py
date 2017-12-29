from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username':'Chad'}
	posts = [
		{
			'author' : {'username': 'Harry'},
			'body' : 'Its snowing in Seattle!'
		},
		{
			'author' : {'username' : 'Jess'},
			'body' : 'Looking forward to Star Wars!'
		}
	]
	return render_template('index.html', title='Home', user=user, posts= posts)
