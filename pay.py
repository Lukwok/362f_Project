import re
import datetime
from cart import shopping_cart
from database import database
import mysql.connector


def email_check(email):
    my_email = email
    #contain only 1 @
    #at least 1 word before . amd @
    #1 word after @ and .
    rule = re.compile('^[\w\-]+(\.[\w\-]+)*@[\w]+(\.[\w]+)+$')

    if rule.match(my_email):
        print('True')
        return True
    else:
        print('False')
        return False

def card_check(card):
    try:
        card_number=int(card)
        upper_no = 10000000000000000
        lower_no = 999999999999999
        if (card_number>lower_no and card_number<upper_no):
            print('True')
            return True
        else:
            print('False')
            return False
    except:
        print('False')
        return False

def date_check(exp_data):
    now = datetime.datetime.now()
    my_year = exp_data.split('-')[0]
    my_month = exp_data.split('-')[1]

    if(int(my_year)== int(now.year)):

        if(int(my_month)> int(now.month)):
            print('True')
            return True
        else:
            print('False')
            return False
        
    elif (int(my_year)> int(now.year)):
        print('True')
        return True
    else:
        print('False')
        return False

def update_database(cart_item):
    #get orgrinal quantity
    query = "Select Quantity from catalogue where ProductID={}".format(str(cart_item.item_id))
    data = database(query)
    old_quantity = data[0][0]

    new_quantity = int(old_quantity)-int(cart_item.count)
    my_id = int(cart_item.item_id)

    try:
        query = 'Update catalogue Set Quantity={} where ProductID={}'.format(str(new_quantity),str(my_id))
        db = mysql.connector.connect(user='root',password='root',
                              host='127.0.0.1',database='362f')
        print("Connect to Database Sucessful")
        cursor = db.cursor()
        cursor.execute(query)
        cursor.close()
        db.commit()

        print('Updated {} (Product_id: {} ) Successfully'.format(cart_item.item_name,cart_item.item_id))
        
    except:
        print('Updated Failed')

def stock_check(cart):
    flag = True
    for item in cart:
        query = "Select Quantity from catalogue where ProductID={}".format(str(item.item_id))
        data = database(query)
        updated_quantity = data[0][0] 
        
        if (int(item.count)>int(updated_quantity)):
            print('Sorry! Not enough {}'.format(item.item_name))
            flag = False

    print(flag)
    return(flag)

def finish_payment(email,card_no,date,cart):
    email_flag = email_check(email)
    card_flag = card_check(card_no)
    date_flag = date_check(date)
    stock_flag = stock_check(cart)
    """
    erroe_code:
    0 : No Error
    1 : Email Error
    2 : Card Number Error
    3 : Card exp Error
    4 : Stock Error
    """
    error_code = 0

    if not email_flag:
        print('Email format wrong')
        error_code = 1
    elif not card_flag:
        print('Card format wrong')
        error_code = 2
    elif not date_flag:
        print('Your credit card is expired')
        error_code = 3
    elif not stock_flag:
        print('Sorry! Some product in your cart is sold out')
        error_code = 4
    else:
        for item in cart:
            update_database(item)
   
    return(error_code)


