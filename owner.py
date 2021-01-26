from database import database
import mysql.connector
from bottle import Bottle, request, route, run, template, response


def replenish_stock(id,number):
    my_id = int(id)
    new_number = int(number)

    query = 'Update catalogue Set Quantity={} where ProductID={}'.format(str(new_number),str(my_id))

    db = mysql.connector.connect(user='root',password='root',
                              host='127.0.0.1',database='362f')
    print("Connect to Database Sucessful")
    cursor = db.cursor()
    cursor.execute(query)
    cursor.close()
    db.commit()

    print('Updated (Product_id: {} ) Successfully'.format(my_id))

    return template("""
      <script>
        alert("Updated Successfully");
        window.location.href='/home';
      </script>
    """)
