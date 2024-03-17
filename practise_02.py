'''
import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
service_obj=Service("C:/Python310/geckodriver.exe")
driver=webdriver.Firefox(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)
driver.maximize_window()
round_buttons=driver.find_elements(By.XPATH,"//fieldset//input[@name='radioButton']")
for button in round_buttons:
    button.click()
driver.find_element(By.CSS_SELECTOR,"input[class*='ui-autocomplete']").send_keys("Ind")
wait=WebDriverWait(driver,5,poll_frequency=1)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"ul[class*='ui-widget-content ui-autocomplete']")))
driver.find_element(By.XPATH,"//li[@class='ui-menu-item']//div[text()='India']").click()
sel=Select(driver.find_element(By.CSS_SELECTOR,"#dropdown-class-example"))
sel.select_by_visible_text("Option2")
check_boxes=driver.find_elements(By.CSS_SELECTOR,"#checkbox-example")
i=0
for check_box in check_boxes:
    check_box.find_element(By.CSS_SELECTOR,"label input[value*='option']").click()
driver.find_element(By.CSS_SELECTOR,"#openwindow").click()
windows=driver.window_handles
driver.switch_to.window(windows[1])
driver.find_element(By.LINK_TEXT,"Courses").click()
driver.close()
driver.switch_to.window(windows[0])
driver.find_element(By.CSS_SELECTOR,"input[name='enter-name']").send_keys("Vish")
time.sleep(4)
driver.find_element(By.XPATH,"//input[@value='Confirm']").click()
time.sleep(4)
alert_text=driver.switch_to.alert
alert_text.accept()
'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
service_obj=Service("C:/Python310/geckodriver.exe")
driver=webdriver.Firefox(service=service_obj)
driver.implicitly_wait(10)
#driver.get("https://www.expedia.com/")
#driver.maximize_window()
#driver.find_element(By.CSS_SELECTOR,"button[name='EGDSDateRange-date-selector-trigger']").click()
#time.sleep(2)
#driver.find_element(By.XPATH,"//table[@class='uitk-month-table' and @aria-label='February 2024']/tbody/tr//div[text()='21']").click()
#date_to_select.click()
#time.sleep(2)
#date_to_select=driver.find_element(By.XPATH,"//table[@class='uitk-month-table' and @aria-label='February 2024']/tbody/tr//div[text()='26']").click()
#date_to_select.click()
#driver.find_element(By.CSS_SELECTOR,"button[class='uitk-button uitk-button-medium uitk-button-has-text uitk-button-primary uitk-layout-flex-item']").click()
#driver.close()
driver.get("https://www.goibibo.com/")

presence=driver.find_element(By.XPATH,"//span[@class='logSprite icClose']")
if presence.is_displayed():
    presence.click()
time.sleep(2)
#driver.find_element(By.XPATH,"//p[@class='sc-jlwm9r-1 ewETUe']").click()
#driver.find_element(By.XPATH,"//input[@type='text']").click()
#driver.save_screenshot('sample1.png')
print(driver.execute_script("return window.innerHeight"))
print(driver.execute_script("return window.innerWidth"))
#assert driver.find_element(By.XPATH,"//input[@type='text']").is_displayed()
#driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Del")
#driver.find_element(By.XPATH,"//div[@class='sc-12foipm-37 lfkrPI']//li//span[@class='autoCompleteTitle ']")