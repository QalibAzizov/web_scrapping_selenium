from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver') #linux
driver.get("")#"https://somesiteexample.com")
driver.implicitly_wait(5)

'''
For current cases, if a blocking window appears 
with the question whether to subscribe or not, 
enter the answer no '''

try:
    no_button = driver.find_element(By.CLASS_NAME, "some")
except:
    print('No element with this class name. Scipping....')

#find elements and add valyue into the input form
sum1 = driver.find_element(By.ID, "b0")
sum2 = driver.find_element(By.ID, "c0")


sum1.send_keys(15)
sum2.send_keys(12)

#if we dont have id an have input type='Calculate' or onclick = 'some' we use CSS selector
btn = driver.find_element(By.CSS_SELECTOR, 'input[value="Calculate"]')
btn.click()