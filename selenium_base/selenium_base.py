#绝对导入是相对于包内引入来说的
from selenium import webdriver
import time
import os
import logging 
#seleium 怎么导入日志
OVER_TIME = 5
BASE_URL = "https://map.baidu.com"



def get_driver(type_driver):
    driver = getattr(webdriver,type_driver)()

    return driver


class BasePage(object):
    #单例模式感觉没有什么卵用
    # def __new__(cls, *args, **kw):
    #     """
    #     使用单例模式将类设置为运行时只有一个实例，在其他Python类中使用基类时，
    #     可以创建多个对象，保证所有的对象都是基于一个浏览器
    #     """
    #     if not hasattr(cls, '_instance'):
    #         orig = super(Driver, cls)
    #         cls._instance = orig.__new__(cls, *args, **kw)
    #     return cls._instance

    def __init__(self,driver):
        self.driver= driver
        self.driver.implicitly_wait(OVER_TIME)

    def start(self, url=BASE_URL):
        """
        启动浏览器
        :param url: 测试地址
        :param driver_name: 在启动时设置浏览器的类型
        :return:
        """
        self.driver.get(url)
        self.driver.maximize_window()

    def get_url(self):
        """返回浏览器的地址"""
        return BASE_URL
    
    # def find_elements(self,*loc):

            
    #     return element


    ## 私有方法
    def __time_format(self):
        current_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        return current_time

    #截屏
    def get_screenshot(self,path="../screenshot/"):
        
        if not os.path.exists(path):
           os.makedirs(path)
        filename = path +self.__time_format()+".png"
        self.driver.get_screenshot_as_file(filename)
        return filename

    # 显式等待


    #隐式等待

    #可见元素
    #不可见元素

    #滚轮直到发现某个元素
    def scroll_down(self,height=0):
        if height:
            self.driver.execute_script('window.scrollTo(0,%s)' %height)
        else:
            self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

    # def scroll_to_element(self,locator):
    #     for i in range(1,50):
    #         height = i*200
    #         self.driver.execute_script('window.scrollTo(0,%s)' % height)
    #         self.wait(1)
    #         if len(self.find_elements(locator)):
    #             break

    # 重试机制，增加稳定性


    def quit(self):
        self.driver.quit()

    def close(self):
         self.driver.close()


if __name__ == "__main__":
      driver = webdriver.Chrome()
      browser = BasePage(driver)
      browser.start(url="https://testerhome.com/articles/23843")
      browser.start(url="https://www.baidu.com")
      time.sleep(1)
      browser.scroll_down(2000)
      browser.get_screenshot()
      browser.quit()



