import os
from flask import render_template
from app import app
from os import listdir
import random
@app.route('/')
@app.route('/index')
def index():
    return render_template('content.html')
@app.route('/getGame/<int:numColls>/<int:numRows>/<int:time>/<string:folderName>')
def getGame(numColls,numRows,folderName,time):
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
