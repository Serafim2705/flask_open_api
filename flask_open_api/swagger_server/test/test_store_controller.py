# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.order import Order  # noqa: E501
from swagger_server.models.position_in_order import PositionInOrder  # noqa: E501
from swagger_server.test import BaseTestCase


class TestStoreController(BaseTestCase):
    """StoreController integration test stubs"""

    def test_delete_order(self):
        """Test case for delete_order

        Delete purchase order by ID
        """
        response = self.client.open(
            '/api/v3/store/order/{orderId}'.format(order_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_order_by_id(self):
        """Test case for get_order_by_id

        Find purchase order by ID
        """
        response = self.client.open(
            '/api/v3/store/order/{orderId}'.format(order_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_place_order(self):
        """Test case for place_order

        Place an order for a pizza
        """
        body = Order()
        data = dict(id=789,
                    positions=PositionInOrder(),
                    ship_date='2013-10-20T19:20:30+01:00',
                    price=1.2,
                    status='status_example',
                    complete=true)
        response = self.client.open(
            '/api/v3/store/order',
            method='POST',
            data=json.dumps(body),
            data=data,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_store_create_position_post(self):
        """Test case for store_create_position_post

        Create positions for order
        """
        body = PositionInOrder()
        data = dict(pizza_id=None,
                    quantity=56,
                    price=1.2,
                    discount=1.2)
        response = self.client.open(
            '/api/v3/store/CreatePosition',
            method='POST',
            data=json.dumps(body),
            data=data,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
