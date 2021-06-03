from re import U
from selenium import webdriver
import os
import unittest
import bcrypt
import sqlite3
from sqlalchemy.util.compat import u 
from app import app, db
from app.models import Users
# python -m unittest

basedir = os.path.abspath(os.path.dirname(__file__))
driver = None
class LoginPageCase(unittest.TestCase):
   def setUp(self):
      #Setting up the driver
      self.driver = webdriver.Chrome(executable_path=os.path.join(basedir, 'chromedriver'))
      self.driver.implicitly_wait(30)
      self.driver.maximize_window()

      #Connecting to the database
      file_path = os.path.abspath(os.getcwd())+"/users.db"
      app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + file_path
      self.app = app.test_client()
      db.create_all()
      
      user1 = Users.query.filter_by(username = 'Zinda').first()
      if user1 != None:
         db.session.delete(user1)
         db.session.commit()
      
      user2 = Users.query.filter_by(username = 'Zindagi').first()
      if user1 != None:
         db.session.delete(user2)
         db.session.commit()
      pass1 = "1234"
      pass2 = "3421"
      userno1 = Users(username="Zinda", email="email1@gmail.com", password = bcrypt.hashpw(pass1.encode('utf-8'), bcrypt.gensalt()))
      userno2 = Users(username="Zindagi", email="34@gmail.com", password = bcrypt.hashpw(pass2.encode('utf-8'), bcrypt.gensalt()))
      db.session.add(userno1)
      db.session.add(userno2)
      db.session.commit()

      # Navigate to the application home page
      self.driver.maximize_window()
      self.driver.get("http://localhost:5000/")

   def tearDown(self):
       db.session.delete()
       db.drop_all()

   def test_login_password(self):
      temp_password = "I am a disco dancer."
      temp_password2 = "1234"
      temp_password = temp_password.encode('utf-8')
      temp_password2 = temp_password2.encode('utf-8')
      # a_user = Users(username="Username", email="the@mad.man", password = bcrypt.hashpw(temp_password.encode('utf-8'), bcrypt.gensalt()))
      conn = sqlite3.connect('users.db')
      cursor = conn.cursor()
      cursor.execute("""SELECT * FROM `users` WHERE `username` LIKE '{}'""".format("Zinda"))
      items = cursor.fetchall()
      # print(items)
      self.assertFalse(bcrypt.checkpw(temp_password, items[0][2]))
      self.assertTrue(bcrypt.checkpw(temp_password2, items[0][2]))

   def test_login(self):
      self.driver.get("http://localhost:5000/")
      user_name = self.driver.find_element_by_id('input-data-id-1')
      psswd = self.driver.find_element_by_id('input-data-id-2')
      submit = self.driver.find_element_by_id('submit-button')

      user_name.send_keys('Zinda')
      psswd.send_keys('1234')

      submit.click()

      self.driver.implicitly_wait(5)
      
      get_title = self.driver.title
      self.assertEquals(get_title, "Home")

   def test_login_2(self):
      self.driver.get("http://localhost:5000/")
      user_name = self.driver.find_element_by_id('input-data-id-1')
      psswd = self.driver.find_element_by_id('input-data-id-2')
      submit = self.driver.find_element_by_id('submit-button')

      user_name.send_keys('Usernames')
      psswd.send_keys('1234')

      submit.click()

      self.driver.implicitly_wait(5)
      
      get_title = self.driver.title
      self.assertEquals(get_title, "Home")



if __name__ == '__main__':
    unittest.main()