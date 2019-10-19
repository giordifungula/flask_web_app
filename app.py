from flask import Flask, render_template, request
from flask_sqlalchemy import flask_sqlalchemy;

ENV = 'dev'
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postresql://postgress:127.0.0.1@localhost/lexus'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_DATABASE_URI'] = False

app = Flask(__name__)

db = SQLAlchemy(app)

class Feedback(db.Models):
    __tablename = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.Text(200), unique=True)
    dealer = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, customer, dealer, rating, comments):
        self.customer = customer
        self.dealer = dealer
        self.rating = rating
        self.comments = comments


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        if customer == '' or dealer == '':
            return (render_template('index.html', message='Please enter required fields'))

        print(customer, dealer, rating, comments)
        return (render_template('success.html'))

if __name__ == '__main__':
    app.debug = True 
    app.run()
    # want to keep running on developement
