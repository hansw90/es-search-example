# 단일 점
class GeoShape(object):

    def __init__(self, field):
        self.field = field

        self._query = dict()
        self._query['geo_shape'] = dict()
        self._query['geo_shage'][self.field] = dict()
        self._query['geo_shage'][self.field]['shape'] = dict()

        self.cordinates = list()

    def type(self, value):
        self._query['geo_shage'][self.field]['shape']['type'] = value
        return self

    def relation(self, value):
        self._query['geo_shage'][self.field]['relation'] = value
        return self

    def cordinate(self, value):
        self.cordinates.append(value)
        return self

    def build(self):
        self._query['geo_shage'][self.field]['shape']['coordinates'] = self.cordinates
        return self._query
