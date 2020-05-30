from selenium import webdriver
import  pytest

class TestCase():
    # def setup(self):
    #     print("teardown: 每个用例开始执行")
    # def teardown(self):
    #     print("teardown: 每个用例结束后执行")
    def setup_class(self):
        print("setup_class：启动浏览器")
        chrome_path = r'C:\Users\MSI-PC\AppData\Local\Google\Chrome\Application\chromedriver.exe'
        self.browser = webdriver.Chrome(executable_path=chrome_path)
        self.browser.get('http://localhost:8000')
    def teardown_class(self):
        print("teardown_class：关闭浏览器")
        self.browser.quit()
    # def setup_method(self):
    #     print("setup_method: 每个用例开始前执行")
    # def teardown_method(self):
    #     print("teardown_method: 每个用例结束后执行")
    def test_django_start_up(self):
        print("正在执行----test_django_start_up")
        assert '登陆' in self.browser.title

if __name__ == '__main__':
    pytest.main(['-s', 'test_functional.py'])