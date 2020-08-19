from selenium import webdriver
import time
   
OVER_TIME = 5
BASE_URL = "https://map.baidu.com"

   
class Driver(object):
    def __new__(cls, *args, **kw):
        """
        使用单例模式将类设置为运行时只有一个实例，在其他Python类中使用基类时，
        可以创建多个对象，保证所有的对象都是基于一个浏览器
        """
        if not hasattr(cls, '_instance'):
            orig = super(Driver, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

    def start(self, url=BASE_URL, driver_name="Chrome"):
        """
        启动浏览器
        :param url: 测试地址
        :param driver_name: 在启动时设置浏览器的类型
        :return:
        """
        if driver_name == "Firefox":
            self.driver = webdriver.Firefox()
        elif driver_name == "Ie":
            self.driver = webdriver.Ie()
        else:
            self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(OVER_TIME)
        self.driver.get(url)
        self.driver.maximize_window()

    def get_url(self):
        """返回浏览器的地址"""
        return BASE_URL
    
    def close(self):
         self.driver.close()


if __name__ == "__main__":
      browser = Driver()
      browser.start()
      time.sleep(10)
      browser.close()



