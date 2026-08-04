from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://autbor.com/example3.html')

username = browser.find_element(By.ID , 'login_user')
username.send_keys('MyrealUSERNAME')

password = browser.find_element(By.ID, "login_pass")
password.send_keys('MyRealPASSWORD')

checkbox = browser.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
checkbox.click()

submit = browser.find_element(By.CSS_SELECTOR, "input[type='submit']")
submit.click()

input('Press Enter to exit:')
browser.quit()
