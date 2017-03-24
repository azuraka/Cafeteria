class OrderDao(object):
    def getAllOrders(self):
        pass
        #Logic goes here to get all orders from order table and return as List of order

    def findById(self, orderId):
        pass
        #Logic goes here to get an Order based on order Id
        #Make sure to validate the orderId(null check or any sanitization)

    def findByName(self, name):
        pass
        # Logic goes here to get an Order based on order name from order table
        # Make sure to validate the name(null check or any sanitization)

    def insert(self, Order):
        pass
        #Insert the order into table here and return the new order obejct return from DB
        #Make sure of any kind of validation

    def delete(self, Order):
        pass
        #Delete the order from table
        #Make sure of any kind of validation

    def update(self, Order):
        pass
        #load the Order from DB by calling findById() and update the order
        #Make sure of validation whether the order exist or not or anyother validation