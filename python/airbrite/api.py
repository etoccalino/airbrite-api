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
        self._id = data[u'_id']
        self.name = data[u'name']
        self.sku = data[u'sku']
        self.description = data[u'description']
        self.inventory = data[u'inventory']
        self.metadata = data[u'metadata']
        self.weight = data[u'weight']

        self.created = data[u'created']
        self.updated = data[u'updated']
        # TODO: This should be datetime objects
        self.created_date = data[u'created_date']
        self.updated_date = data[u'updated_date']

        self.user_id = data[u'user_id']

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
        self._id = data[u'_id']
        self.user_id = data[u'user_id']
        self.customer_id = data[u'customer_id']
        self.order_number = data[u'order_number']
        self.description = data[u'description']

        self.currency = data[u'currency']
        self.discount = data[u'discount']
        self.tax = data[u'tax']

        self.shipping = data[u'shipping']
        self.shipping_address = data[u'shipping_address']
        self.status = data[u'status']

        self.created = data[u'created']
        self.updated = data[u'updated']
        # TODO: This should be datetime objects
        self.created_date = data[u'created_date']
        self.updated_date = data[u'updated_date']

        self.metadata = data[u'metadata']

        # TODO: make this Product instances, or at least Product proxies
        self.line_items = data[u'line_items']

        self.status = data[u'status']

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
