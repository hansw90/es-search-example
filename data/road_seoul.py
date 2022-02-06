road = dict()


def get_all_road(path, name='road_seoul', file_type='txt'):
    roads = read_write_file(path, name, file_type)
    return roads

def read_write_file(path, name, file_type):
    f = open(f'{path}{name}.{file_type}', 'r')
    # w = open(f'{path}{name}_dump.json', 'a', encoding='UTF8')
    # line_no = 0
    while True:
        line = f.readline()
        if not line : break
        # if line_no == 0:
        #     line_no += 1
        #     continue
        pase_line_to_dict(line)
        # w.write(json)
        # w.write("\n")
    return road

def pase_line_to_dict(line):
    infos = line.split('|')
    road_name = infos[1]

    if road_name not in road:
        road[road_name] = {'code': [], 'juso': []}
        road[road_name]['code'].append(infos[0])
        road[road_name]['juso'].append(infos[4]+" "+infos[6]+" "+infos[8])
    else:
        road[road_name]['code'].append(infos[0])
        road[road_name]['juso'].append(infos[4]+" "+infos[6]+" "+infos[8])
    
    

if __name__ == "__main__":
    """
    resource 도로명 주소를 파싱한다.
    도로명은 법정동과 1:n 인점을 알아두자. 이게 주소 찾는데 중요한 정보
    법종동 행정동간의 1:n도 ㅠㅠㅠ
    """
    file_path = ''
    file_name = 'road_seoul'
    file_type = 'txt'
    read_write_file(file_path, file_name, file_type)