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
    
    