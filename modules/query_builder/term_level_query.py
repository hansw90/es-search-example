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

class TermQuery(object):

    def __init__(self):
        self.query = dict()
    

    def term(self, field, value, boost=None, case_insensitive=None):
        """
        term query
        검색하고자 하는 필드에 정확한 텀을 포함하고 있는지 확인하는 쿼리
        """
        self.query[_term][field][_value] = value

        if boost != None:
            self.query[_term][_boost] = boost
        
        # (Optional, Boolean(false)) ASCII 대소문자를 구분하지 않고 인덱스 필드 값을 찾는다. 
        if case_insensitive != None: 
            self.query[_term][_case_insensitive] = case_insensitive

        return self.query


    def terms(self, field, values:list(), boost=None):
        """
        검색하고자 하는 필드에 정확한 텀들을 포함하고 있는지 확인하는 쿼리
        """
        self.query[_terms][field] = values

        if boost != None:
            self.query[_terms][field][_boost] = boost

        return self.query

    def terms_set(self, field, values, minimum_should_match_field=None):
        """
        지정된 용어중 하나 이상과 일치하는 문서를 찾는다. 지정된 최소값과 일치해야 하는 용어의 수는 필드 또는 스크립트와 일치해야 한다.
        """
        self.query[_terms_set][field][_terms] = values
        
        if minimum_should_match_field != None:
            self.query[_terms_set][field][_minimum_should_match_field] = minimum_should_match_field

        return self.query


    def range(self, field, gte=None, gt=None, lte=None, lt=None, time_zone=None, format=None):
        """
        검색 하고자 하는 필드에서 입력한 범위에 포험되는 날짜나, 숫자, 문자열등을 검색할 때 사용
        """

        # greater than or equal to 이상
        if gte != None:
            self.query[_range][field][_gte] = gte
        
        # greater than 초과 큼
        if gt != None:
            self.query[_range][field][_gt] = gt

        # less than or equal to
        if lte != None:
            self.query[_range][field][_lte] = lte

        # less than
        if lt != None:
            self.query[_range][field][_lt] = lt
        
        # ex "+01:00"
        if time_zone != None:
            self.query[_range][field][_timezone] = time_zone
        
        # ex "dd/MM/yyyy||yyyy" || 로 구분.
        if format != None:
            self.query[_range][field][_format] = time_zone
                
        return self.query

    def exist(self, field):
        """
        검색하고자 하는 필드에 값이 있는지 여부 확인
        """
        self.query[_exist][_field] = field

        return self.query



    def prefix(self, field, value):
        """
        검색하고자 하는 필드에서 입력한 값으로 시작하는 문장이 있는지 검색할 때 사용
        """
        self.query[_prefix][field] = value

        return self.query



    def wildcard(self, field, value, boost=None, rewrite=None):
        """
        와일드 카드 *,? 를 사용하여 검색하는 방법, 전체를 다 뒤져서 찾아야 하기 때문에 성능에 좋지 못하다.
        ex) hel* or hel?o
        """
        self.query[_wildcard][field][_value] = value
        
        if boost != None:
            self.query[_wildcard][field][_boost] = boost

        # rewrite param
        # https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-multi-term-rewrite.html
        if rewrite != None:
            self.query[_wildcard][field][_rewrite] = rewrite
            
        return self.query

    def fuzzy(self, field, value, boost=None, fuzziness=None, prefix_length=None, transpositions=None, max_expansions=None):
        """
        입력한 term과 비슷한 문자를 찾을때 사용하는 쿼리 레벤스테인 거리 알고리즘을 사용하며, 설정한 거리에 따라서 어느정도 유사도에 값을 찾을지 정할수 있다.
        한글 초성 중성 종성 단위의 거리는 따로 처리가 필요함
        """
        self.query[_fuzzy][field][_value] = value

        # 허용 최대 거리 0,1,2
        # default AUTO 는 용어의 길이에 따라 편집거리를 생성 
        if fuzziness != None:
            self.query[_fuzzy][field][_fuzziness] = fuzziness

        # 확장할때 변경되지 않을 채로 남아 있는 시작 문자수
        if prefix_length != None:
            self.query[_fuzzy][field][_prefixlength] = prefix_length

        # 근접한 두 문자의 순서가 변경되는지에 대한 여부 표현
        if transpositions != None:
            self.query[_fuzzy][field][_transpositions] = transpositions

        if max_expansions != None:
            self.query[_fuzzy][field][_max_expansions] = max_expansions

        return self.query
