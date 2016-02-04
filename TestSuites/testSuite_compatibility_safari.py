import  unittest
from Controller import inherit_controller
from Model.Log import logger


__author__ = 'kzhu'
class CompatibilitySafari(unittest.TestCase):

    SAFARI = inherit_controller.Runner('safari')

    @classmethod
    def setUpClass(cls):
        cls.SAFARI.open('bbcerts.bbpd.io')
        return cls.SAFARI

    @classmethod
    def tearDownClass(cls):
        cls.SAFARI.quit('safari')


    def setUp(self):
        pass

    def test_login(self):
        self.SAFARI.login_as('kzhu','Black@1')
        self.assertEqual(self.SAFARI.get_title(),'Home Page')

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()