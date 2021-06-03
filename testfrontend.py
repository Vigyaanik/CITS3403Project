import unittest, os
from flask import config
from flask_testing import LiveServerTestCase
from selenium import webdriver
import bcrypt


from app import app, db
from app.models import Users, Progress
import time

#The Database should have username - "Vigyaanik10" with Password - "10" in it before running these tests. Some extra code can be added here on top of this code to achieve this.
class TestBase(unittest.TestCase):
    driver = None
    def create_app(self):
        app.config['TESTING'] = True        
        self.app = app.test_client()
        return app
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=os.path.join(os.path.abspath(os.path.dirname(__file__)), 'chromedriver'))
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.abspath(os.getcwd())+"/test2.db"

        if not self.driver:
            self.skitTest('Web browser not available')
        else:
            db.session.commit()
            db.drop_all()
            db.init_app(app)
            db.create_all()

            db.session.commit()
            self.driver.maximize_window()
            self.driver.get('http://127.0.0.1:5000/')
    
    def tearDown(self):
        # self.driver.close()
        db.session.commit()
        db.session.remove()
        self.driver.quit()



    def test_server_running(self):
        #Testing that the server page is running
        response = self.driver.get('http://127.0.0.1:5000/')
        self.driver.implicitly_wait(5)
        user_field = self.driver.find_element_by_id("input-data-id")
        user_field.send_keys("Vigyaanik10")
        pass_field = self.driver.find_element_by_name("Pass")
        pass_field.send_keys("10")
        time.sleep(1)
        submit_field = self.driver.find_element_by_id("submit-button")
        submit_field.click()
        self.driver.implicitly_wait(10)
        time.sleep(1)
        text_check = self.driver.find_elements_by_class_name("heading")

        self.assertNotEqual(text_check, None)

    def test_server_accessibility(self):
        response = self.driver.get('http://127.0.0.1:5000/')
        self.driver.implicitly_wait(5)
        user_field = self.driver.find_element_by_id("input-data-id")
        user_field.send_keys("Vigyaanik10")
        pass_field = self.driver.find_element_by_name("Pass")
        pass_field.send_keys("10")
        time.sleep(1)
        submit_field = self.driver.find_element_by_id("submit-button")
        submit_field.click()
        self.driver.implicitly_wait(10)
        time.sleep(1)
        content_field = self.driver.find_element_by_id("assessmentsid")
        content_field.click()
        self.driver.implicitly_wait(5)
        content_field = self.driver.find_element_by_id("feedbackid")
        content_field.click()
        self.driver.implicitly_wait(5)
        content_field = self.driver.find_element_by_id("statisticsid")
        content_field.click()
        self.driver.implicitly_wait(5)
        text_check = self.driver.find_elements_by_class_name("heading")
        self.assertNotEqual(text_check, None)
        content_field = self.driver.find_element_by_id("contentid")
        content_field.click()
        self.driver.implicitly_wait(5)
        text_check = self.driver.find_elements_by_class_name("memoryhead")
        self.assertNotEqual(text_check, None)

    def test_server_not_found(self):
        response = self.driver.get('http://127.0.0.1:5000/')
        self.driver.implicitly_wait(5)
        user_field = self.driver.find_element_by_id("input-data-id")
        user_field.send_keys("Vigyaanik10")
        pass_field = self.driver.find_element_by_name("Pass")
        pass_field.send_keys("10")
        time.sleep(1)
        submit_field = self.driver.find_element_by_id("submit-button")
        submit_field.click()
        self.driver.implicitly_wait(10)
        time.sleep(1)
        self.driver.get('http://127.0.0.1:5000/unknown')
        text_field = self.driver.find_element_by_link_text("Back")
        self.assertNotEqual(text_field, None)

    def test_unreachable_locations(self):
        self.driver.get('http://127.0.0.1:5000/contents')
        text_check = self.driver.find_elements_by_class_name("messages")
        self.assertNotEqual(text_check, None)
        self.driver.get('http://127.0.0.1:5000/assessments')
        text_check = self.driver.find_elements_by_class_name("messages")
        self.assertNotEqual(text_check, None)
        self.driver.get('http://127.0.0.1:5000/feedback')
        text_check = self.driver.find_elements_by_class_name("messages")
        self.assertNotEqual(text_check, None)
        self.driver.get('http://127.0.0.1:5000/statistics')
        text_check = self.driver.find_elements_by_class_name("messages")
        self.assertNotEqual(text_check, None)

    def test_login_twice(self):
        #Test that a user can't login twice
        response = self.driver.get('http://127.0.0.1:5000/')
        self.driver.implicitly_wait(5)
        user_field = self.driver.find_element_by_id("input-data-id")
        user_field.send_keys("Vigyaanik10")
        pass_field = self.driver.find_element_by_name("Pass")
        pass_field.send_keys("10")
        time.sleep(1)
        submit_field = self.driver.find_element_by_id("submit-button")
        submit_field.click()
        self.driver.implicitly_wait(10)
        time.sleep(1)
        submit_field = self.driver.find_element_by_id("alert-messages")
        self.assertNotEqual(submit_field, None)
        
if __name__ == '__main__':
    unittest.main()