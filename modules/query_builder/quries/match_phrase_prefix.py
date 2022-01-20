
_match_phrase_prefix= '_match_phrase_prefix'
_query = 'query'
_analyzer = 'analyzer'
_boost = 'boost'
_max_expansions = 'max_expansions'
_zero_terms_query = 'zero_terms_query'
_slop = 'slop'


class MatchPhrasePrefix(object):
    """
    match phrase 와 비슷하지만 마지막 단어에 와일드 카드가 사용된다. (자동완성 기능에서 자주 사용)
    """
    def __init__(self, field, value):
        self.field = field
        self.query = dict()
        self.query[_match_phrase_prefix] = dict()
        self.query[_match_phrase_prefix][field][_query] = value

    def analyzer(self, value):
        self.query[_match_phrase_prefix][self.field][_analyzer] = value
        return self

    def boost(self, value):
        self.query[_match_phrase_prefix][self.field][_boost] = value
        return self
        
    def max_expansions(self, value):
        self.query[_match_phrase_prefix][self.field][_max_expansions] = value
        return self
        
    def slop(self, value):
        self.query[_match_phrase_prefix][self.field][_slop] = value
        return self
        
    def zero_terms_query(self, value):
        self.query[_match_phrase_prefix][self.field][_zero_terms_query] = value
        return self
        
    def build(self):
        return self.query
    
