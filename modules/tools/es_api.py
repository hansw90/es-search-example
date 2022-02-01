import json
from urllib import request
import requests

import modules.utils.es_utils as esutils

class ElasticApi(object):

    def __init__(self, es_model):
        self.http_method = "http://"
        print(es_model)
        self.url = es_model['url']
        self.security_token = es_model['security_token']
        self.default_headers = {'Content-Type': 'application/json; charset=utf-8'}
        self.es_url = self.http_method+self.security_token+self.url

        self.doc = "/_doc"
        self.search= "/_search"
        self.update = "/update"
        self.delete = "/delete"
        self.delete_by_query = "/delete_by_query"
        self._analyze = "_analyze"
        self.cat ="/_cat"
    
    
    def get_docs_by_id(self, index, id, body):
        """
        doc_id를  통하여 docs를 가지고 온다.
        """
        es_url =  f"{self.es_url}{index}{self.doc}/{id}"
        es_result = requests.get(url=es_url, headers=self.default_headers)
        return es_result
    
    def search_docs(self, index, query):
        """
        query를 통해 docs 를 검색한다.
        """
        es_url = f"{self.es_url}{index}{self.search}"
        es_result = requests.post(es_url, headers=self.default_headers, data=json.dumps(query, ensure_ascii=False).encode('utf-8'))
        return es_result

    def insert_docs(self, index, body):
        """
        docs를 추가한다.
        """
        es_url = f"{self.es_url}{index}{self.doc}"
        es_result = requests.post(
                            es_url
                            , headers=self.default_headers
                            , data=json.dumps(body, ensure_ascii=False)
                            , default=esutils.defaultconverter).encode('utf-8')
        return es_result

    def insert_bulk(self, index, body):
        """
        bulk insert를 실시한다.
        """


    def update_docs(self, index, id, body):
        """
        docs를 업데이트 한다.
        """
        data = esutils.del_none(body)
        data = json.dumps(data, ensure_ascii=True).encode('utf-8')
        es_url = f"{self.es_url}{index}{self.update}/{id}"
        es_result = requests.post(
                    url=es_url
                    , headers=self.default_headers
                    , data=data
                    )
        return es_result

    def delete_docs(self, index, id):
        """
        docs를 제거한다.
        """
        es_url = f"{self.es_url}{index}{self.doc}/{id}"
        es_result = requests.delete(
            url = es_url,
            headers=self.default_headers
        )
        return es_result
        

    def delete_query(self, index, query):
        """
        query를 통해 docs들을 제거한다.
        """
        es_url = f"{self.es_url}{index}{self.delete_by_query}"
        es_result = requests.post(
                    url=es_url
                    , headers=self.default_headers
                    , data=query
                    )
        return es_result

    def analyze(self, query):
        """
        query를 분석한다.
        """
        es_url = f"{self.es_url}{self._analyze}"
        es_result = requests.get(
            url = es_url
            , headers=self.default_headers
            , data=query
        )
        
        return es_result


    def get_health(self):
        """
        Elastic health checking
        """
        es_url = f"{self.es_url}{self.cat}/health?v"
        es_result = requests.get(
            url = es_url
            , headers=self.default_headers
        )

        return es_result

    def get_node(self):
        """
        Elastic health checking
        """
        es_url = f"{self.es_url}{self.cat}/node?v"
        es_result = requests.get(
            url = es_url
            , headers=self.default_headers
        )

        return es_result


# 주소 검색 예제 프로젝트
if __name__ == 'main':
    print("hello address")