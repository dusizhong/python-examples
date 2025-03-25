from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# option = webdriver.ChromeOptions()  # 创建一个配置对象
# option.add_argument("--headless")  # 开启无界面模式
# option.add_argument("--disable-gpu")  # 禁用gpu

# browser = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # 每次启动自动安装驱动慢
browser = webdriver.Chrome(service=Service("D:\\chromedriver.exe")) # 加载本地驱动

browser.set_window_size(500, 500)
browser.get("http://hebeibidding.com:5000/TPFrame/customframe4bid/login_TP")
time.sleep(3)

browser.find_element(by=By.ID, value="txtUserName").send_keys("admin")
browser.find_element(by=By.ID, value="txtPwd").send_keys("123")
#text_box = browser.find_element(by=By.NAME, value="my-text")
submit_button = browser.find_element(by=By.CLASS_NAME, value="btn")
# submit_button.click()
browser.execute_script("arguments[0].click()", submit_button)

print(browser.current_url)
print(browser.title)
# print(browser.page_source)

# browser.quit()

#这里input用来保证命令行运行的情况下，Python主程序不结束，否则会带着Selenium彻底退出，会关闭浏览器
input("Selenium is running, input 'q' quit: ")
