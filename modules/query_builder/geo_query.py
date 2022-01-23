from quries import geo_bounding_box, geo_distance, geo_shape

class GeoQuery(object):
   """
   ES geo coding 입력 방법은 매우 다양하다, 여기선 보편적으로 많이 쓰는 방법으로 구현한다.
   """
   def __init__(self):
      self._query = dict()
   
   # 사각범위
   def geo_bounding_box(self, field):
      return geo_bounding_box.GeoBoundingBox(field)
   
   # 반경 원 범위
   def geo_distance(self, distance, field, geo):
      return geo_distance.GeoDistance()

   # 단일 점
   def geo_shape(self, field, coordinates, _type, relation=None):
      return geo_shape.GeoShape()


if __name__ == '__main__': 
   q = GeoQuery()
   q = q.geo_bounding_box(field='aa').top_left(11).bottom_right(22).build()
   print(q)