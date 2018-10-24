from selenium import webdriver
"""
driver = webdriver.PhantomJS(executable_path='C:\\Program Files\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
driver.get("https://www.facebook.com/eddrda/about")
"""
"""
driver = webdriver.Chrome(executable_path="C:\\Program Files (x86)\\chromedriver_win32.\\chromedriver.exe")
driver.get("https://www.facebook.com/")

# This will get the initial html - before javascript
html1 = driver.page_source

# This will get the html after on-load javascript
html2 = driver.execute_script("return document.documentElement.innerHTML;")

print(html1)
"""

from selenium.webdriver.common.keys import Keys

usr = "dung23030000@gmail.com"
pwd = "dung1234"

driver = webdriver.Chrome(executable_path="C:\\Program Files (x86)\\chromedriver_win32.\\chromedriver.exe")
driver.get("https://www.facebook.com")
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(usr)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)


driver.get("https://www.facebook.com/eddrda/about")
html2 = driver.execute_script("return document.body.innerHTML")
print(html2)