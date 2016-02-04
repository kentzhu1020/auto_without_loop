import  unittest
from Controller import inherit_controller
from Model.Log import logger
from TestSuites import __init__


__author__ = 'kzhu'


class EndToEndModule(__init__):

    log = logger()

    @classmethod
    def setUpClass(cls):
        try:
            super(EndToEndModule, cls).setUpClass()
            cls.DRIVER.login_as('kzhu','Black@1')
        except Exception:
            cls.log.log('[-] Trying to start a webdriver but not the first one')
            cls.DRIVER = inherit_controller.Runner('chrome')
            cls.DRIVER.open(__init__.url)
            cls.DRIVER.login_as('kzhu','Black@1')

    @classmethod
    def tearDownClass(cls):
        super(EndToEndModule, cls).tearDownClass()
    def setUp(self):
        pass

    def test_navigation(self):
        self.DRIVER.navigate_to_help()
        self.assertEqual(self.DRIVER.get_title(),'Help Page')
        self.DRIVER.navigate_to_home()
        self.assertEqual(self.DRIVER.get_title(),'Home Page')


    def test_search(self):
        self.DRIVER.navigate_to_view_cert()
        self.assertEqual(self.DRIVER.get_title(),'View Certificate')
        self.DRIVER.search()


    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
