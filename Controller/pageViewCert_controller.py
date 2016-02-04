import time
from Controller.base import Base
from Model.Log import logger
from Views.view_certs_view import repo

__author__ = 'kzhu'

class ViewCertPage(Base):
    def __init__(self,browser):
        Base.__init__(self,browser)
        self.log = logger()

    def search(self):
        driver = self.driver
        try:
            driver.by_xpath(repo['search']).send_keys('test')
            time.sleep(2)
        except Exception as e:
            self.log.log('[-] Error occur @search')
            self.log.log('[-] Error is '+str(e))

    def get_title(self):
        return super(ViewCertPage,self).get_title()