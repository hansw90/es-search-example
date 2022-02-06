import json

address = {
    'id': str(),
    'name': str(),
    'branch': str(),
    'sido_code': str(),
    'sido_name': str(),
    'sigungu_code': str(),
    'sigungu_name': str(),
    'admin_address_code': str(),
    'admin_address_name': str(),
    'law_address_code': str(),
    'law_address_name': str(),
    'jibun_code': str(),
    'deji_code': str(),
    'jibun_main_bunji': str(),
    'jibun_sub_bunji': str(),
    'jibun_address': str(),
    'road_code': str(),
    'road_name': str(),
    'road_main_bunji': str(),
    'road_sub_bunji': str(),
    'build_name': str(),
    'road_address': str(),
    'location': {
        'long': None,
        'lat': None,
    },
    'store': {
        'store_main_code': str(),
        'store_main_name': str(),
        'store_middle_code': str(),
        'store_middle_name': str(),
        'store_sub_code': str(),
        'store_sub_name': str()
    }
}

def read_write_file(path, name, file_type):
    f = open(f'{path}{name}{file_type}', 'r', encoding='UTF8')
    w = open(f'{path}{name}_dump.json', 'a', encoding='UTF8')
    line_no = 0
    while True:
        line = f.readline()
        if not line : break
        if line_no == 0:
            line_no += 1
            continue
        json = pase_line_to_json(line)
        w.write(json)
        w.write("\n")

def pase_line_to_json(line):
    line = line.replace('"', '')
    cols = line.split(',')

    address['id'] = cols[0]
    address['name'] = cols[1]
    address['branch'] = cols[2]
    address['sido_code'] = cols[11]
    address['sido_name'] = cols[12]
    address['sigungu_code'] = cols[13]
    address['sigungu_name'] = cols[14]
    address['admin_address_code'] = cols[15]
    address['admin_address_name'] = cols[16]
    address['law_address_code'] = cols[17]
    address['law_address_name'] = cols[18]
    address['jibun_code'] = cols[19]
    address['deji_code'] = cols[20]
    address['jibun_main_bunji'] = cols[22]
    address['jibun_sub_bunji'] = cols[23]
    address['jibun_address'] = cols[24]
    address['road_code'] = cols[25]
    address['road_name'] = cols[26]
    address['road_main_bunji'] = cols[27]
    address['road_sub_bunji'] = cols[28]
    address['build_name'] = cols[30]
    address['road_address'] = cols[31]
    address['location']['long'] = cols[37]
    address['location']['lat'] = cols[38]
    address['store']['store_main_code'] = cols[3]
    address['store']['store_main_name'] = cols[4]
    address['store']['store_middle_code'] = cols[5]
    address['store']['store_middle_name'] = cols[6]
    address['store']['store_sub_code'] = cols[7]
    address['store']['store_sub_name'] = cols[8]

    json_val = json.dumps(address, ensure_ascii=False)
    return json_val


if __name__ == "__main__":
    """
    es_dump용 파일 만들기
    이건 테스트 목적이므로 데이터를 10만개로 줄였음
    너무 줄이면 의미가 없으므로.
    """
    file_path = ''
    file_name = 'store_seoul'
    file_type = '.csv'
    read_write_file(file_path, file_name, file_type)

