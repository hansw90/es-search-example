
_wildcard = 'wildcard'
_value = 'value'
_boost = 'boost'
_rewrite = 'rewrite'

class WildCard(object):
    """
    와일드 카드 *,? 를 사용하여 검색하는 방법, 전체를 다 뒤져서 찾아야 하기 때문에 성능에 좋지 못하다.
    ex) hel* or hel?o
    """
    
    def __init__(self, field, value):
        self.field = field
        self.query = dict()
        self.query[_wildcard] = dict()
        self.query[_wildcard][self.field] = dict()
        self.query[_wildcard][self.field][_value] = value
        
    def boost(self, value):
        self.query[_wildcard][self.field][_boost] = value
        return self

    # rewrite param
    # https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-multi-term-rewrite.html
    def rewrite(self, value):
        self.query[_wildcard][self.field][_rewrite] = value
        return self

    def build(self):
        return self.query