import time
from Controller.pageIndex_controller import IndexPage
from Controller.pageHome_controller import HomePage
from Controller.pageViewCert_controller import ViewCertPage

__author__ = 'kzhu'

class Runner(IndexPage,HomePage,ViewCertPage):
    def __init__(self,browser):
        super(Runner,self).__init__(browser)


# if __name__ == '__main__':
#     user = Runner('chrome')
#     user.open('bbcerts.bbpd.io')
#     user.login_as()
#     time.sleep(5)
#     print user.get_current_url()
#     print user.get_title()
#     user.quit()