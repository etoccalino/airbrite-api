import unittest
import airbrite
import airbrite.api

CURRENT_END_POINT = 'https://api.airbrite.io/v2/'


class ConnectionTestCase(unittest.TestCase):

    def test_defaults_to_test_API_KEY(self):
        self.assertEqual(airbrite.API_KEY, airbrite.TEST_API_KEY)

    def test_endpoint(self):
        self.assertEqual(airbrite.END_POINT, CURRENT_END_POINT)

    def test_can_connect(self):
        ret = airbrite.test_connection()
        self.assertTrue(ret)


class ProductTestCase(unittest.TestCase):
    """Test the actual Product, not its REST endpoint functionality"""

    DATA = {
        u'_id': u'5237a50459459f0500000007',
        u'created': 1379378436,
        u'created_date': u'2013-09-17T00:40:36.649Z',
        u'description': u'My First Product',
        u'inventory': None,
        u'metadata': {},
        u'name': None,
        u'sku': u'first-product',
        u'updated': 1379378436,
        u'updated_date': u'2013-09-17T00:40:36.649Z',
        u'user_id': u'5237a347429acf0400000013',
        u'weight': None
    }

    MY_FIRST_PRODUCT_ID = u'5237a50459459f0500000007'

    def test_instance_id(self):
        product = airbrite.api.Product()
        product._from_data(self.DATA)
        self.assertEqual(product._id, self.MY_FIRST_PRODUCT_ID)


class RESTProductTestCase(unittest.TestCase):
    """Test the 'products' frontend to the REST interface"""

    MY_FIRST_PRODUCT_ID = u'5237a50459459f0500000007'

    def test_get_product(self):
        product = airbrite.get_product(self.MY_FIRST_PRODUCT_ID)
        self.assertIsNotNone(product)
        self.assertEqual(product._id, self.MY_FIRST_PRODUCT_ID)

    def test_get_products(self):
        """The products can be iterated over"""
        products = airbrite.get_products()
        self.assertIsNotNone(products)
        self.assertTrue(hasattr(products, 'next'))

    def test_get_products_test_all(self):
        """The test API key has a single product"""
        # len() is not yet supported, so we exhaust the iterator.
        products = airbrite.get_products()
        ps = []
        for product in products:
            ps.append(product)

        self.assertEqual(len(ps), 1)
        self.assertEqual(ps[0]._id, self.MY_FIRST_PRODUCT_ID)


# class OrderTestCase(unittest.TestCase):
#     """Test the actual Order, not its REST endpoint functionality"""

#     def test_order(self):


class RESTOrderTestCase(unittest.TestCase):
    """Test the 'orders' frontend to the REST interface"""

    ORDER_SKU = 'first-product'
    ORDER_QUANTITY = 'first-product'

    def test_new_order(self):
        order = airbrite.new_order(sku=self.ORDER_SKU,
                                   quantity=self.ORDER_QUANTITY)
        self.assertIsNotNone(order)
        self.assertEqual(order.sku, self.ORDER_SKU)
        self.assertEqual(order.quantity, self.ORDER_QUANTITY)
