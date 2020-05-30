from selenium import webdriver
import  pytest
from django.urls import resolve
from basicinfo.views import login

import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scoresystem.settings")  # project_name 项目名称
django.setup()

# @pytest.fixture(scope="module")
# def first():
#     print("\n获取用户名,scope为module级别当前.py模块只运行一次")
#     a = "yoyo"
#     return a
chrome_path = r'C:\Users\MSI-PC\AppData\Local\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(executable_path=chrome_path)

def setup_module():
    print("setup_class：启动浏览器")
    browser.get('http://localhost:8000')

def teardown_module():
    print("teardown_class：关闭浏览器")
    browser.quit()
class TestLoginPage():
    # def setup(self):
    #     print("teardown: 每个用例开始执行")
    # def teardown(self):
    #     print("teardown: 每个用例结束后执行")
    # def setup_class(self):
    #     pass
    # def teardown_class(self):
    #     print("teardown_class：关闭浏览器")
    #     browser.quit()
    # def setup_method(self):
    #     print("setup_method: 每个用例开始前执行")
    # def teardown_method(self):
    #     print("teardown_method: 每个用例结束后执行")
    # def test_django_start_up(self):
    #     print("正在执行----test_django_start_up")
    #     assert '登陆' in browser.title

    def test_root_url_resolves_to_login_view(self):

        found = resolve('/login/')
        assert found.func==login


if __name__ == '__main__':

    pytest.main(['-s', 'test_login_page.py'])