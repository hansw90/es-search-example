_terms = 'terms'
_boost = 'boost'

class Terms(object):
    """
    검색하고자 하는 필드에 정확한 텀들을 포함하고 있는지 확인하는 쿼리
    """
    
    def __init__(self, field, values:list()):
        self.field = field

        self.query = dict() 
        self.query[_terms][field] = values

    def boost(self, value):
        self.query[_terms][self.field][_boost] = value

    def build(self):
        return self.query

    