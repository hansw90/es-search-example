_term = 'term'
_terms = 'terms'
_terms_set = 'terms_set'
_range = 'range'
_exist = 'exist'
_prefix = 'prefix'
_wildcard = 'wildcard'
_fuzzy = 'fuzzy'

_field = 'field'
_value = 'value'
_boost = 'boost'
_case_insensitive = 'case_insensitive'
_minimum_should_match_field = 'minimum_should_match_field'
_gte = 'gte'
_gt = 'gt'
_lte = 'lte'
_lt = 'llt'
_timezone = 'timezone'
_format = 'format'
_rewrite = 'rewrite'
_fuzziness = 'fuzziness'
_prefixlength = 'prefix_length'
_transpositions = 'transpositions'
_max_expansions = 'max_expansions'

class Fuzzy(object):
    """
    입력한 term과 비슷한 문자를 찾을때 사용하는 쿼리 레벤스테인 거리 알고리즘을 사용하며, 설정한 거리에 따라서 어느정도 유사도에 값을 찾을지 정할수 있다.
    한글 초성 중성 종성 단위의 거리는 따로 처리가 필요함
    """

    def __init__(self, field, value):
        self.field = field

        self.query = dict()
        self.query[_fuzzy] = dict()
        self.query[_fuzzy][self.field] = dict()
        self.query[_fuzzy][self.field][_value] = value
    
    # 허용 최대 거리 0,1,2
    # default AUTO 는 용어의 길이에 따라 편집거리를 생성 
    def fuzziness(self, value):
        self.query[_fuzzy][self.field][_fuzziness] = value
        return self

    # 확장할때 변경되지 않을 채로 남아 있는 시작 문자수
    def prefix_length(self, value):
        self.query[_fuzzy][self.field][_prefixlength] = value
        return self
    
    # 근접한 두 문자의 순서가 변경되는지에 대한 여부 표현
    def transpositions(self, value):
        self.query[_fuzzy][self.field][_transpositions] = value
        return self

    def max_expansions(self, value):
        self.query[_fuzzy][self.field][_max_expansions] = value
        return self

    def build(self):
        return self.query