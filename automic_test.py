from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

link = "http://127.0.0.1:8080/"
driver = webdriver.Chrome() # to open the chromebrowser 
driver.get(link)


#login fail
print ("Start testing login failed")

element = driver.find_element_by_name("username")
element.send_keys("hello world")
time.sleep(1)
element.submit()

obj = driver.switch_to.alert
msg=obj.text
print ("Alert message: "+ msg )

time.sleep(2)
obj.accept()

print ("End of testing login failed")

#login as user
print("Start owner testing")
element = driver.find_element_by_xpath('//*[@id="login"]/div/p[1]/input')
element.send_keys("owner")
time.sleep(2)
element.submit()
if (driver.current_url=="{}home".format(link)):
    print("Owner login suceess")

#apple detail
time.sleep(2)
org_no = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div/p/b')
second_layer=driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[1]/div/div/img")
apple_button = driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[1]/div/div/div/button")

print("Apple",org_no.text)
print("Try to refill APPLE as 20")

hover=ActionChains(driver).move_to_element(second_layer)
hover.perform()
apple_button.click()

if (driver.current_url=="{}detail?id=1".format(link)):
    print("Now in Apple Detail")

#Refill apple
print("Apple Replenish")
time.sleep(2)
refill_no = driver.find_element_by_xpath('/html/body/div[2]/div[3]/form/table/tbody/tr[3]/td/input')
input = driver.find_element_by_xpath('/html/body/div[2]/div[3]/form/table/tbody/tr[4]/td[1]/button')
refill_no.clear()
refill_no.send_keys("20")
time.sleep(2)
input.click()

obj = driver.switch_to.alert
msg=obj.text
print ("Alert message: "+ msg )
time.sleep(2)

obj.accept()

now_no =driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div/p/b')
print("Apple Now",now_no.text)
time.sleep(2)

print('Check back function')
second_layer=driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[1]/div/div/img")
apple_button = driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[1]/div/div/div/button")
hover=ActionChains(driver).move_to_element(second_layer)
hover.perform()
apple_button.click()
refill_no = driver.find_element_by_xpath('/html/body/div[2]/div[3]/form/table/tbody/tr[3]/td/input')
back = driver.find_element_by_xpath('/html/body/div[2]/div[3]/form/table/tbody/tr[4]/td[2]/button')
refill_no.clear()
refill_no.send_keys("30")
time.sleep(2)
back.click()
now_no =driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div/p/b')
print("Apple Now",now_no.text)

#logout
logout = driver.find_element_by_xpath('/html/body/nav/div[2]/a[2]')
logout.click()
time.sleep(2)

if(driver.current_url=="{}login".format(link)):
    print("Logout sucess")
    print("End of owner testing")
driver.close()
