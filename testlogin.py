# import pytest
import os
import unittest
import bcrypt
import sqlite3
import selenium
import pytest
from app import app, db
from app.models import Users, Progress
from flask import url_for, abort
# from flask_testing import TestCase

class LoginPageCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.abspath(os.getcwd())+"/test.db"
        db.drop_all() #Just to make sure there are no entries in the testing database before adding to the database.
        db.create_all()
        pass1 = "1234"
        pass2 = "3421f"
        userno1 = Users(username="Zinda", email="email1@gmail.com", password = bcrypt.hashpw(pass1.encode('utf-8'), bcrypt.gensalt()))
        userno2 = Users(username="Zindagi", email="34@gmail.com", password = bcrypt.hashpw(pass2.encode('utf-8'), bcrypt.gensalt()))
        prog1 = Progress(username="Zinda", numFlips=23)
        prog2 = Progress(username="Zinda", numFlips=22)
        prog3 = Progress(username="Zindagi", numFlips=21)
        db.session.add(userno1)
        db.session.add(userno2)
        db.session.add(prog1)
        db.session.add(prog2)
        db.session.add(prog3)
        db.session.commit()

    def tearDown(self):
        #This function runs after every test.
        db.session.remove()
        db.drop_all()

    def test_entries(self):
        #Test to check both the entries got added to the database or not.
        self.assertEqual(Users.query.count(), 2)
   
    def test_login_password(self):
        #Test to check whether a matching username and password will give access to the database or not and it's converse.
        temp_password = "I am a disco dancer."
        temp_password2 = "1234"
        temp_password = temp_password.encode('utf-8')
        temp_password2 = temp_password2.encode('utf-8')
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM `users` WHERE `username` LIKE '{}'""".format("Zinda"))
        items = cursor.fetchall()
        self.assertFalse(bcrypt.checkpw(temp_password, items[0][2]))
        self.assertTrue(bcrypt.checkpw(temp_password2, items[0][2]))


    def test_progress_database(self):
        #Test to check that Progress database is storing data correctly
        self.assertEqual(Progress.query.count(), 3)
        self.assertNotEqual(Progress.query.count(), 0)

    def test_password_hashing(self):
        #Test to check that Passwords are being stored as hashes
        pass_check = "3421f"
        pass_check = pass_check.encode('utf-8')
        usernaam = "Zindagi"        
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM `users` WHERE `username` LIKE '{}'""".format("Zindagi"))
        items = cursor.fetchall()
        self.assertFalse(bcrypt.checkpw(pass_check, items[0][2]))

    def test_homepage_view(self):
        #Test to check that we can reach home page without logging in.
        with app.test_client() as c:
            response = c.get('/home')
            self.assertEqual(response.status_code, 200)
    
    def test_contentspage_view(self):
        #Test to check that we can not reach contents page without logging in.
        with app.test_client() as c:
            response = c.get('/contents')
            redirected = c.get('/log-in')
            self.assertEqual(response.status_code, 302)

    def test_feedbackpage_view(self):
        #TEst to check that we can't reach feedback, statistics, game without logging in.
        with app.test_client() as c:
            response = c.get('/feedback')
            self.assertEqual(response.status_code, 302)
        with app.test_client() as c:
            response = c.get('/statistics')
            self.assertEqual(response.status_code, 302)
        with app.test_client() as c:
            response = c.get('/getGame/6/4/10/All)')
            self.assertEqual(response.status_code, 302)
    
    def test_404_not_found(self):
        #Testing that 404 error is working correctly
        with app.test_client() as c:
            response = c.get('/something')
            self.assertNotEqual(response.status_code, 302)
            self.assertEqual(response.status_code, 404)
        


if __name__ == '__main__':
    unittest.main()