from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import bcrypt
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///registrations.db'
db = SQLAlchemy(app)

#Creating db Model
class Registrations(db.Model):
    username = db.Column(db.String(length=50), nullable=False, unique=True, primary_key=True)
    email = db.Column(db.String(length=100), unique=True, nullable=False)
    password = db.Column(db.String(length=256), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)


@app.route("/")
@app.route("/login")
def index():
    return render_template('LogInPage.html')


@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        reg_name = request.form['Username']
        reg_pass = request.form['Pass']
        reg_id = request.form['id']

        hashed = bcrypt.hashpw(reg_pass.encode('utf-8'), bcrypt.gensalt())

        user = Registrations(username=reg_name, email=reg_id, password=hashed)    
        try:
            db.session.add(user)
            db.session.commit()
            return redirect('/home')
        except:
            return "There was an error in registration."
    else:
        return render_template('LogInPage.html')

# def register():
#     username = request.json.get('username', None)
#     email = request.json.get('email', None)
#     password = request.json.get('password', None)
#     if not username:
#         return "Missing Username", 400
#     if not email:
#         return "Missing email", 400
#     if not password:
#         return "Missing Password", 400

#     hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

#     user = User(username=username, email=email, password=hashed)

#     db.session.add(user)
#     db.session.commit()
    
#     return f'Welcome {username}'
# def login():


@app.route("/feedback")
def feedbackpage():
    items = [
        {'id'}
    ]
    return render_template('feedback.html', item_name="Yeah, here we go!")

@app.route("/statistics")
def statisticspage():
    return render_template('statistics.html')

@app.route("/home")
def homepage():
    return render_template('fakehomepage.html')

@app.route("/assessments")
def assessmentspage():
    return render_template('assessments.html')

@app.route("/contents")
def contentspage():
    return render_template('base2.html')

if __name__ == "__main__":
    app.run(debug=True)