from flask import render_template, request, redirect, session, flash
import random
import bcrypt
import sqlite3
import os
from flask import render_template
from app import app
from app import db
from app.models import Users,Progress
from datetime import datetime

@app.route('/getGame/<int:numColls>/<int:numRows>/<int:time>/<string:folderName>')
def getGame(numColls,numRows,folderName,time):
    if 'username' in session:
        images=[]
        shortPath=os.path.join(r"static/images",folderName)
        path=os.path.join(r"app",shortPath)
        #path=r"C:\Users\Ron Zatuchny\CITS3403Project\Content\app\static\images\colour"
        gPath=os.path.abspath(path)
        for d in os.listdir(gPath):
            Mypath=os.path.join(shortPath,d)
            images.append(Mypath)
        for_use=[]
        random.shuffle(images)
        for i in range(int((numRows*numColls)/2)):
            for_use.append(images[i])
            for_use.append(images[i])
        random.shuffle(for_use)
        return render_template('game.html', numColls=numColls, numRows=numRows,paths=for_use,time=time)
    else:
        flash("Please log in first!")
        return redirect('/log-in')


@app.route("/")
@app.route("/login")
def index():
    if 'username' in session:
        flash("You are already logged in!")
        #return session['username']
        return redirect('/home-welcome')
    else:
        # return Users.query.get("Vigyaanik")
        return render_template('login.html')


@app.route("/", methods=['POST', 'GET'])
@app.route("/login", methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        reg_name = request.form['Username']
        reg_pass = request.form['Pass']
        reg_id = request.form['id']

        hashed = bcrypt.hashpw(reg_pass.encode('utf-8'), bcrypt.gensalt())
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM `users` WHERE `username` LIKE '{}'""".format(reg_name))
        items = cursor.fetchall()
        if len(items) > 0:
            flash("Username taken!")
        cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}'""".format(reg_id))
        items = cursor.fetchall()
        if len(items) > 0:
            flash("Email taken!")
        user = Users(username=reg_name, email=reg_id, password=hashed)
        try:
            db.session.add(user)

            db.session.commit()
            flash("Registered Successfully!")
            session['username'] = reg_name
            flash("Welcome! You have logged in!")
            return redirect('/home-welcome')
        except:
            return render_template('messageflash.html')
    else:
        return render_template('login.html')

@app.route('/login_validation', methods=['POST', 'GET'])
def login_validation():
    username = request.form.get('Username')
    password = request.form.get('Pass').encode('utf-8')
    conn = sqlite3.connect('users.db')
    #Creating a cursor
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM `users` WHERE `username` LIKE '{}'""".format(username))
    items = cursor.fetchall()
    state = False
    pos = 0
    for each in range(len(items)):
        if (bcrypt.checkpw(password, items[each][2])):
            pos = each
            state = True
            break
    if len(items) > 0 and state:
        session['username'] = items[pos][0]
        flash("Login Successful", "message")
        return redirect('/home-welcome')
    else:
        flash("Invalid Credentials", "warning")
        return redirect('/log-in')
@app.route('/home-welcome')
def homewelcome():
    return render_template('homealert.html')

@app.route('/log-in')
def loginalert():
    if 'username' in session:
        flash("You are already logged in!")
        return redirect('/home-welcome')
    else:
        return render_template('/messageflash.html')
@app.route('/logout')
def logout():
    session.pop('username')
    flash("You have been logged out!", "info")
    return redirect('/log-in')

@app.route("/feedback")
def feedbackpage():
    if 'username' in session:
        return render_template('feedback.html')
    else:
        flash("You are not logged in, please log in!")
        return redirect('/log-in')

@app.route("/statistics")
def statisticspage():
    if 'username' in session:
        Allresults = db.session.query(Progress.numFlips).all()
        Allresults=[value for value, in Allresults]
        UseResults=db.session.query(Progress.numFlips).filter_by(username=session['username'] ).all()
        UseResults=[value for value, in UseResults]

        return render_template('statistics.html',Allresults=Allresults,UseResults=UseResults )
    else:
        flash("You are not logged in, please log in!")
        return redirect('/log-in')

@app.route("/home")
def homepage():
    return render_template('home.html')

@app.route("/assessments")
def assessmentspage():
    if 'username' in session:
        return render_template('assessments.html')
    else:
        flash("You are not logged in, please log in!")
        return redirect('/log-in')

@app.route("/contents")
def contentspage():
    if 'username' in session:
        return render_template('content.html')
    else:
        flash("You are not logged in!")
        return redirect('/log-in')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
@app.route("/update/<int:numFlips>")
def update(numFlips):
    data=Progress(numFlips,session['username'] )
    db.session.add(data)
    db.session.commit()
    return render_template('content.html')