
_match_phrase = 'match_phrase'
_query = 'query'
_analyzer = 'analyzer'
_boost = 'boost'
_zero_terms_query = 'zero_terms_query'
_max_expansions = 'max_expansions'
_slop = 'slop'

class MatchPhrase(object):
    """
    입력을 analyze 한다. 그리고 다음의 조건을 충족하는 document를 반환한다.
    - 모든 term들이 field에 존재해야 한다. 
    - 모든 term들이 입력된 순서에 맞게 존재한다. 
    """
    def __init__(self, field, value):
        self.field = field

        self.query = dict()
        self.query[_match_phrase] = dict()
        self.query[_match_phrase][field][_query] = value


    def analyzer(self, value):
        self.query[_match_phrase][self.field][_analyzer] = value
        return self

    def boost(self, value):
        self.query[_match_phrase][self.field][_boost] = value
        return self

    def max_expansions(self, value):
        self.query[_match_phrase][self.field][_max_expansions] = value
        return self
    
    def slop(self, value):
        self.query[_match_phrase][self.field][_slop] = value
        return self
        
    def zero_terms_query(self, value):
        self.query[_match_phrase][self.field][_zero_terms_query] = value
        return self

    def build(self):
        return self.query