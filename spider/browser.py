from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
 
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # 每次启动自动安装驱动（慢）
# browser = webdriver.Chrome(service=Service("r D:\\chromedriver.exe")) # 加载本地驱动，版本不对
# browser = webdriver.Chrome()

browser.set_window_size(500, 500)
browser.get("http://www.baidu.com")
browser.find_element(by=By.ID, value="kw").send_keys("python教程")
#text_box = browser.find_element(by=By.NAME, value="my-text")
#submit_button = browser.find_element(by=By.CSS_SELECTOR, value="button")

print(browser.title)
print(browser.current_url)
print(browser.name)
print(browser.page_source)
 
browser.quit()