import time
from Controller.base import Base
from Model.Log import logger
from Views.home_view import repo

__author__ = 'kzhu'

class HomePage(Base):
    def __init__(self,browser):
        Base.__init__(self,browser)

    def navigate_to_home(self):
        log = logger()
        driver = self.driver
        try:
            driver.by_link_text(repo['navigation_home']).click()
            time.sleep(2)
        except Exception as e:
            log.log('[-] Error occur @navigate_to_home')
            log.log('[-] Error is '+str(e))

    def navigate_to_view_cert(self):
        log = logger()
        driver = self.driver
        try:
            driver.by_link_text(repo['navigation_view_certs']).click()
            time.sleep(3)
        except Exception as e:
            log.log('[-] Error occur @navigate_to_view_cert')
            log.log('[-] Error is '+str(e))

    def navigate_to_notification_group(self):
        log = logger()
        driver = self.driver
        try:
            driver.by_link_text(repo['navigation_notification_group']).click()
            time.sleep(3)
        except Exception as e:
            log.log('[-] Error occur @navigate_to_notification_group')
            log.log('[-] Error is '+str(e))

    def navigate_to_help(self):
        log = logger()
        driver = self.driver
        try:
            driver.by_link_text(repo['navigation_help']).click()
            time.sleep(3)
        except Exception as e:
            log.log('[-] Error occur @navigate_to_help')
            log.log('[-] Error is '+str(e))

    def logout(self):
        log = logger()
        driver = self.driver
        try:
            driver.by_link_text(repo['logout']).click()
            time.sleep(2)
        except Exception as e:
            log.log('[-] Error occur @logout')
            log.log('[-] Error is '+str(e))

    def get_title(self):
        return super(HomePage,self).get_title()

