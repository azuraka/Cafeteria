"""
This file is to write the test cases related to OrderDao APIs exposed from order module to use in order-view
"""

from django.test import TestCase
from order import OrderDao
from order.models import Order


class OrderDaoTest(TestCase):

    ORDER_NAME = "order_name"
    ORDER_ITEMS = "{'Item1':'2', 'Item2':'1','Item3':'4',}"
    STATUS = "DRAFT"
    RESTAURANT_ID = 101
    ORDER_TYPE = "ONLINE"
    LAST_UPDATE_BY = "test"

    @staticmethod
    def get_order_dao():
        return OrderDao.OrderDao.getInstance()

    def testInsert(self):
        order_dao = self.get_order_dao()
        order = Order()
        order.order_name = self.ORDER_NAME
        order.order_items = self.ORDER_ITEMS
        order.status = self.STATUS
        order.restaurant_id = self.RESTAURANT_ID
        order.order_type = self.ORDER_TYPE
        order.last_update_by = self.LAST_UPDATE_BY
        saved_order = order_dao.insert(order)
        self.assertIsNotNone(saved_order, "order insert returns null object")
        self.assertTrue(saved_order.order_id>0, "order id is less then or equals to 0")
        self.assertEqual(order.order_name,saved_order.order_name, "Stored order name do not match!")
