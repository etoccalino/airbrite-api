# TODO: define a manager to handle paging for the resources.


class Product (object):

    def __init__(self, data={}):
        self._id = ''
        self.name = ''
        self.description = ''
        self.inventory = None
        self.metadata = {}
        self.weight = None

        self.created = 0
        self.updated = 0
        # TODO: This should be datetime objects
        self.created_date = ''
        self.updated_date = ''

        self.user_id = ''

        if data:
            self._from_data(data)

    def _from_data(self, data):
        """Initialize the Product instance with the data dict"""
        self._id = data[u'_id'] or self._id
        self.name = data[u'name'] or self.name
        self.sku = data[u'sku'] or self.sku
        self.description = data[u'description'] or self.description
        self.inventory = data[u'inventory'] or self.inventory
        self.metadata = data[u'metadata'] or self.metadata
        self.weight = data[u'weight'] or self.weight

        self.created = data[u'created'] or self.created
        self.updated = data[u'updated'] or self.updated
        # TODO: This should be datetime objects
        self.created_date = data[u'created_date'] or self.created_date
        self.created_date
        self.updated_date = data[u'updated_date'] or self.updated_date

        self.user_id = data[u'user_id'] or self.user_id

        # TODO: reimplement __repr__ and __str__ to avoid this reference
        self._data = data

    def __repr__(self):
        return "<Product (%s)>" % str(self._id)

    def __str__(self):
        # TODO: make it more user-friendly.
        return repr(self.to_dict())

    def to_dict(self):
        return self._data

###############################################################################


class Order (object):

    def __init__(self, data={}):
        self._id = ''
        self.user_id = ''
        self.customer_id = None
        self.order_number = 0
        self.description = ''

        self.currency = ''
        self.discount = {}
        self.tax = {}

        self.shipping = {}
        self.shipping_address = None
        self.status = None

        self.created = 0
        self.updated = 0
        # TODO: This should be datetime objects
        self.created_date = ''
        self.updated_date = ''

        self.metadata = {}
        self.line_items = []
        self.status = None

        if data:
            self._from_data(data)

    def _from_data(self, data):
        """Initialize the Product instance with the data dict"""
        self._id = data[u'_id'] or self._id
        self.user_id = data[u'user_id'] or self.user_id
        self.customer_id = data[u'customer_id'] or self.customer_id
        self.order_number = data[u'order_number'] or self.order_number
        self.description = data[u'description'] or self.description

        self.currency = data[u'currency'] or self.currency
        self.discount = data[u'discount'] or self.discount
        self.tax = data[u'tax'] or self.tax

        self.shipping = data[u'shipping'] or self.shipping
        self.shipping_address = (data[u'shipping_address']
                                 or self.shipping_address)
        self.status = data[u'status'] or self.status

        self.created = data[u'created'] or self.created
        self.updated = data[u'updated'] or self.updated
        # TODO: This should be datetime objects
        self.created_date = data[u'created_date'] or self.created_date
        self.updated_date = data[u'updated_date'] or self.updated_date

        self.metadata = data[u'metadata'] or self.metadata

        # TODO: make this Product instances, or at least Product proxies
        self.line_items = data[u'line_items'] or self.line_items

        self.status = data[u'status'] or self.status

        # TODO: reimplement __repr__ and __str__ to avoid this reference
        self._data = data

    @property
    def quantity(self):
        return len(self.line_items)

    def __repr__(self):
        return "<Order (%s)>" % str(self._id)

    def __str__(self):
        # TODO: make it more user-friendly.
        return repr(self.to_dict())

    def to_dict(self):
        return self._data
