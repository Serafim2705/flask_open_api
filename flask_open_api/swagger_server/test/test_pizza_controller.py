# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.pizza import Pizza  # noqa: E501
from swagger_server.models.pizzas import Pizzas  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPizzaController(BaseTestCase):
    """PizzaController integration test stubs"""

    def test_add_pizza(self):
        """Test case for add_pizza

        Add a new Pizza to the store
        """
        body = Pizza()
        data = dict(id=789,
                    name='name_example',
                    photo_urls='photo_urls_example')
        response = self.client.open(
            '/api/v3/pizza',
            method='POST',
            data=json.dumps(body),
            data=data,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_pizza(self):
        """Test case for delete_pizza

        Deletes a pizza
        """
        headers = [('api_key', 'api_key_example')]
        response = self.client.open(
            '/api/v3/pizza/{pizzaId}'.format(pizza_id=789),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_pizza_by_id(self):
        """Test case for get_pizza_by_id

        Find pizza by ID
        """
        response = self.client.open(
            '/api/v3/pizza/{pizzaId}'.format(pizza_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_pizza_get(self):
        """Test case for pizza_get

        Show all pizzas
        """
        response = self.client.open(
            '/api/v3/pizza/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_pizza(self):
        """Test case for update_pizza

        Update an existing pizza
        """
        body = Pizza()
        data = dict(id=789,
                    name='name_example',
                    photo_urls='photo_urls_example')
        response = self.client.open(
            '/api/v3/pizza',
            method='PUT',
            data=json.dumps(body),
            data=data,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_pizza_with_form(self):
        """Test case for update_pizza_with_form

        Updates a pizza in the store with form data
        """
        query_string = [('name', 'name_example'),
                        ('status', 'status_example')]
        response = self.client.open(
            '/api/v3/pizza/{pizzaId}'.format(pizza_id=789),
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_upload_file(self):
        """Test case for upload_file

        uploads an image
        """
        body = Object()
        query_string = [('additional_metadata', 'additional_metadata_example')]
        response = self.client.open(
            '/api/v3/pizza/{pizzaId}/uploadImage'.format(pizza_id=789),
            method='POST',
            data=json.dumps(body),
            content_type='application/octet-stream',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
