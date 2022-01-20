_match = 'match'
_query = 'query'
_analyzer = 'analyzer'
_boost = 'boost'
_fuzziness = 'fuzziness'
_operator = 'operator'
_minimum_should_match = 'minimum_should_match'
_zero_terms_query = 'zero_terms_query'
_cutoff_frequency = 'cutoff_frequency'
_rewrite = 'rewrite'
_prefix_length = 'prefix_length'
_max_expansions = 'max_expansions'

class Match(object):
    """
    전체 텍스트 쿼리를 수행하기 위한 기본 쿼리 (fuzzy 매치와 phrase, 근접 쿼리를 포함) 
    쉽게 말해 전체 텍스트에서 특정 부분이 포함되는지 여부를 확인하는데 
    fuzzy를 이용하여 유사도가 어느정도 되는 쿼리들도 조회 가능
    """
     
    def __init__(self, field, value):
        
        self.field = field
        
        self.query = dict()
        self.query[_match] = dict()
        self.query[_match][field] = dict()
        self.query[_match][field][_query] = value

    def analyzer(self, value):
        self.query[_match][self.field][_analyzer] = value
        return self
    
    def boost(self, value=1):
        self.query[_match][self.field][_boost] = value
        return self

    def fuzziness(self, value):
        self.query[_match][self.field][_fuzziness] = value
        return self

    def operator(self, value):
        self.query[_match][self.field][_operator] = value
        return self
    
    def minimum_should_match(self, value):
        self.query[_match][self.field][_minimum_should_match] = value
        return self

    def zero_terms_query(self, value):
        self.query[_match][self.field][_zero_terms_query] = value
        return self
        
    def cutoff_frequency(self, value):
        self.query[_match][self.field][_cutoff_frequency] = value
        return self

    def rewrite(self, value):
        self.query[_match][self.field][_rewrite] = value
        return self

    def prefix_length(self, value):
        self.query[_match][self.field][_prefix_length] = value
        return self

    def max_expansions(self, value):
        self.query[_match][self.field][_max_expansions] = value
        return self


    def build(self):
        return self.query


if __name__ == "main":
    print("Query Test")