import selenium
import os
import unittest
import bcrypt
import sqlite3
import selenium 
from app import app, db
from app.models import Users
# python -m unittest

basedir = os.path.abspath(os.path.dirname(__file__))
driver = None
class LoginPageCase(unittest.TestCase):
   def setUp(self):
      #Setting up the driver
      self.driver = selenium.webdriver.Chrome(executable_path=os.path.join(basedir, 'chromedriver'))
      self.driver.implicitly_wait(30)
      self.driver.maximize_window()

      # Navigate to the application home page
      self.driver.get("http://localhost:5000/")

      #Getting the Register Id
      register_field = self.driver.find_element_by_id("input-data-id")


      file_path = os.path.abspath(os.getcwd())+"/users.db"
      app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + file_path
      self.app = app.test_client()
      db.create_all()
      pass1 = "1234"
      pass2 = "3421"
      pass3 = "abc3e"
      userno1 = Users(username="Zinda", email="email1@gmail.com", password = bcrypt.hashpw(pass1.encode('utf-8'), bcrypt.gensalt()))
      userno2 = Users(username="Zindagi", email="34@gmail.com", password = bcrypt.hashpw(pass1.encode('utf-8'), bcrypt.gensalt()))
      db.session.add(userno1)
      db.session.add(userno2)
      db.session.commit()

   def tearDown(self):
       db.session.remove()
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

   def test_already_registered(self):
      pass1 = "somepass"
      anotherUser = Users(username="Zindagi", email="someemail@email.com", password = bcrypt.hashpw(pass1.encode('utf-8'), bcrypt.gensalt()))
      db.session.add(anotherUser)

      
   # def test_unique_contraint(self):
   #    apass = "1234"
   #    repeatedUser = Users(username="Zinda", email="hai@toh.com", password=bcrypt.hashpw(apass.encode('utf-8'), bcrypt.gensalt()))
   #    if

   #simple test to check if 404 errors work
   #  def test_index(self):
   #      tester = app.test_client(self)
   #      response = tester.get('/index/asdqwe', content_type='html/text')
   #      self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
