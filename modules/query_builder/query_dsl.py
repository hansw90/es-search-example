# ES 기본 쿼리들을 정리 한다.
# query DSL
# https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html 참고
# https://elasticsearch-dsl.readthedocs.io/en/latest/search_dsl.html 도 있지만, 내 입맛대로 만듬, 모든 파람을 가지고 있는건 아님
# valid check를 할만큼,, 여유는 없어서리,,,
import json

# leaf query

def _query():
    query = dict()
    query["query"] = dict()
    return query

def parse_json(query):
    return json.dump(query)

# match_all 생성.
def match_all(boost=None) :
    query = _query()
    query["match_all"] = dict()
    
    if boost != None:
        query["match_all"]["boost"] = boost
    return query

# match query 생성
# match short request
def match(field, search):
    query = _query()
    query["match"] = dict()
    query["match"][field] = search

    return search

# match query 생성.
def match(field, search, analyzer=None, boost=None, fuzziness=None, operator="OR", minimum_should_match=None):
    query = _query()
    
    query["match"] = dict()
    query["match"][field] = search

    if analyzer != None:
        query["match"]["analyzer"] = analyzer
    
    if boost != None:
        query["match"]["boost"] = boost

    if fuzziness != None:
        query["match"]["fuzziness"] = fuzziness

    if operator != None:
        query["match"]["operator"] = operator
    
    if minimum_should_match != None:
        query["match"]["minimum_should_match"]=minimum_should_match

    return query    

    

