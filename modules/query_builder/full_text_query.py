# ES 기본 쿼리들을 정리 한다.
# query DSL
# https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html 참고
# https://elasticsearch-dsl.readthedocs.io/en/latest/search_dsl.html 도 있지만, 내 입맛대로 만듬, 모든 파람을 가지고 있는건 아님
# valid check를 할만큼,, 여유는 없어서리,,,
import json

# leaf query

_query = 'query'

_term = 'term'

_match = 'match'
_match_phrase = 'match_phrase'
_match_phrase_prefix = 'match_phrase_prefix'
_match_boolean_prefix = 'match_boolean_prefix'
_multi_match = 'multi_match'


_analyzer = 'analyzer'
_fuzziness = 'fuzziness'
_operator = 'operator'
_minimum_should_match = 'minimum_should_match'
_max_expansions = 'max_expansions'
_slop = 'slop'
_zero_terms_query = 'zero_terms_query'
_value = 'value'
_prefix_length = 'prefix_length'
_fields = 'fields'
_type = 'type'
_zero_term_query = 'zero_term_query'
_cutoff_frequency = 'cutoff_frequency'
_rewrite = 'rewrite'

class FullTextQuery():

    query = dict()

    def __init__(self):
        self.query = dict()

    def parse_json(self, query):
        return json.dump(query)
    
    
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


    def multi_match(self, fields:list(), search, type=None, operator=None, zero_term_query=None, cutoff_frequency=None, boost=None, rewrite=None,
                                prefix_length=None, fuzziness=None, minimum_should_match=None, analyzer=None, max_expansions=None):
        """
        match 쿼리의 다중 필드 버전
        """

        self.query[_multi_match] = dict()

        self.query[_multi_match][_fields] = fields
        self.query[_multi_match][_query] = search

        # multi_match field type (best_fileds, most_fileds, cross_fileds, phrase, phrase_prefix, bool_prefix)
        if type != None:
            self.query[_multi_match][_type] = type

        if operator != None:
            self.query[_multi_match][_operator] = operator

        if zero_term_query != None:
            self.query[_multi_match][_zero_term_query] = zero_term_query

        if cutoff_frequency != None:
            self.query[_multi_match][_cutoff_frequency] = cutoff_frequency

        if boost != None:
            self.query[_multi_match][_boost] = boost

        if rewrite != None:
            self.query[_multi_match][_rewrite] = rewrite

        if prefix_length != None:
            self.query[_multi_match][_prefix_length] = prefix_length

        if fuzziness != None:
            self.query[_multi_match][_fuzziness] = fuzziness

        if minimum_should_match != None:
            self.query[_multi_match][_minimum_should_match] = minimum_should_match

        if analyzer != None:
            self.query[_multi_match][_analyzer] = analyzer

        if max_expansions != None:
            self.query[_multi_match][_max_expansions] = max_expansions

        return self.query

