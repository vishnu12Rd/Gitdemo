import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from pynput.keyboard import Key,Controller
from selenium.webdriver import ActionChains
service_obj=Service("C:/Python310/geckodriver.exe")
driver=webdriver.Firefox(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0,900)")
element = driver.find_element(By.ID, "mousehover")
actions=ActionChains(driver)
actions.move_to_element(element).perform()
actions.move_to_element(driver.find_element(By.XPATH,"//a[text()='Top']")).context_click().perform()

#driver.get("https://jqueryui.com/droppable/")
#driver.switch_to.frame(0)
#from_element=driver.find_element(By.XPATH,"//p[text()='Drag me to my target']")
#to_element=driver.find_element(By.XPATH,"//p[text()='Drop here']")
#action=ActionChains(driver)
#action.drag_and_drop(from_element,to_element).perform()
#action.click_and_hold(from_element).move_to_element(to_element).release().perform()
#action.move_to_element(from_element).context_click()
'''
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0,900)")
element = driver.find_element(By.ID, "mousehover")
actions.move_to_element(element).perform()
actions.move_to_element(driver.find_element(By.XPATH,"//a[text()='Top']")).click().perform()
driver.execute_script("window.scrollBy(0,900)")
actions.move_to_element(element).perform()
actions.move_to_element(driver.find_element(By.XPATH,"//a[text()='Reload']")).click().perform()



driver.get("https://www.plupload.com/examples/")
#driver.find_element(By.XPATH,"//div[@id='uploader_buttons']/div/input").click()
#driver.find_element(By.ID,"uploader_browse").click()
time.sleep(3)
keyboard=Controller()
keyboard.type("C:\\Users\\vhuddeda\\PycharmProjects1\\PythonTesting\\ProjectTestingE2E\\Tests\\sample.png")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
#element=driver.find_element(By.XPATH,"//div[@id='uploader_buttons']/div/input")
#element.send_keys("C:\\Users\\vhuddeda\\PycharmProjects1\\PythonTesting\\ProjectTestingE2E\\Tests\\sample.png")


driver.get("https://www.letskodeit.com/practice")
print(driver.execute_script("return window.innerHeight;"))
print(driver.execute_script("return window.innerWidth;"))
driver.execute_script("")#w-587,h-1280
driver.execute_script("window.scrollBy(0,83)")

#time.sleep(4)
driver.execute_script("window.scrollBy(0,-1000)")
element=driver.find_element(By.CSS_SELECTOR,"#mousehover")
#driver.execute_script("arguments[0].scrollIntoView(true)",element)
driver.execute_script("window.scrollBy(0,-1000)")
driver.execute_script("arguments[0].scrollIntoView(true)",element)
#time.sleep(2)
#driver.execute_script("window.scrollBy(0,-150)")
location=element.location_once_scrolled_into_view
print(location)
driver.quit()
'''