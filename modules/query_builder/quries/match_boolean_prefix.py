_match_boolean_prefix = 'match_boolean_prefix'
_query = 'query'

_analyzer = 'analyzer'
_fuzziness = 'fuzziness'
_operator = 'operator'
_minimum_should_match = 'minimum_should_match'
_max_expansions = 'max_expansions'
_prefix_length = 'prefix_length'

class MatchBooleanPrefix(object):
    """
    match_boolean_prefix
    마지막 term을 제외한 모든 term은 term query에 사용된다. 마지막 term은 prefix query에 사용된다.
    match_boolean_prefix는 match_phrase_prefix와 상당히 유사하지만 match_phrase_prefix는 입력값을 phrase로 보고 쭉 이어진 하나의 검색을 하는 반면
    match_boolean_prefix는 term단위 검색으로 서로 떨어져있어도 되고, 순서가 바뀌어도 가능하다.
    """
    
    def __init__(self, field, value):
        self.field = field
        self.query = dict()
        self.query[_match_boolean_prefix] = dict()
        self.query[_match_boolean_prefix][field][_query] = value

    def analyzer(self, value):
        self.query[_match_boolean_prefix][self.field][_analyzer] = value
        return self

    def minimum_should_match(self, value):
        self.query[_match_boolean_prefix][self.field][_minimum_should_match] = value
        return self
    
    def operator(self, value):
        self.query[_match_boolean_prefix][self.field][_operator] = value
        return self

    def fuzziness(self, value):
        self.query[_match_boolean_prefix][self.field][_fuzziness] = value
        return self
    
    def prefix_length(self, value):
        self.query[_match_boolean_prefix][self.field][_prefix_length] = value
        return self

    def max_expansions(self, value):
        self.query[_match_boolean_prefix][self.field][_max_expansions] = value
        return self

    def build(self):
        return self.query

    