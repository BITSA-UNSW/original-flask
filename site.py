from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/bitsamag')
def mag():
	return render_template('bitsamag.html')

@app.route('/getinvolved')
def get_involved():
	return render_template('getinvolved.html')

@app.route('/team')
def team():
	return render_template('ourteam.html')

@app.route('/past')
def past_events():
	return render_template('pastevents.html')

@app.route('/sponsors')
def sponsors():
	return render_template('sponsors.html')

@app.route('/upcoming')
def upcoming_events():
	return render_template('upcomingevents.html')

@app.route('/whatwedo')
def what_we_do():
	return render_template('whatwedo.html')

#running the app
#defaults to host on port 5000
if(__name__ == '__main__'):
	app.run(debug=True)