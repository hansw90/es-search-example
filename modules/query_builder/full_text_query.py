# ES 기본 쿼리들을 정리 한다.
# query DSL
# https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html 참고
# https://elasticsearch-dsl.readthedocs.io/en/latest/search_dsl.html 도 있지만, 내 입맛대로 만듬, 모든 파람을 가지고 있는건 아님
# valid check를 할만큼,, 여유는 없어서리,,,
import json

# leaf query

_query = 'query'

_term = 'term'
_match_all = 'match_all'
_match = 'match'
_match_phrase = 'match_phrase'
_match_phrase_prefix = 'match_phrase_prefix'
_match_boolean_prefix = 'match_boolean_prefix'
_multi_match = 'multi_match'

_boost = 'boost'
_analyzer = 'analyzer'
_fuzziness = 'fuzziness'
_operator = 'operator'
_minimum_should_match = 'minimum_should_match'
_max_expansions = 'max_expansions'
_slop = 'slop'
_zero_terms_query = 'zero_terms_query'
_value = 'value'
_prefix_length = 'prefix_length'


class FullTextQuery():

    def __init__(self):
        self.query = dict()
        self.query[_query] = dict()

    def parse_json(self, query):
        return json.dump(query)

    # match_all 생성.
    def match_all(self, boost=None) :
        self.query[_match_all] = dict()
        
        if boost != None:
            self.query[_match_all][_boost] = boost
        return self.query


    def match(self, field, search, analyzer=None, boost=None, fuzziness=None, operator=None, minimum_should_match=None
                        , zero_terms_query=None, cutoff_frequency=None, rewrite=None, prefix_length=None, max_expansions=None):
        """
       전체 텍스트 쿼리를 수행하기 위한 기본 쿼리 (fuzzy 매치와 phrase, 근접 쿼리를 포함) 
       쉽게 말해 전체 텍스트에서 특정 부분이 포함되는지 여부를 확인하는데 
       fuzzy를 이용하여 유사도가 어느정도 되는 쿼리들도 조회 가능
        """

        self.query[_query][_match] = dict()
        self.query[_query][_match][field] = dict()
        self.query[_query][_match][field][_query] = search

        if analyzer != None:
            self.query[_query][_match][field][_analyzer] = analyzer
        
        if boost != None:
            self.query[_query][_match][field][_boost] = boost

        if fuzziness != None:
            self.query[_query][_match][field][_fuzziness] = fuzziness

        if operator != None:
            self.query[_query][_match][field][_operator] = operator
        
        if minimum_should_match != None:
            self.query[_query][_match][field][_minimum_should_match]=minimum_should_match

        return self.query    

    def match_phrase(self, field, search, analyzer=None, boost=None, max_expansions=None, slop=None, zero_terms_query=None):
        """
        입력을 analyze 한다. 그리고 다음의 조건을 충족하는 document를 반환한다.
        - 모든 term들이 field에 존재해야 한다. 
        - 모든 term들이 입력된 순서에 맞게 존재한다. 
        """
        self.query[_match_phrase] = dict()
        self.query[_match_phrase][field][_query] = search

        if analyzer != None:
            self.query[_match_phrase][field][_analyzer] = analyzer

        if boost != None:
            self.query[_match_phrase][field][_boost] = boost

        if max_expansions != None:
            self.query[_match_phrase][field][_max_expansions] = boost

        if slop != None:
            self.query[_match_phrase][field][_slop] = slop

        if zero_terms_query != None:
            self.query[_match_phrase][field][_zero_terms_query] = zero_terms_query

        return self.query


    def match_phrase_prefix(self, field, search, analyzer=None, boost=None, max_expansions=None, slop=None, zero_terms_query=None):
        """
        match phrase 와 비슷하지만 마지막 단어에 와일드 카드가 사용된다. (자동완성 기능에서 자주 사용)
        """
        self.query[_match_phrase_prefix] = dict()
        self.query[_match_phrase_prefix][field][_query] = search

        if analyzer != None:
            self.query[_match_phrase_prefix][field][_analyzer] = analyzer

        if boost != None:
            self.query[_match_phrase_prefix][field][_boost] = boost

        if max_expansions != None:
            self.query[_match_phrase_prefix][field][_max_expansions] = boost

        if slop != None:
            self.query[_match_phrase_prefix][field][_slop] = slop

        if zero_terms_query != None:
            self.query[_match_phrase_prefix][field][_zero_terms_query] = zero_terms_query

        return self.query
            
    
    def match_boolean_prefix(self, field, search, analyzer=None, minimum_should_match=None, operator=None, fuzziness=None, prefix_length=None, max_expansions=None):
        """
        match_boolean_prefix
        마지막 term을 제외한 모든 term은 term query에 사용된다. 마지막 term은 prefix query에 사용된다.
        match_boolean_prefix는 match_phrase_prefix와 상당히 유사하지만 match_phrase_prefix는 입력값을 phrase로 보고 쭉 이어진 하나의 검색을 하는 반면
        match_boolean_prefix는 term단위 검색으로 서로 떨어져있어도 되고, 순서가 바뀌어도 가능하다.
        """
        
        self.query[_match_boolean_prefix] = dict()
        self.query[_match_boolean_prefix][field][_query] = search

        if analyzer != None:
            self.query[_match_boolean_prefix][field][_analyzer] = analyzer

        if minimum_should_match != None:
            self.query[_match_boolean_prefix][field][_minimum_should_match] = minimum_should_match

        if operator != None:
            self.query[_match_boolean_prefix][field][_operator] = operator

        if fuzziness != None:
            self.query[_match_boolean_prefix][field][_fuzziness] = fuzziness

        if prefix_length != None:
            self.query[_match_boolean_prefix][field][_prefix_length] = prefix_length
        
        if max_expansions != None:
            self.query[_match_boolean_prefix][field][_max_expansions] = max_expansions

        return self.query


    def multi_match(self, fields:list(), search, operator=None, zero_term_query=None, cutoff_frequency=None, boost=None, rewrite=None,
                                prefix_length=None, fuzziness=None, minimum_should_match=None, analyzer=None, max_expansions=None):
        """
        match 쿼리의 다중 필드 버전
        """
        pass

    def common(self):
        """
        - Document에서 자주 사용되는 단어를 제외하고, 의미있는 단어만 검색하기 위해서 사용하는 쿼리
        - cutoff_frequency 옵션을 사용하여, 특정 빈도 보다 많은 단어를 제외하고 검색할 수 있다.
        """
        pass

    