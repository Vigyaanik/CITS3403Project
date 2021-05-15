import os
from flask import render_template
from app import app
from os import listdir

@app.route('/')
@app.route('/index')
def index():
    return render_template('content.html')
@app.route('/getGame/<int:numColls>/<int:numRows>/<int:test>/<string:folderName>')
def getGame(numColls,numRows,folderName,test):
    images=[]
    path=os.path.abspath(os.path.join("app/static/images",folderName))
    #path=r"C:\Users\Ron Zatuchny\CITS3403Project\Content\app\static\images\colour"
    gPath=os.path.abspath(path)
    for d in os.listdir(gPath):
        images.append(os.path.join(folderName,d))
    return render_template('game.html', numColls=numColls, numRows=numRows,paths=images,test=test)
