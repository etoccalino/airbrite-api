import requests
import api

END_POINT = 'https://api.airbrite.io/v2/'

TEST_API_KEY = 'sk_test_a805be8b2add854f09976b3b5c0f5bd06c14617c'
API_KEY = TEST_API_KEY


def _get(location):
    return requests.get(END_POINT + location, auth=(API_KEY, ''))


def test_connection():
    """Returns True if the API is operational, False otherwise"""
    # TODO: implement a cheaper test

    # Connection test based on assumption that the test API key is used, and
    # that there's at least one product registered.
    result = _get('products')
    if result.status_code == 200:
        return True
    return False


###############################################################################

def get_product(product_id):
    """Returns an api.Product object for the provided ID"""

    response = _get('products/' + product_id)
    if response.status_code != 200:
        raise Exception('Product not found')
    product_data = response.json()[u'data']
    return api.Product(product_data)


def get_products():
    """Returns an iterable of api.Product objects"""

    response = _get('products')
    if response.status_code != 200:
        # TODO: make this a critical error
        raise Exception('Products endpoint failed')

    # TODO: adapt to pagination
    data = response.json()
    for product_data in data[u'data']:
        yield api.Product(product_data)


###############################################################################

def new_order():
    pass
