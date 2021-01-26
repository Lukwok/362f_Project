from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from prettytable import PrettyTable
import time
from datetime import datetime
import random
from random import choice

link = "http://127.0.0.1:8080/"
driver = webdriver.Chrome() # to open the chromebrowser 
driver.get(link)

def show_cart():
    t = PrettyTable(['Product', 'Price', 'Quantity', 'Total'])
    rows=driver.find_elements_by_id("product-row")
    for row in rows:
        product = row.find_elements_by_tag_name("td")[0].text
        price = row.find_elements_by_tag_name("td")[1].text
        quantity = row.find_elements_by_tag_name("td")[2].find_element_by_tag_name("input").get_attribute('value')
        total = row.find_elements_by_tag_name("td")[3].text
        t.add_row([product,price,quantity,total])
    print("MY CART:")
    print(t)

def show_final_cart():
    container = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div")
    rows = container.find_elements_by_tag_name("p")
    print("Modified cart:")
    t = PrettyTable()
    for row in rows:
        content = row.text.split()
        if content[0] == "Total":
            t.field_names = content
        else:
            t.add_row(content)
    print(t)

def add_to_cart(num):
    refill_no = driver.find_element_by_xpath('/html/body/div[2]/div[3]/form/table/tbody/tr[3]/td/input')
    add = driver.find_element_by_xpath('/html/body/div[2]/div[3]/form/table/tbody/tr[4]/td[1]/button')
    refill_no.clear()
    refill_no.send_keys(str(num))
    time.sleep(2)
    add.click()

    if (driver.current_url=="{}cart".format(link)):
        print("Add to Cart Success")
        show_cart()
        time.sleep(2)
        button = driver.find_element_by_xpath("/html/body/div[2]/div[3]/form/div[2]/button[1]")
        button.click()
    else:
        print("Add to chart failed!! Reason: Input Quanity Wrong")
        button = driver.find_element_by_xpath("/html/body/div[2]/div[3]/form/table/tbody/tr[4]/td[2]/button")
        button.click()

def checkout_input(em,cname,cnum,year,month,cvv):
    email_input=driver.find_element_by_id("email")
    card_name_input = driver.find_element_by_id("cname")
    card_no_input = driver.find_element_by_id("ccnum")
    date_input = driver.find_element_by_id("exp")
    cvv_input = driver.find_element_by_id("cvv")
    checkout_button = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/form/input")

    email_input.clear()
    card_name_input.clear()
    card_no_input.clear()
    # date_input.clear()
    cvv_input.clear()
    
    email_input.send_keys(em)
    card_name_input.send_keys(cname)
    card_no_input.send_keys(cnum)
    date_input.send_keys(year,Keys.TAB,month)
    cvv_input.send_keys(cvv)

    time.sleep(3)
    rand_time = random.randint(3,10)        #random waiting time for check out
    print("Now waiting {}second then process checkout".format(rand_time))
    time.sleep(rand_time)
    checkout_button.click()

def alert_handle():
    obj = driver.switch_to.alert
    msg=obj.text
    print ("Alert message: "+ msg )
    time.sleep(2)

    obj.accept()
    time.sleep(3)

print("Start customer testing")
while(True):
    element = driver.find_element_by_xpath('//*[@id="login"]/div/p[1]/input')
    input= choice(['guest','user']) #login as guest or user
    element.send_keys(input)
    time.sleep(4)
    element.submit()
    if (driver.current_url=="{}home".format(link)):
        print("{} login suceess".format(input))
        break
    alert_handle()


#apple detail
time.sleep(2)
second_layer=driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[1]/div/div/img")
apple_button = driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[1]/div/div/div/button")
print("Try to add 20 apple in cart")

hover=ActionChains(driver).move_to_element(second_layer)
hover.perform()
apple_button.click()

if (driver.current_url=="{}detail?id=1".format(link)):
    print("Now in Apple Detail")

#Add apple in chart 
print("Adding Apple")
time.sleep(2)
add_to_cart(20)

#sandwiches detail
second_layer=driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[2]/div/div/img")
apple_button = driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[2]/div/div/div/button")
print("Try to add 1 sandwiches in cart")

hover=ActionChains(driver).move_to_element(second_layer)
hover.perform()
apple_button.click()

if (driver.current_url=="{}detail?id=2".format(link)):
    print("Now in Sandwich Detail")

#Add Sandwich in chart 
print("Adding 1 Sandwich")
time.sleep(2)
add_to_cart(1)

#sandwiches detail
second_layer=driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[8]/div/div/img")
apple_button = driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[8]/div/div/div/button")
print("Try to add 2 jam in cart")

hover=ActionChains(driver).move_to_element(second_layer)
hover.perform()
apple_button.click()

if (driver.current_url=="{}detail?id=8".format(link)):
    print("Now in 2 Jam Detail")

#Add Jam in chart 
print("Adding Jam")
time.sleep(2)
add_to_cart(2)


#Manage Cart
print("Go to Cart Page")
cartb = driver.find_element_by_xpath("/html/body/nav/div[2]/a[2]")
cartb.click()

if (driver.current_url=="{}cart".format(link)):
    show_cart()
    print("Change SANDWICHES Quantity to 4 and Delete JAM")
    jam_delete = driver.find_element_by_xpath("/html/body/div[2]/div[3]/form/table/tbody/tr[4]/td[5]/a")
    jam_delete.click()
    sandwich_no = driver.find_element_by_xpath("/html/body/div[2]/div[3]/form/table/tbody/tr[3]/td[3]/input")
    sandwich_no.clear()
    sandwich_no.send_keys("4")
time.sleep(1)
checkout = driver.find_element_by_xpath("/html/body/div[2]/div[3]/form/div[2]/button[2]")
checkout.click()


if (driver.current_url=="{}checkout".format(link)):
    show_final_cart()
    print("Entering checkout informaton")
    checkout_input("123@abc.com","Peter","1111222233334444","2021","12","123")

time.sleep(3)

#alert
alert_handle()
#Other fail testing
time.sleep(2)
home_page = driver.find_element_by_xpath("/html/body/nav/div[2]/a[1]")
home_page.click()

second_layer=driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[6]/div/div/img")
apple_button = driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[6]/div/div/div/button")
print("Add 1 chocolate in cart")

hover=ActionChains(driver).move_to_element(second_layer)
hover.perform()
apple_button.click()

add_to_cart(1)

shopping_cart = driver.find_element_by_xpath("/html/body/nav/div[2]/a[2]")
shopping_cart.click()

if (driver.current_url == "{}cart".format(link)):
    show_cart()
    time.sleep(1)
    checkout = driver.find_element_by_xpath("/html/body/div[2]/div[3]/form/div[2]/button[2]")
    checkout.click()
    time.sleep(2)

if (driver.current_url=="{}checkout".format(link)):
    print("Enter wrong email")
    checkout_input("123abc.com","Peter","1111222233334444","2021","12","123")
    alert_handle()
    print("Enter wrong card number")
    checkout_input("123@abc.com","Peter","111122223333aaaa","2021","12","123")
    alert_handle()
    print("Enter expiried card date")
    checkout_input("123@abc.com","Peter","1111222233334444","2020","12","123")
    alert_handle()
    #session timeout
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    time.sleep(182)
    if(driver.current_url=="{}cart".format(link)):
        print("Checkout page is expiried in 3 minutes")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
        show_cart()
        time.sleep(2)

if (driver.current_url=="{}cart".format(link)):
    print("click the item link, jump to item detail") 
    table_body = driver.find_element_by_tag_name("tbody")
    item_link = table_body.find_element_by_tag_name("a") 
    item_link.click()

    obj = driver.switch_to.alert
    msg=obj.text
    print ("Alert message: "+ msg )
    time.sleep(2)

    obj.dismiss()
    if(driver.current_url=="{}cart".format(link)):
        print("Cancel button is clicked")
        table_body = driver.find_element_by_tag_name("tbody")
        item_link = table_body.find_element_by_tag_name("a") 
        item_link.click()

        obj = driver.switch_to.alert
        msg=obj.text
        print ("Alert message: "+ msg )
        time.sleep(2)
        obj.accept()

        if not(driver.current_url=="{}cart".format(link)):
            print("Jump to item detail")

time.sleep(3)
logout = driver.find_element_by_xpath("/html/body/nav/div[2]/a[4]")
logout.click()

if(driver.current_url=="{}login".format(link)):
    print("logout sucess")
    print("End of customer testing")
    
driver.close()
