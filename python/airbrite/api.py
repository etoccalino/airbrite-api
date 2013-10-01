# TODO: define a manager to handle paging for the resources.


class Product (object):

    def __init__(self, data={}):
        self._id = ''
        self.name = ''
        self.description = ''
        self.inventory = None
        self.metadata = {}
        self.created = 0
        self.updated = 0
        self.weight = None

        # This should be datetime objects
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
        self.created = data[u'created']
        self.updated = data[u'updated']
        self.weight = data[u'weight']

        # This should be datetime objects
        self.created_date = data[u'created_date']
        self.updated_date = data[u'updated_date']

        self.user_id = data[u'user_id']

        # TODO: reimplement __repr__ and __str__ to avoid this reference
        self._data = data

    def __repr__(self):
        """Show data as a dict"""
        return repr(self._data)

    def __str__(self):
        # TODO: make it more user-friendly.
        return repr(self)


###############################################################################

class Order (object):

    def __init__(self, data={}):

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
        self.created = data[u'created']
        self.updated = data[u'updated']
        self.weight = data[u'weight']

        # This should be datetime objects
        self.created_date = data[u'created_date']
        self.updated_date = data[u'updated_date']

        self.user_id = data[u'user_id']

        # TODO: reimplement __repr__ and __str__ to avoid this reference
        self._data = data

    def __repr__(self):
        """Show data as a dict"""
        return repr(self._data)

    def __str__(self):
        # TODO: make it more user-friendly.
        return repr(self)
