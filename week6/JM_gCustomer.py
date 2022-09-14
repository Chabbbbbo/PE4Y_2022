"""
📌Q4. 여러분은 어떤 상품을 판매하고 있습니다. 매월 상품을 많이 구매해준 VIP회원에게 할인 쿠폰을 제공해주려고 합니다. 아래와 같은 회원 정보가 있을 때 회원 정보를 출력하고 할인 쿠폰을 받을 회원이 누구인지 출력하는 함수를 만들어 주세요.

😲조건1 - 8회 이상 구매한 회원이 VIP대상
😲조건2 - 전화번호가 없으면 쿠폰을 받을 수 없음
😲조건3 - 전화번호가 없으면 000-0000-0000으로 출력할 것

# 6명의 회원이고 "아이디,나이,전화번호,성별,지역,구매횟수" 순서로 입력되어 있음
info = "abc,21세,010-1234-5678,남자,서울,5,cdb,25세,x,남자,서울,4,bbc,30세,010-2222-3333,여자,서울,3,ccb,29세,x,여자,경기,9,dab,26세,x,남자,인천,8,aab,23세,010-3333-1111,여자,경기,10"
✅출력 예시
good_customer(info)
{'아이디': ['abc', 'cdb', 'bbc', 'ccb', 'dab', 'aab'], '나이': ['21세', '25세', '30세', '29세', '26세', '23세'], '전화번호': ['010-1234-5678', '000-0000-0000', '010-2222-3333', '000-0000-0000', '000-0000-0000', '010-3333-1111'], '성별': ['남자', '남자', '여자', '여자', '남자', '여자'], '지역': ['서울', '서울', '서울', '경기', '인천', '경기'], '구매횟수': [5, 4, 3, 9, 8, 10]}
할인 쿠폰을 받을 회원정보 아이디:aab, 나이:23세, 전화번호:010-3333-1111, 성별:여자, 지역:경기, 구매횟수: 10
"""

import re
from collections import defaultdict

# 딕셔너리를 다루는 작업은 재밌지만 인덱스가 없어 리스트를 활용, 접근하기가 까다롭네요..!
# 정규표현식을 활용해서 010-xxxx-xxxx 형식을 확인했습니다.
# 딕셔너리 값에 리스트를 넣기 위해 검색하다 defaultdict 함수를 알게되었습니다.

#분류 기준 리스트
subject_list = ['아이디', '나이', '전화번호', '성별', '지역', '구매횟수']
# 정보 스트링
info = "abc,21세,010-1234-5678,남자,서울,5,cdb,25세,x,남자,서울,4,bbc,30세,010-2222-3333,여자,서울,3,ccb,29세,x,여자,경기,9,dab,26세,x,남자,인천,8,aab,23세,010-3333-1111,여자,경기,10"

# 스트링에서 정보를 딕셔너리로 바꿔주는 함수
def good_customer(info):                                                                                    
    info_list = info.split(',')                                                                             # info_list : info를 ','로 나눈 리스트
    resultDict = defaultdict(list)                                                                          # resultDict: 키 - subject_list / 값 - 정보리스트. 값으로 리스트 형식을 갖도록 설정
    vipIndex_list = list()                                                                                  # vipIndex_list: 우수고객의 인덱스를 갖고있는 리스트 (resultDict의 값, 정보리스트의 인덱스)

    for idx, val in enumerate(info_list):                                                                   # info_list리스트의 길이만큼 반복문을 돌려 분류별로 고객 정보 리스트 정리
        criteria = idx%6                                                                                        # criteria: 인덱스/6 의 나머지의 값으로 분류 기준 인덱스 저장
        subject = subject_list[criteria]                                                                        # subject: 분류 기준 인덱스를 통해 현재 분류값을 subject_list에서 가져옴
        resultDict[subject].append(val)                                                                         # subject를 키값으로 갖는 resultDict의 값(리스트)에 해당 분류에 속하는 정보를 append

        if subject == '구매횟수' and int(val) > 7:                                                                  # subject가 구매횟수일 때, 해당 값이 8 이상인 경우
            vipIndex_list.append(list(resultDict[subject]).index(val))                                                  # vipIndex_list에 해당 값을 가진 인덱스를 저장. resultDict의 값 리스트의 인덱스.


    for value in vipIndex_list:                                                                             # vipIndex_list 길이만큼 만큼 반복문을 돌려 해당 고객의 정보를 출력
        phoneList = resultDict.get('전화번호')                                                                  # phoneList: resultDict에서 키가 '전화번호'인 값 리스트
        if re.match('^010\-\d{4}\-\d{4}', phoneList[value]):                                                   # '전화번호'인 값 리스트에서 vip고객에 해당하는 인덱스의 정보가 올바른 형식인지 확인
            print('---------- 할인 쿠폰을 받을 회원정보 ----------')                                             # vip에 해당하는 고객, 전화번호 형식이 올바른 고객임이 확인된 후 문구 출력
            for k, v in resultDict.items():                                                                         # resultDict의 값을 반복하여 특정 고객의 정보 출력
                customer = ""
                customer = customer + (k+': '+v[value])                                                                 # customer: customer + '분류(키): 리스트[특정인덱스]'
                print(customer)


#실행함수
good_customer(info)
            



