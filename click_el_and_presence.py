from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
driver.get("")#"https://somesiteexample.com")

driver.implicitly_wait(10)

#find element by classname and clik it
element = driver.find_element(By.CLASS_NAME, "search-toggle-li")
print("element:",element)
element.click()

#after click we will wait until located elements are precence
WebDriverWait(driver, 30).until(
    EC.presence_of_all_elements_located(
        (By.ID, 'someid'),#Element filtration
        
    )
)

