class GeoBoundingBox(object):
    """
    사각범위
    """
    def __init__(self, field):
        self.field = field
        self._query = dict()
        self._query['geo_bounding_box'] = dict()
        self._query['geo_bounding_box'][field] = dict()


    def top_left(self, value):
        self._query['geo_bounding_box'][self.field]['top_left'] = value
        return self

    def bottom_right(self, value):
        self._query['geo_bounding_box'][self.field]['bottom_right'] = value
        return self

    def build(self):
        return self._query

