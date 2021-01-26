from dataclasses import dataclass
from database import database
import mysql.connector


@dataclass
class CartItem:
    """
    Data class for items in cart.
    """
    item_id: str
    item_name: str
    item_price: float
    item_quantity: int
    count: int = 0
    
    # def total_price(self)->float:
    #      return self.item_price*self.count

class shopping_cart():

    def  __init__(self):
        self.cart=[]

    def get_cart(self):
        """
        Helper function for getting all items in a cart.
        Parameters:
        uid (str): The unique ID of an user.
        Output:
        A list of CartItem.
        """
        return self.cart
    
    def get_total(self):
        sum = 0
        for thing in self.cart:
            sum+= thing.item_price*thing.count
        return sum


    def add_to_cart(self,id,count):

        update = False

        for thing in self.cart:
            if str(id) == thing.item_id:
                thing.count = thing.count+int(count)
                update = True
                break

        if not update: 
            query="Select * from catalogue where ProductID={}".format(str(id))
            data = database(query)

            for (ProductID, Name, Price, Quantity,Image) in data:
                item = CartItem(
                    item_id= str(ProductID),
                    item_name = Name,
                    item_price = float(Price), 
                    item_quantity = Quantity,
                    count = int(count),
                    )
            
            self.cart.append(item)
    
    def update_from_cart(self,id,count):
        for thing in self.cart:
            if str(id) == thing.item_id:
                query = "Select Quantity from catalogue where ProductID={}".format(str(id))
                data = database(query)
                updated_quantity = data[0][0]                

                thing.item_quantity = int(updated_quantity)

                #select>quantity => max quantity
                if (int(thing.item_quantity)<int(count)):
                    thing.count = int(thing.item_quantity)
                    return False
                else:
                    thing.count = int(count)
                    return True
                break


    def remove_from_cart(self,id):

        for thing in self.cart:
            if thing.item_id == str(id):
                self.cart.remove(thing)
                break


