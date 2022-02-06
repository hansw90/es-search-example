jibun = dict()

def get_all_jibun(path, name='jibun_seoul', file_typ='txt'):
    jibuns = read_write_file(path, name, file_typ)
    return jibuns

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
    return jibun

def pase_line_to_dict(line):
    infos = line.split('|')
    jibun_name = infos[5]

    if jibun_name not in jibun:
        jibun[jibun_name] = {'code': [], 'juso': []}
        jibun[jibun_name]['code'].append(infos[2])
        jibun[jibun_name]['juso'].append(infos[3]+" "+infos[4]+" "+infos[5])
    else:
        return
    

if __name__ == "__main__":
    """
    법정동을 뽑아 낸다.
    그외에도 이 파일은 db에서 그대로 쓰임
    """
    file_path = ''
    file_name = 'jibun_seoul'
    file_type = 'txt'
    read_write_file(file_path, file_name, file_type)