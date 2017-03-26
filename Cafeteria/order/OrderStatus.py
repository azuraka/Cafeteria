"""
It represents different possible Order status used in the application
"""

class OrderStatus(object):
    #When the order is not placed with payment
    DRAFT = "DRAFT"

    #When the Order is placed and paid by customer and awaiting for acceptance from attender
    AWAITING_ACCEPTANCE = "AWAITING_ACCEPTANCE"

    #When the order is accepted by the attender
    ACCEPTED = "ACCEPTED"

    #When the attender decline/cancel the order
    DECLINED = "DECLINED"

    #When the user cancel the order
    CANCELLED = "CANCELLED"

    #When the order is dispatched from cafeteria then this status will be updated by attender
    DISPATCHED = "DISPATCHED"

    #When the order is with delivery boy and order is in trasit
    IN_TRANSIT = "IN_TRANSIT"

    #When the order is reached to destination/customer
    COMPLETED = "COMPLETED"