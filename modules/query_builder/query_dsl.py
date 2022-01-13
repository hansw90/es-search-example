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

def query_init():
    query = dict()
    query[_query] = dict()
    return query

def parse_json(query):
    return json.dump(query)


# term
# 하나의 term을 찾는다, 이 term 은 analyzer 되지 않는다. 따라서 대소문자, 복수형등 다 구분된다. 
def term(field, search, boost=None):
    query = query_init()
    query[_term][field][_value] = search

    if boost != None:
        query[_term][_boost] = boost
    
    return query

# match_all 생성.
def match_all(boost=None) :
    query = query_init()
    query[_match_all] = dict()
    
    if boost != None:
        query[_match_all][_boost] = boost
    return query

# match query 생성
# match short request
def match(field, search):
    query = query_init()
    query[_match] = dict()
    query[_match][field] = search

    return search

# match query 생성.
# 가장 기본적인 search로 text, number, date, boolean을 사용할 수 있다. text를 검색전 analyzer한다.
# fuzzy matching 을 지원한다. (이게 한글에 초성 중성 종성에는 완벽하지는 않음)
def match(field, search, analyzer=None, boost=None, fuzziness=None, operator=None, minimum_should_match=None):
    query = query_init()
    
    query[_match] = dict()
    query[_match][field][_query] = search

    if analyzer != None:
        query[_match][field][_analyzer] = analyzer
    
    if boost != None:
        query[_match][field][_boost] = boost

    if fuzziness != None:
        query[_match][field][_fuzziness] = fuzziness

    if operator != None:
        query[_match][field][_operator] = operator
    
    if minimum_should_match != None:
        query[_match][field][_minimum_should_match]=minimum_should_match

    return query    


# match_phrase simple query
def match_phrase(field, search):
    query = query_init()
    query[_match_phrase] = dict()
    query[_match_phrase][field] = search

    return query

# match_phrase query
# 입력을 analyze 한다. 그리고 다음의 조건을 충족하는 document를 반환한다.
# 모든 term들이 field에 존재해야 한다. 
# 모든 term들이 입력된 순서에 맞게 존재한다.
def match_phrase(field, search, analyzer=None, boost=None, max_expansions=None, slop=None, zero_terms_query=None):
    query = query_init()
    query[_match_phrase] = dict()
    query[_match_phrase][field][_query] = search

    if analyzer != None:
        query[_match_phrase][field][_analyzer] = analyzer

    if boost != None:
        query[_match_phrase][field][_boost] = boost

    if max_expansions != None:
        query[_match_phrase][field][_max_expansions] = boost

    if slop != None:
        query[_match_phrase][field][_slop] = slop

    if zero_terms_query != None:
        query[_match_phrase][field][_zero_terms_query] = zero_terms_query

    return query

# match_phrase_prefix
def match_phrase_prefix(field, search):
    query = query_init()
    query[_match_phrase_prefix] = dict()
    query[_match_phrase_prefix][field] = search

    return query

# 입력값을 하나의 뭉텅이로 검색한다.
def match_phrase_prefix(field, search, analyzer=None, boost=None, max_expansions=None, slop=None, zero_terms_query=None):
    query = query_init()
    query[_match_phrase_prefix] = dict()
    query[_match_phrase_prefix][field][_query] = search

    if analyzer != None:
        query[_match_phrase_prefix][field][_analyzer] = analyzer

    if boost != None:
        query[_match_phrase_prefix][field][_boost] = boost

    if max_expansions != None:
        query[_match_phrase_prefix][field][_max_expansions] = boost

    if slop != None:
        query[_match_phrase_prefix][field][_slop] = slop

    if zero_terms_query != None:
        query[_match_phrase_prefix][field][_zero_terms_query] = zero_terms_query

    return query
        
# match_boolean_prefix
# 마지막 term을 제외한 모든 term은 term query에 사용된다. 마지막 term은 prefix query에 사용된다.
# match_boolean_prefix는 match_phrase_prefix와 상당히 유사하지만 match_phrase_prefix는 입력값을 phrase로 보고 쭉 이어진 하나의 검색을 하는 반면
# match_boolean_prefix는 term단위 검색으로 서로 떨어져있어도 되고, 순서가 바뀌어도 가능하다.
def match_boolean_prefix(field, search, analyzer=None, minimum_should_match=None, operator=None, fuzziness=None, prefix_length=None, max_expansions=None):
    query = query_init()
    query[_match_boolean_prefix] = dict()
    query[_match_boolean_prefix][field][_query] = search

    if analyzer != None:
        query[_match_boolean_prefix][field][_analyzer] = analyzer

    if minimum_should_match != None:
        query[_match_boolean_prefix][field][_minimum_should_match] = minimum_should_match

    if operator != None:
        query[_match_boolean_prefix][field][_operator] = operator

    if fuzziness != None:
        query[_match_boolean_prefix][field][_fuzziness] = fuzziness

    if prefix_length != None:
        query[_match_boolean_prefix][field][_prefix_length] = prefix_length
    
    if max_expansions != None:
        query[_match_boolean_prefix][field][_max_expansions] = max_expansions

    return query

