import sys, os
print(os.getcwd())
sys.path.append(os.getcwd()+"/quries")
from quries.compound_query import BoolQuery
from quries.full_text_query import FullTextQuery
from quries.term_level_query import TermQuery

class Query(BoolQuery, FullTextQuery, TermQuery):
    def hello():
        print()


query = dict()
m = Query().match(field="test", search="hello word")

query["query"] = m
print(query)
m2 = Query().match(field="test", search="hello word")
q = BoolQuery().filter(queries=[m]).filter(queries=[m2]).build()
print(q)