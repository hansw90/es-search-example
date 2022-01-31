class AddressSearch(object):
    """
    주소 검색 관련 모델
    """

    def __init__(self):
        pass

    def load_dong_and_road(self):
        """
        도로명/법정동/행정동 명을 맵에 저장한다.
        """
    
    def find_dong_and_road_by_name(self, name) :
        """
        도로명/법정동/행정동 맵정보에서 네임을 통해 값을 가져온다.
        """

    def find_dong_and_road(self, address):
        """
        주소 정보를 통해 도로명/법정동/행정동 명을 가져온다.
        """

    def parse_dong_to_road(self, dong):
        """
        법정동 주소를 도로명으로 파싱한다.
        """
    
    def parse_road_to_dong(self, road):
        """
        도로명 주소를 법정동 주소로 파싱한다.
        """

    def get_pnu_no(self, dong):
        """
        법정동 주소를 통해 pnu 코드를 얻는다.
        """

    def split_keywords(self, keywords):
        """
        키워드를 분리한다.
        """
        keyword_list = keywords.split("\t")

