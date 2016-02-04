import unittest
from Controller import inherit_controller

__author__ = 'kzhu'


class __init__(unittest.TestCase):


    DRIVER = inherit_controller.Runner('chrome')
    url = 'bbcerts.bbpd.io'
    # g_pass_count = 0
    # g_fail_count = 0

    @classmethod
    def setUpClass(cls):
        cls.DRIVER.open(cls.url)
        return cls.DRIVER

    @classmethod
    def tearDownClass(cls):
        cls.DRIVER.quit()











