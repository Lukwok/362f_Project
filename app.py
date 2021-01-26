import mysql.connector
import sqlite3
import base64
import bottle
import urllib.parse as urlparse
from owner import replenish_stock
from cart import shopping_cart
from database import database
from pay import finish_payment
from urllib.parse import parse_qs
from bottle import Bottle, request, route, run, template, response
from mysql.connector import errorcode

#create shopping cart
app = Bottle()
#my_cart = shopping_cart()

@app.route('/')
def index():
  #create shopping cart
  new_cart = shopping_cart()
  response.set_cookie("cart", new_cart, secret='I-wanna-pass-362f')
  #default user is guest (2)
  response.set_cookie("user_id", "NA", secret='when-sem-break')
  return template("""
      <script>
        window.location.href = '/login';
      </script>
    """)
  

  #my_cart = request.get_cookie("cart", secret='I-wanna-pass-362f')

@app.route('/login')
def login():
  new_cart = shopping_cart()
  response.set_cookie("cart", new_cart, secret='I-wanna-pass-362f')
  output = template('template/login')
  return output

@app.route('/logout')
def logout():
  return template("""
      <script>
        window.location.href = '/';
      </script>
    """)
@app.route('/logincheck',method="POST")
def logincheck():
  my_username = str(request.forms.get('username'))

  try:
    query = "SELECT iduser FROM user WHERE username ='"+my_username+"'"
    data=database(query)
    my_userId = data[0][0]
    response.set_cookie("user_id",int(my_userId), secret='when-sem-break')
    response.set_cookie("user_name",str(my_username), secret='no-program-but-travel')
    return template("""
      <script>
        window.location.href = '/home';
      </script>
    """)

  except:
    return template("""
      <script>
        alert("Your username is wrong!! Please enter 'guest' if you don't have username");
        window.location.href = '/login';
      </script>
    """)


@app.route('/home')
def home():
  query="Select * from catalogue"
  data = database(query)
  my_userid = request.get_cookie("user_id", secret='when-sem-break')
  my_username = request.get_cookie("user_name", secret='no-program-but-travel')

  info = []
  for (ProductID, Name, Price, Quantity,Image) in data:
      #image = Image.decode('base64')
      image= base64.b64encode(Image).decode('utf-8')
      info.append((ProductID, Name, Price, Quantity, image))
  
  try:
    if not (int(my_userid)== 1):
      output = template('template/display', rows=info,name=my_username)
      return output
    elif (int(my_userid)== 1):
      output = template('template/display_owner', rows=info,name=my_username)
      return output
  except:
    output = template('template/loginagain')
    return output

  #db.close()

@app.route('/detail', method='GET')
def detail_handle():
  product_id = request.GET.get('id')
  my_userid = request.get_cookie("user_id", secret='when-sem-break')
  my_username = request.get_cookie("user_name", secret='no-program-but-travel')
  query = "Select * from catalogue where ProductID = {}".format(product_id)
  data = database(query)

  info = []
  for (ProductID, Name, Price, Quantity,Image) in data:
      #image = Image.decode('base64')
      image= base64.b64encode(Image).decode('utf-8')
      info.append((ProductID, Name, Price, Quantity, image))

  try:
    if not (int(my_userid)== 1):
      output = template('template/detail', rows=info, name=my_username)
      return output
    elif (int(my_userid)== 1):
      output = template('template/detail_owner', rows=info, name=my_username)
      return output
  except:
    output = template('template/loginagain')
    return output

@app.route('/cart')
def cart_show():
  my_cart = request.get_cookie("cart", secret='I-wanna-pass-362f')
  my_userid = request.get_cookie("user_id", secret='when-sem-break')
  my_username = request.get_cookie("user_name", secret='no-program-but-travel')
  try:
    if not (int(my_userid)== 1):
      output = template('template/shopping', cart = my_cart, name=my_username)
      return output
  except:
    output = template('template/loginagain')
    return output

@app.route('/cart',method='POST')
def cart():
    my_cart = request.get_cookie("cart", secret='I-wanna-pass-362f')
    my_username = request.get_cookie("user_name", secret='no-program-but-travel')

    my_id = request.forms.get('id')
    my_number = request.forms.get('number')
    my_cart.add_to_cart(my_id,my_number)

    response.set_cookie("cart", my_cart, secret='I-wanna-pass-362f')
    print(my_cart.get_cart())

    output = template('template/shopping', cart = my_cart,name=my_username)
    return output

@app.route('/update',method="POST")
def owner_update_handle():
  my_id = request.forms.get('id')
  my_number = request.forms.get('number')
  return replenish_stock(my_id,my_number)
  #replenish_stock(my_id,my_price,my_number)


@app.route('/delete', method='GET')
def delete_handle():
    my_cart = request.get_cookie("cart", secret='I-wanna-pass-362f')

    product_id = request.GET.get('id')
    my_cart.remove_from_cart(product_id)

    response.set_cookie("cart", my_cart, secret='I-wanna-pass-362f')
    print(my_cart.get_cart())

    return template("""
      <script>
        window.location.href = '/cart';
      </script>
    """)

@app.route('/edit',method='POST')
def edit_handle():
  my_cart = request.get_cookie("cart", secret='I-wanna-pass-362f')
  #Update 
  for thing in my_cart.get_cart():
    updateInput = "{}_number".format(thing.item_id)
    my_number = request.forms.get(updateInput)
    my_cart.update_from_cart(thing.item_id,my_number)
    

  response.set_cookie("cart", my_cart, secret='I-wanna-pass-362f')
  print(my_cart.get_cart())

  output = template('template/edit')
  return output

@app.route('/checkout',method='POST')
def checkout():
  my_cart = request.get_cookie("cart", secret='I-wanna-pass-362f')
  #Update 
  for thing in my_cart.get_cart():
    updateInput = "{}_number".format(thing.item_id)
    my_number = request.forms.get(updateInput)
    my_cart.update_from_cart(thing.item_id,my_number)

  response.set_cookie("cart", my_cart, secret='I-wanna-pass-362f')
  print(my_cart.get_cart())

  output = template('template/payment',cart = my_cart)
  return output
  
@app.route('/history')
def shoppingRecord():
  output = template('template/history')
  return output

@app.route('/paymentStatus',method='POST')
def paymentStatus():
  my_cart = request.get_cookie("cart", secret='I-wanna-pass-362f')
  my_email = request.forms.get('email')
  my_card_number = request.forms.get('cardnumber')
  my_card_date = request.forms.get('exp')

  status = finish_payment(my_email,my_card_number,my_card_date,my_cart.get_cart())
  
  #switch case
  if status == 1: #email error
    return template("""
      <script>
        alert("Email format wrong");
        window.history.back();
      </script>
    """)

  elif status == 2: #card-num error
    return template("""
      <script>
        alert("Your card number is not valid");
        window.history.back();
      </script>
    """)

  elif status == 3: #exp error
    return template("""
      <script>
        alert("Your credit card is expired");
        window.history.back();
      </script>
    """)

  elif status == 4: #stock error
    return template("""
      <script>
        alert("Sorry! Some product in your cart is sold out");
        window.location.href='/history';
      </script>
    """)

  elif status == 0: #no error
    new_cart = shopping_cart()
    response.set_cookie("cart", new_cart, secret='I-wanna-pass-362f')
    return template("""
      <script>
        alert("Thank you for buying");
        window.location.href='/history';
      </script>
    """)
  
app.run(server='paste')
# application = bottle.default_app()
# from paste import httpserver
# httpserver.serve(application, host='0.0.0.0', port=80)