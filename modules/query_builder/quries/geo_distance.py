class GeoDistance(object):
    """
    반경 원 범위
    """
    def __init__(self, field):
        self.field = field
        self._query = dict()
        self._query['geo_distance'] = dict()
        self._query['geo_distance'][field] = dict()

        self.lat = None
        self.lon = None
    
    def lat(self, value):
        self.lat = value
        return self
    
    def lon(self, value):
        self.lon = value
        return self

    def distance(self, value):
        self._query['geo_distance']['distance'] = value
        return self

    def build(self):
        _geo = dict()
        _geo['lat'] = self.lat
        _geo['lon'] = self.lon
        self._query['geo_distance'][self.field] = _geo

        return self._query
