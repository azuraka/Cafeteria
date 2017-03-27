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
    RESTAURANT_ID = "101"
    ORDER_TYPE = "ONLINE"
    LAST_UPDATE_BY = "test"
    CUSTOMER_ID = "my_customer_id"

    @staticmethod
    def get_order_dao():
        return OrderDao.OrderDao.getInstance()

    #Creates an order for testing - this order is not saved in DB
    def create_order(self):
        order = Order()
        order.order_name = self.ORDER_NAME
        order.order_items = self.ORDER_ITEMS
        order.status = self.STATUS
        order.restaurant_id = self.RESTAURANT_ID
        order.order_type = self.ORDER_TYPE
        order.last_update_by = self.LAST_UPDATE_BY
        order.customer_id = self.CUSTOMER_ID
        return order

    def assertOrders(self, expected, actual, message):
        self.assertEqual(expected.order_name, actual.order_name, "order_name do not match"+message)
        self.assertEqual(expected.order_items, actual.order_items, "order_items do not match" + message)
        self.assertEqual(expected.status, actual.status, "status do not match" + message)
        if expected.restaurant_id is not None or actual.restaurant_id is not None:
            self.assertEqual(expected.restaurant_id, actual.restaurant_id, "restaurant_id, expected:<"+str(expected.restaurant_id)+">actual:<" + str(actual.restaurant_id)+">" + message)
        self.assertEqual(expected.order_type, actual.order_type, "order_type do not match" + message)
        self.assertEqual(expected.last_update_by, actual.last_update_by, "last_update_by do not match" + message)
        if expected.customer_id is not None or actual.customer_id is not None:
            self.assertEqual(expected.customer_id, actual.customer_id, "customer_id, expected:<"+str(expected.customer_id)+">actual:<" + str(actual.customer_id)+">" + message)

    def test_insert(self):
        order_dao = self.get_order_dao()
        order = self.create_order()
        saved_order = order_dao.insert(order)
        self.assertIsNotNone(saved_order, "order insert returns null object")
        self.assertTrue(saved_order.order_id>0, "order id is less then or equals to 0")
        self.assertOrders(order, saved_order, "something wrong in test_insert")
        #self.assertEqual(order.order_name,saved_order.order_name, "Stored order name do not match!")

    def test_update(self):
        order_dao = self.get_order_dao()
        order = self.create_order()
        saved_order = order_dao.insert(order)
        updated_name = "New Order Name"
        saved_order.order_name = updated_name
        updated_order = order_dao.update(saved_order)
        self.assertEqual(updated_order.order_name, updated_name, "update of an order name failed")

    def test_get_all_orders(self):
        order_dao = self.get_order_dao()
        order = self.create_order()
        order_dao.insert(order)
        self.assertEqual(order_dao.get_all_orders().count(), 1, "Number of loaded orders differs from actual")

    def test_find_by_id(self):
        order_dao = self.get_order_dao()
        order = self.create_order()
        order = order_dao.insert(order)
        db_order = order_dao.find_by_id(order.order_id)
        self.assertIsNotNone(db_order, "duhduhduh, didn't find data in db :(")
        self.assertOrders(order, db_order, "something wrong here in find_by_id")
        db_order = order_dao.find_by_id(10101)
        self.assertIsNone(db_order, "duhduhduh, find some fake data in db :(")

    def test_find_by_name(self):
        order_dao = self.get_order_dao()
        order = self.create_order()
        order = order_dao.insert(order)
        db_order = order_dao.find_by_name(order.order_name)
        self.assertIsNotNone(db_order, "duhduhduh, didn't find data in db :(")
        self.assertOrders(order, db_order.first(), "something wrong here in find_by_id")
        db_order = order_dao.find_by_name("some_random_name")
        self.assertTrue(db_order.count() == 0, "duhduhduh, find some fake data in db :(")

    def test_find_by_customer_id(self):
        order_dao = self.get_order_dao()
        order = self.create_order()
        order = order_dao.insert(order)
        db_order = order_dao.find_by_customer_id(order.customer_id)
        self.assertIsNotNone(db_order, "duhduhduh, didn't find data in db :(")
        self.assertOrders(order, db_order.first(), "something wrong here in find_by_customer_id")
        db_order = order_dao.find_by_customer_id("some_random_name")
        self.assertTrue(db_order.count() == 0, "duhduhduh, find some fake data in db :(")

    def test_find_by_restaurant_id(self):
        order_dao = self.get_order_dao()
        order = self.create_order()
        order = order_dao.insert(order)
        db_order = order_dao.find_by_restaurant_id(order.restaurant_id)
        self.assertIsNotNone(db_order, "duhduhduh, didn't find data in db :(")
        self.assertOrders(order, db_order.first(), "something wrong here in find_by_restaurant_id")
        db_order = order_dao.find_by_restaurant_id("some_random_restaurant_id")
        self.assertTrue(db_order.count() == 0, "duhduhduh, find some fake data in db :(")

    def test_delete(self):
        order_dao = self.get_order_dao()
        order = self.create_order()
        order = order_dao.insert(order)
        self.assertEqual(order_dao.get_all_orders().count(), 1, "order didn't saved in db")
        order_dao.delete(order)
        self.assertEqual(order_dao.get_all_orders().count(), 0, "order didn't get deleted in db")
