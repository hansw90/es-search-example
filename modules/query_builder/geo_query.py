class GeoQuery(object):
   """
   ES geo coding 입력 방법은 매우 다양하다, 여기선 보편적으로 많이 쓰는 방법으로 구현한다.
   """
   def __init__(self):
      self._query = dict()
   
   def geo(self, lat, lon):
      _geo = dict()
      _geo['lat'] = lat
      _geo['lon'] = lon
      return _geo
   
   # 사각범위
   def geo_bounding_box(self, field, top_left, bottom_right):
      self._query['geo_bounding_box'] = dict()
      self._query['geo_bounding_box'][field] = dict()
      self._query['geo_bounding_box'][field]['top_left'] = top_left
      self._query['geo_bounding_box'][field]['bottom_right'] = bottom_right
      return self._query
   
   # 반경 원 범위
   def geo_distance(self, distance, field, geo):
      self._query['geo_distance'] = dict()
      self._query['geo_distance'][field] = geo
      self._query['geo_distance']['distance'] = distance
      return self._query

   # 단일 점
   def geo_shape(self, field, coordinates, _type, relation=None):
      self._query['geo_shape'] = dict()
      self._query['geo_shage'][field] = dict()
      self._query['geo_shage'][field]['shape']['coordinates'] = coordinates
      
      if _type != None:
         self._query['geo_shage'][field]['shape']['type'] = _type
      
      if relation != None:
         self._query['geo_shage'][field]['relation'] = relation
      
      return self._query
