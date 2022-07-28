from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':


		login_session['quote'] = request.form['quote']
		login_session['author'] = request.form['author']
		login_session['age'] = request.form['age']

		# quote = {'quote': 'your quote:'}
		# x = requests.post(userquote = quote)
		# print(x.text)
		# name = {'name': 'the author:'}
		# x = requests.post(username= name)
		# print(x.text)
		# age = {'age': 'hisage:'}
		# x = requests.post(userage = age)
		# print(x.text)
		try:

		    quote = login_session['quote']
		    author= login_session['author']
		    age = login_session['age']
		    return redirect(url_for('thanks'))
		except:
		    print('try again')
		    return redirect(url_for('home'))
	else: 
		return render_template('home.html')




@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():
    return render_template('display.html', quote = login_session['quote'], author = login_session['author'], age = login_session['age']) 



@app.route('/thanks')
def thanks():
	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True)