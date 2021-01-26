import mysql.connector
from cart import shopping_cart
from database import database
from pay import*

def database_connect_test():
    """
        expect result: Connect to Database Sucessful
    """
    mysql.connector.connect(user='root',password='root',
                              host='127.0.0.1',database='362f')
    print("Connect to Database Sucessful")

def shopping_cart_test():
    """
        expect result: [CartItem(item_id='2', item_name='Sandwich', item_price=8.0, item_quantity=5, count=3),
                        CartItem(item_id='5', item_name='Orange', item_price=3.7, item_quantity=12, count=10)]
                        Sum:61.0
    """
    apple = shopping_cart()     #creat new cart
    apple.add_to_cart(2,3)  #add item in cart 
    apple.add_to_cart(5,6)  #add item in cart 
    apple.add_to_cart(5,4)  #add item in cart
    print (apple.get_cart())
    print ("Sum:{}".format(apple.get_total()))

def remove_shopping_item_test():
    """
        expected result: [CartItem(item_id='2', item_name='Sandwich', item_price=8.00, item_quantity=5, count=3),
                          CartItem(item_id='1', item_name='Apple', item_price=5.00, item_quantity=10, count=4)]
    """
    apple = shopping_cart()     #creat new cart
    apple.add_to_cart(2,3)  #add item in cart 
    apple.add_to_cart(5,6)  #add item in cart 
    apple.add_to_cart(1,4)  #add item in cart
    apple.remove_from_cart(5)   #remove item from cart
    print (apple.get_cart())

def update_shopping_item_test():
    """
    expected result: [CartItem(item_id='2', item_name='Sandwich', item_price=8.00, item_quantity=5, count=3),
                      CartItem(item_id='5', item_name='Orange', item_price=3.7, item_quantity=12, count=4),
                      CartItem(item_id='1', item_name='Apple', item_price=5.0, item_quantity=10, count=10)]
    """
    apple = shopping_cart()     #creat new cart
    apple.add_to_cart(2,3)  #add item in cart 
    apple.add_to_cart(5,6)  #add item in cart 
    apple.add_to_cart(1,4)  #add item in cart
    apple.update_from_cart(5,4)  #update item in cart
    apple.update_from_cart(1,100)  #update item in cart (more than stock)
    print (apple.get_cart())

def email_check_test():
    """
    expected result: True False False False
    """
    email_check('abc@google.com')
    email_check('abc@google@com')
    email_check('abcgoogle.com')
    email_check('abc@google.')

def card_number_check_test():
    """
    expected result: True False False False
    """
    card_check('1111222233334444')
    card_check('1234')
    card_check('abcd')
    card_check('1111-2222-3333')

def exp_check_test():
    """
    expected result: True True False False
    """
    date_check('2026-12')
    date_check('2021-12')
    date_check('2021-01')
    date_check('1111-11')

def stock_check_test():
    """
    expected result: Sorry! Not enough Apple
                     False
    """
    apple = shopping_cart()     #creat new cart
    apple.add_to_cart(2,3)  #add item in cart 
    apple.add_to_cart(1,100)  #add item in cart

    stock_check(apple.get_cart()) 

def main():
    # database_connect_test()
    # shopping_cart_test()
    # remove_shopping_item_test()
    # update_shopping_item_test()
    # email_check_test()
    # card_number_check_test()
    # exp_check_test()
    # stock_check_test()
    return 0


if __name__ == '__main__':
    main()