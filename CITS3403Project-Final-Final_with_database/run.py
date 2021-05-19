# #from sqlite3.dbapi2 import connect
# from flask import Flask, render_template, request, redirect, session, flash
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
# import bcrypt
# import sqlite3
# import os
# import random
# #import os
from app import app


# app = Flask(__name__)
# app.secret_key=os.urandom(24)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///registrations.db'
# db = SQLAlchemy(app)

# conn = sqlite3.connect('registrations.db')
# #Creating a cursor
# cursor = conn.cursor()
# cursor.execute("SELECT * FROM registrations")
# items = cursor.fetchall()

#Creating db Model
# class Registrations(db.Model):
#     username = db.Column(db.String(length=50), nullable=False, unique=True, primary_key=True)
#     email = db.Column(db.String(length=100), unique=True, nullable=False)
#     password = db.Column(db.String(length=256), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)

#     def __repr__(self):
#         return '<Registrations {}>'.format(self.username)


# def get_db():
#     datab = getattr(g, '_database', None)
#     if datab is None:
#         datab = g._database = sqlite3.connect(Registrations)
#         return datab

# @app.teardown_appcontext
# def close_connection(exception):
#     datab = getattr(g, '_database', None)
#     if datab is not None:
#         db.close()

# def retrieveUsers():
#     connectdb = sqlite3.connect("registrations.db")
#     cur = connectdb.cursor()
#     cur.execute("SELECT username, email, password FROM Registrations")
#     users = cur.fetchall()
#     connectdb.close()
#     return users

# @app.route('/getGame/<int:numColls>/<int:numRows>/<int:time>/<string:folderName>')
# def getGame(numColls,numRows,folderName,time):
#     images=[]
#     shortPath=os.path.join(r"static/images",folderName)
#     path=os.path.join(r"app",shortPath)
#     #path=r"C:\Users\Ron Zatuchny\CITS3403Project\Content\app\static\images\colour"
#     gPath=os.path.abspath(path)
#     for d in os.listdir(gPath):
#         Mypath=os.path.join(shortPath,d)
#         images.append(Mypath)
#     for_use=[]
#     random.shuffle(images)
#     for i in range(int((numRows*numColls)/2)):
#         for_use.append(images[i])
#         for_use.append(images[i])
#     random.shuffle(for_use)
#     return render_template('game.html', numColls=numColls, numRows=numRows,paths=for_use,time=time)



# @app.route("/")
# @app.route("/login")
# def index():
#     if 'username' in session:
#         flash("You are already logged in!")
#         return redirect('/home-welcome')
#     else:
#         return render_template('LogInPage.html')


# @app.route("/", methods=['POST', 'GET'])
# @app.route("/login", methods=['POST', 'GET'])
# def register():
#     if request.method == "POST":
#         reg_name = request.form['Username']
#         reg_pass = request.form['Pass']
#         reg_id = request.form['id']

#         hashed = bcrypt.hashpw(reg_pass.encode('utf-8'), bcrypt.gensalt())
#         conn = sqlite3.connect('registrations.db')
#         cursor = conn.cursor()
#         cursor.execute("""SELECT * FROM `registrations` WHERE `username` LIKE '{}'""".format(reg_name))
#         items = cursor.fetchall()
#         if len(items) > 0:
#             flash("Username taken!")
#         cursor.execute("""SELECT * FROM `registrations` WHERE `email` LIKE '{}'""".format(reg_id))
#         items = cursor.fetchall()
#         if len(items) > 0:
#             flash("Email taken!")
#         user = Registrations(username=reg_name, email=reg_id, password=hashed)
#         try:
#             db.session.add(user)
#             db.session.commit()
#             flash("Registered Successfully!")
#             session['username'] = reg_name
#             flash("Welcome! You have logged in!")
#             return redirect('/home-welcome')
#         except:
#             return render_template('messageflash.html')
#     else:
#         return render_template('LogInPage.html')

# @app.route('/login_validation', methods=['POST', 'GET'])
# def login_validation():
#     username = request.form.get('Username')
#     password = request.form.get('Pass').encode('utf-8')
#     conn = sqlite3.connect('registrations.db')
#     #Creating a cursor
#     cursor = conn.cursor()
#     #cursor.execute("SELECT username FROM registrations")
#     cursor.execute("""SELECT * FROM `registrations` WHERE `username` LIKE '{}'""".format(username))
#     items = cursor.fetchall()
#     state = False
#     pos = 0
#     for each in range(len(items)):
#         if (bcrypt.checkpw(password, items[each][2])):
#             pos = each
#             state = True
#             break
#     if len(items) > 0 and state:
#         session['username'] = items[pos][0]
#         flash("Login Successful", "message")
#         return redirect('/home-welcome')
#     else:
#         flash("Invalid Credentials", "warning")
#         return redirect('/log-in')
# @app.route('/home-welcome')
# def homewelcome():
#     return render_template('homealert.html')

# @app.route('/log-in')
# def loginalert():
#     if 'username' in session:
#         flash("You are already logged in!")
#         return redirect('/home-welcome')
#     else:
#         return render_template('/messageflash.html')
# def logout():
#     session.pop('username')
#     flash("You have been logged out!", "info")
#     return redirect('/login')    
# # def register():
# #     username = request.json.get('username', None)
# #     email = request.json.get('email', None)
# #     password = request.json.get('password', None)
# #     if not username:
# #         return "Missing Username", 400
# #     if not email:
# #         return "Missing email", 400
# #     if not password:
# #         return "Missing Password", 400

# #     hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# #     user = User(username=username, email=email, password=hashed)

# #     db.session.add(user)
# #     db.session.commit()
    
# #     return f'Welcome {username}'
# # def login():


# @app.route("/feedback")
# def feedbackpage():
#     if 'username' in session:
#         return render_template('feedback.html')
#     else:
#         flash("You are not logged in, please log in!")
#         return redirect('/log-in')

# @app.route("/statistics")
# def statisticspage():
#     if 'username' in session:
#         return render_template('statistics.html')
#     else:
#         flash("You are not logged in, please log in!")
#         return redirect('/log-in')

# @app.route("/home")
# def homepage():
#     return render_template('home.html')

# @app.route("/assessments")
# def assessmentspage():
#     if 'username' in session:
#         return render_template('content.html')
#     else:
#         flash("You are not logged in, please log in!")
#         return redirect('/log-in')

# @app.route("/contents")
# def contentspage():
#     if 'username' in session:
#         return render_template('assessments.html')
#     else:
#         flash("You are not logged in, please log in!")
#         return redirect('/log-in')

if __name__ == "__main__":
    app.run(debug=True)