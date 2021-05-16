from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('content.html')
@app.route('/getGame/<int:numColls>/<int:numRows>/<string:folderName>/<int:test>')
def getGame(numColls,numRows,folderName,test):
    return render_template('game.html', numColls=numColls, numRows=numRows,folderName=folderName,test=test)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(500):
    dp.session.rollback()
    return render_template('500.html'), 500
