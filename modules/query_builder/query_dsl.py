import sys, os
from telnetlib import COM_PORT_OPTION
sys.path.append(os.getcwd()+"/quries")

from term_level_query import TermQuery
from full_text_query import FullTextQuery
from geo_query import GeoQuery
from compound_query import CompoundQuery

class Query(TermQuery, FullTextQuery, GeoQuery, CompoundQuery):
    def hello():
        print()



if __name__ == "__main__":
    pass