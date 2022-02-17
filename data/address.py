sido_list = dict()
sigun_list = dict()
gu_list = dict()
dong_list = dict()


def load_all_address():
    import sys, os
    file_path = os.path.dirname(os.path.abspath(__file__))
    file_name = '법정동코드 전체자료'
    file_type = 'txt'
    read_file(file_path, file_name, file_type)

    address = dict()
    address['sido'] = sido_list
    address['sigun'] = sigun_list
    address['gu'] = gu_list
    address['dong'] = dong_list
    return address

def read_file(path, name, file_type):
    f = open(f'{path}/{name}.{file_type}', 'r')
    # w = open(f'{path}{name}_dump.json', 'a', encoding='UTF8')
    line_no = 0
    while True:
        line = f.readline()
        if not line : break
        # line_no += 1
        # if line_no == 100:
        #     break
        pase_line_to_dict(line)
    return

#서울특별시 종로구 창신3동
def pase_line_to_dict(line):
    address = line.split('\t')
    if (address[0][-8:] == '00000000'):
        # sido
        sido_list[address[1]] = dict()
        sido_list[address[1]]['code'] = address[0][:2]
        sido_list[address[1]]['status'] = address[2]
        # print(sido_list[address[1]])

    if (address[0][-8:] != '00000000' and address[0][-6:] == '000000'):
        # sigun
        # print(f"{address[0]} = {address[1]}")
        if address[1][-1] == '구':
            sigun = address[1].split(' ')
            sigun_name = sigun[0]
            gu_name = sigun[1]
            add_sigun(address, sigun_name)
            add_gu(address, sigun_name, sigun_name, gu_name)
            
        else:
            sigun = address[1].split(' ')

            sigun_name = sigun[0] if len(sigun) == 1 else sigun[1]
            add_sigun(address, sigun_name)
    
    if (address[0][-8:] != '00000000' and address[0][-5:] != '00000' and address[0][-2:] == '00'):
        gu = address[1].split(' ')
        
        if len(gu) > 3:
            add_gu(address, sido=gu[0], sigun=gu[1], gu=gu[2])
            add_dong(address, sido=gu[0], sigun=gu[1], gu=gu[2], dong=gu[3])
            
        if len(gu) == 3:
            add_dong(address, sido=gu[0], sigun=gu[1], gu=None, dong=gu[2])
        
        if len(gu) <= 2:
            add_dong(address, sido=gu[0], sigun=gu[0], gu=None, dong=gu[1])
        
        # print(address[1])
    return

def add_sigun(address, sigun):
    if sigun not in sigun_list:
        sigun_list[sigun] = dict()
        sigun_list[sigun]['code'] = address[0]
        sigun_list[sigun]['address'] = address[1]
        sigun_list[sigun]['status'] = address[2]

def add_gu(address, sido, sigun, gu):
    if gu not in gu_list :
        gu_list[gu] = list()
    gu_info = dict()
    gu_info['code'] = address[0]
    gu_info['address'] = address[1]
    gu_info['sido'] = sido
    gu_info['sigun'] = sigun
    gu_info['status'] = address[2]
    gu_list[gu].append(gu_info)

def add_dong(address, sido, sigun, gu, dong):
    if dong not in dong_list:
        dong_list[dong] = list()
    dong_info = dict()
    dong_info['code'] = address[0]
    dong_info['address'] = address[1]
    dong_info['sido'] = sido
    dong_info['sigun'] = sigun
    dong_info['gu'] = gu


if __name__ == "__main__":
    """
    전국 법정동을 추출하여 알맞게 변형한다.
    """
    # import sys, os
    # file_path = os.path.dirname(os.path.abspath(__file__))
    # file_name = '법정동코드 전체자료'
    # file_type = 'txt'
    # read_file(file_path, file_name, file_type)
    
    load_all_address()
    print(dong_list["서교동"])