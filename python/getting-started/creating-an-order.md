# Creating an Order

This tutorial describes how you can create orders with the python interface to Airbrite's API. If you need help, refer to our python interface documentation or email support@airbriteinc.com.

* [Setup](#setup)
* [Create a Simple Order](#create-a-simple-order)
* [Create an Order with One-Time Payment](#create-an-order-with-one-time-payment)
* [Create a Pre-Order](#create-a-pre-order)


## Setup

First you will have to install the python interface to Airbrite's API in your system (or virtual environment):

    >>> pip install airbrite

Airbrite's API can be accessed through the Python interactive interpreter. You'll be running all the turorials in an interactive session:

    python
    >>> import airbrite

The python interface will be setup to use a test API key that we've provided, so you can test right away. The tutorials assume you have a test connection ready, as in the example above.

## Create a Simple Order

This order does not have any payment attached to it.

__Step 1: Make sure you've created a Product__

To get started, let's double check that you have at least one product in Airbrite. Make the following request:

    >>> for product in airbrite.get_products():
    >>>    print product.sku, product.description

We have a product called "My First Product" with the SKU "first-product". We'll be creating orders with "first-product".

__Step 2: Create your Order__

Next, we'll attempt to order 1 item of "first-product".

    >>> order = airbrite.new_order(sku='first-product', quantity=1)
    >>> order

If successful, you should receive a response similar to:

    >>> <Order (xxx)>

To have a quick look at the data catched by the order object:

    >>> from pprint import pprint
    >>> pprint(order.to_dict())
    {u'_id': u'524c360b1382340700000029',
    u'created': 1380726283,
    u'created_date': u'2013-10-02T15:04:43.879Z',
    u'currency': u'usd',
    u'customer_id': None,
    u'description': None,
    u'discount': {},
    u'line_items': [{u'description': u'My First Product',
                     u'inventory': None,
                     u'metadata': {},
                     u'name': None,
                     u'quantity': 1,
                     u'sku': u'first-product',
                     u'updated': 1379378436,
                     u'updated_date': u'2013-09-17T00:40:36.649Z',
                     u'weight': None}],
    u'metadata': {},
    u'order_number': 1361,
    u'shipping': {},
    u'shipping_address': None,
    u'status': None,
    u'tax': {},
    u'updated': 1380726283,
    u'updated_date': u'2013-10-02T15:04:43.880Z',
    u'user_id': u'5237a347429acf0400000013'}

## Creating an order with one-time payment

To create an order and charge the payment card, we'll be using [Stripe](https://www.stripe.com) to process the payment. [Get a test Stripe token](https://dash.airbrite.io/stripe.html) and replace {tok_xxxxxxxxxxxxxxx} below.

    >>> item = { "sku": "first-product", "quantity": 1 }
    >>> payment = airbrite.payment(card_token="{tok_xxxxxxxxxxxxxxx}", amount=100)
    >>> order = airbrite.new_order(line_items=[item], payments=[payment])

## Creating A Pre-Order

TBD
