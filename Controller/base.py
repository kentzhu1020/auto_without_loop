# coding=utf-
from selenium.webdriver import ActionChains
import sys
from Model.Log import logger
import commands
import os
import subprocess
import time
from selenium import webdriver
import selenium.webdriver.support.ui as ui

__author__ = 'kzhu'

class Base(object):

    def __init__(self,browser):
        self.driver = self.set_up(browser)
        self.element_selector_setting()
        self.wait = ui.WebDriverWait(self.driver, 5)

    def set_up(self,browser_name):
        log = logger()
        cmd = "netstat -an | grep '4444'|awk '{print $6}'"
        dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        browser_name = browser_name.decode('utf-8').lower()
        try:
            if browser_name == 'chrome':
                browser = webdriver.Chrome()
            elif browser_name == 'safari':
                subprocess.Popen(["java", "-jar",dir_path+"/Selenium/selenium-server-standalone-2.48.2.jar"])
                output = commands.getoutput(cmd)
                while 1:
                    if output == '':
                        time.sleep(1)
                        output = commands.getoutput(cmd)
                    else :
                        break
                browser = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.SAFARI)
            else:
                browser = webdriver.Firefox()
            return browser
        except Exception as er:
            pid = commands.getoutput("ps -eaf|grep -i 'selenium'|grep -v grep|awk '{print $2}'")
            if len(pid) != 0:
                log.log("[-] Force killing the process with signal at the beginning of testing")
                os.system("kill -9 "+ pid)
            log.log("[-] Error occur @set_up")
            log.log("[-] The Error is set up browser driver failed, details is "+str(er))
            sys.exit()

    def element_selector_setting(self):
        self.driver.by_id = self.driver.find_element_by_id
        self.driver.by_xpath = self.driver.find_element_by_xpath
        self.driver.by_name = self.driver.find_element_by_name
        self.driver.by_tag_name = self.driver.find_element_by_tag_name
        self.driver.by_css_selector = self.driver.find_element_by_css_selector
        self.driver.by_link_text = self.driver.find_element_by_link_text
        self.driver.by_partial_link_text = self.driver.find_element_by_partial_link_text

    def drag_and_drop(self, elem, target):
        ActionChains(self.driver).drag_and_drop(elem, target).perform()

    def get_current_url(self):
        this_url = self.driver.current_url
        return this_url

    def get_title(self):
        this_title = self.driver.title
        return this_title

    def clear_cookies(self):
        self.driver.delete_all_cookies()


    def quit(self,browser=''):
        self.driver.quit()
        if browser.decode('utf-8').lower() == 'safari':
            self.kill_selenium_process()

    def kill_selenium_process(self):
        pid = commands.getoutput("ps -eaf|grep -i 'selenium'|grep -v grep|awk '{print $2}'")
        log = logger()
        try:
            log.log("Kill the running selenium process")
            os.system('kill -9 '+pid)
        except Exception as er:
            if len(pid) !=0:
                log.log("[-] Failed to kill the process but force it to")
                log.log("[-] Error is "+str(er))
                os.system('kill -9 '+pid)



# if __name__ == '__main__':
#     base  = Base('safari')

