import csv
import os
import  unittest
from Controller import inherit_controller
from Model.Log import logger
from TestSuites import __init__

__author__ = 'kzhu'

class SmokeTestSuite(__init__):

    log = logger()

    @classmethod
    def setUpClass(cls):
        try:
            super(SmokeTestSuite, cls).setUpClass()
        except Exception:
            cls.log.log('[-] Trying to start a webdriver but not the first one')
            cls.DRIVER = inherit_controller.Runner('chrome')
            cls.DRIVER.open(__init__.url)

    @classmethod
    def tearDownClass(cls):
        super(SmokeTestSuite, cls).tearDownClass()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_login(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(BASE_DIR+'/Data/login_data.csv') as configfile:
            reader = csv.DictReader(configfile)
            for row in reader:
                username = row['username']
                password = row['password']
                self.DRIVER.login_as(username,password)
                self.assertEqual(self.DRIVER.get_title(),'Home Page')
                self.DRIVER.logout()




if __name__ == "__main__":
    unittest.main()




