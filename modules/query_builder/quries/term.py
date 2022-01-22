from re import L


_term = 'term'
_value = 'value'
_boost = 'boost'
_case_insensitive = 'case_insensitive'

class Term(object):
    
    """
    term query
    검색하고자 하는 필드에 정확한 텀을 포함하고 있는지 확인하는 쿼리
    """
    
    def __init__(self, field, value):
        self.query = dict() 
        self.query[_term][field][_value] = value

    def boost(self, value):
        self.query[_term][_boost] = value
        return self

    def case_insensitive(self, value):
        self.query[_term][_case_insensitive] = value
        return self
    
    def build(self):
        return self.query
