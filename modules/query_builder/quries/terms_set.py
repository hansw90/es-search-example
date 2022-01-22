
_terms = 'terms'
_terms_set = 'terms_set'
_minimum_should_match_field = 'minimum_should_match_field'

class TermsSet(object):
    """
    지정된 용어중 하나 이상과 일치하는 문서를 찾는다. 지정된 최소값과 일치해야 하는 용어의 수는 필드 또는 스크립트와 일치해야 한다.
    """

    def __init__(self, field, values):
        self.field = field

        self.query = dict()
        self.query[_terms_set][field][_terms] = values

    def minimum_should_match_field(self, minimum_should_match_field):

        self.query[_terms_set][self.field][_minimum_should_match_field] = minimum_should_match_field    
        return self

    def build(self):
        return self.query