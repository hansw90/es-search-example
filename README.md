# 주소 검색 엔진을 만들어 본다.
 
ES Builder는 7.16 에 맞추어 동작, 7.17, 8+ 에서는 쿼리가 정상적으로 동작 안할수 있음

## 주소 검색엔진

- 데이터
- [주소DB](https://www.juso.go.kr/addrlink/addressBuildDevNew.do?menu=match)  
- [소상공인시장진흥공단_상가(상권)정보](https://www.data.go.kr/data/15083033/fileData.do)
- [행정표준코드 관리시스템](https://www.code.go.kr/stdcode/regCodeL.do)

- TEST 데이터 : 이곳에선 ner 은 들어가지 않기 때문에, 각 대화당 나오는 주소 키워드만 직접 넣어 최종 주소를 찾도록 한다.
- ES analyzer는 기본 nori analyzer 를 사용한다.
- ES 의 오타보정, 자동완성등의 plugin 제작 방법은 블로그에서 다룬다.
- Query builder 작성 
    - TODO: 각 query Class로 변경해서 빌더 패턴사용하기
    - 빌더 패턴으로 하고, 필수값은 생성자 입력 받기

- 검색엔진은 플러그인 방식으로, 최대한 사용하기 편하게 만든다.

- 지식그래프는 neo4j 또는 redis graph 일단 자료가 neo4j 가 많기 때문에 이걸로 갈 예정

