_multi_match = 'multi_match'
_query = 'query'

_analyzer = 'analyzer'
_fuzziness = 'fuzziness'
_operator = 'operator'
_minimum_should_match = 'minimum_should_match'
_max_expansions = 'max_expansions'
_zero_terms_query = 'zero_terms_query'
_prefix_length = 'prefix_length'
_fields = 'fields'
_type = 'type'
_cutoff_frequency = 'cutoff_frequency'
_rewrite = 'rewrite'
_boost = 'boost'

class MultiMatch(object):
    
    def __init__(self, fields:list(), value):
        
        self.query = dict()
        self.query[_multi_match] = dict()

        self.query[_multi_match][_fields] = fields
        self.query[_multi_match][_query] = value

    def type(self, value):
        self.query[_multi_match][_type] = value
        return self

    def operator(self, value):
        self.query[_multi_match][_operator] = value
        return self
        
    def zero_terms_query(self, value):
        self.query[_multi_match][_zero_terms_query] = value
        return self
        
    def cutoff_frequency(self, value):
        self.query[_multi_match][_cutoff_frequency] = value
        return self
        
    def boost(self, value):
        self.query[_multi_match][_boost] = value
        return self

    def rewrite(self, value):
        self.query[_multi_match][_rewrite] = value
        return self

    def prefix_length(self, value):
        self.query[_multi_match][_prefix_length] = value
        return self

    def fuzziness(self, value):
        self.query[_multi_match][_fuzziness] = value
        return self

    def minimum_should_match(self, value):
        self.query[_multi_match][_minimum_should_match] = value
        return self

    def analyzer(self, value):
        self.query[_multi_match][_analyzer] = value
        return self

    def max_expansions(self, value):
        self.query[_multi_match][_max_expansions] = value
        return self

    def build(self):
        return self.query