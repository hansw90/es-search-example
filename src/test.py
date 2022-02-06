import sys, os

sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+"/src")
sys.path.append(os.getcwd()+"/modules/tools")
sys.path.append(os.getcwd()+"/modules/data")

import requests
from modules.tools import es_api
from data import jibun_seoul, road_seoul
from itertools import chain
from collections import defaultdict

class Tester(object):

    def __init__(self):
        self.talk_no = 1
        pass
    
    def read_file(self, name):
        f = open(f"{name}", "r")
        while True:
            line = f.readline()
            if not line : break
            
            self.read_line(line)

    def read_line(self, line):
        if line.startswith("#"):
            print(f"{self.talk_no} 번째 대화 주소 키워드")
            self.talk_no += 1
            return
        
        if line.startswith("//"):
            return
        
        print(line)

if __name__ == "__main__":

    es_model = dict()
    es_model['url'] = "localhost:9200"
    es_model['security_token'] = ""
    
    api = es_api.ElasticApi(es_model)
    es_health = api.get_health()
    

    # test = Tester()
    # file_name = "test.csv"
    # file_path = os.path.join(os.getcwd()+"/src", file_name)
    # test.read_file(file_path)

    seoul_jibuns = jibun_seoul.get_all_jibun(path="./data/")
    seoul_roads = road_seoul.get_all_road(path="./data/")
    
    seoul_addresses = defaultdict(list)
    for k, v in chain(seoul_jibuns.items(), seoul_roads.items()):
        seoul_addresses[k].append(v)

    print(seoul_addresses['청운동'])
    
    print(seoul_addresses['창경궁로'])