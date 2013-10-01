# Creating an Order

This tutorial describes how you can create orders with the python interface to Airbrite's API. If you need help, refer to our python interface documentation or email support@airbriteinc.com.

* [Setup](#setup)
* [Create a Simple Order](#create-a-simple-order)
* [Create an Order with One-Time Payment](#create-an-order-with-one-time-payment)
* [Create a Pre-Order](#create-a-pre-order)


## Setup

The Airbrite's API can be access through the Python interactive interpreter. You'll be running all the turorials in an interactive session:

    python
    >>> import airbrite

The python interface will be setup to use an test API key that we've provided, so you can test right away. The tutorials assume you have a test connection ready, as above.

## Create a Simple Order

This order does not have any payment attached to it.

__Step 1: Make sure you've created a Product__

To get started, let's double check that you have at least one product in Airbrite. Make the following request:

    >>> for product in airbrite.products():
    >>>    print product

We have a product called "My First Product" with the SKU "first-product". We'll be creating orders with "first-product".

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> SO FAR <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


__Step 2: Create your Order__

Next, we'll attempt to order 1 item of "first-product".

curl https://api.airbrite.io/v2/orders \
    -u sk_test_a805be8b2add854f09976b3b5c0f5bd06c14617c: \
    -d "line_items[0][sku]=first-product"\
    -d "line_items[0][quantity]=1"

If successful, you should receive a response similar to:

    {
        "meta": {
            "code": 200,
            "env": "test"
        },
        "data": {
            "user_id": "5237a347429acf0400000013",
            "_id": "5237a8e7a1b644040000000d",
            "line_items": [
                {
                    "sku": "first-product",
                    "quantity": "1",
                    "price": "995",
                    "description": "My First Product",
                    "name": null,
                    "weight": null,
                    "inventory": null,
                    "metadata": {}
                }
            ],
            "customer_id": null,
            "shipping_address": null,
            "shipping": {},
            "tax": {},
            "discount": {},
            "currency": "usd",
            "status": null,
            "description": null,
            "metadata": {},
            "created": 1379379432,
            "created_date": "2013-09-17T00:57:12.007Z",
            "updated": 1379379432,
            "updated_date": "2013-09-17T00:57:12.008Z",
            "order_number": 1001,
            "payments": [],
            "shipments": []
        }
    }

## Create an Order with One-Time Payment



## Create a Pre-Order
