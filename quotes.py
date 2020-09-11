from flask import Flask ,render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:W1ndemere@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://pgqtzvahbtfjmi:adba77d538c1fbd7141ce1cfa14895e43223308cd6a81e001fe75e4601a3cfb9@ec2-34-251-118-151.eu-west-1.compute.amazonaws.com:5432/d7085s3m5rv715'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

class Favquotes(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	author = db.Column(db.String(30))
	quote = db.Column(db.String(2000))

@app.route('/')
def index():
    result = Favquotes.query.all()
    return render_template('index.html', result=result)

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/process', methods=['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata = Favquotes(author=author, quote=quote)
    db.session.add(quotedata)
    db.session.commit()

    return redirect(url_for('index'))

    #signature =Favquotes(author=author, quote=quote)
    #db.session.add(signature)
    #db.session.commit()
