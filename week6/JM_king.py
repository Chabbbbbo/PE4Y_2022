
"""
📌Q1. 역사 문제를 하나 내보겠습니다. 고려시대와 조선시대 왕 이름 중에서 고려에도 있고 조선에도 있는 이름은 몇개 일까요? 한 번에 딱 안 떠오른다면 왕 이름을 드릴테니 파이썬 함수로 만들어서 출력 해봅시다.

😲조건1 - 중복되는 왕 이름 출력
😲조건2 - 중복되는 왕 이름의 수 출력
# 왕이름
korea_king = "태조,혜종,정종,광종,경종,성종,목종,현종,덕종,정종,문종,순종,선종,헌종,숙종,예종,인종,의종,명종,신종,희종,강종,고종,원조,충렬왕,충선왕,충숙왕,충혜왕,충목왕,충정왕,공민왕,우왕,창왕,공양왕"
chosun_king = "태조,정종,태종,세종,문종,단종,세조,예종,성종,연산군,중종,인종,명종,선조,광해군,인조,효종,현종,숙종,경종,영조,정조,순조,헌종,철종,고종,순종"

✅출력 예시
king(korea_king, chosun_king)
조선과 고려에 모두 있는 왕 이름 : 태조
조선과 고려에 모두 있는 왕 이름 : 정종
조선과 고려에 모두 있는 왕 이름 : 경종
조선과 고려에 모두 있는 왕 이름 : 성종
조선과 고려에 모두 있는 왕 이름 : 현종
조선과 고려에 모두 있는 왕 이름 : 문종
조선과 고려에 모두 있는 왕 이름 : 순종
조선과 고려에 모두 있는 왕 이름 : 헌종
조선과 고려에 모두 있는 왕 이름 : 숙종
조선과 고려에 모두 있는 왕 이름 : 예종
조선과 고려에 모두 있는 왕 이름 : 인종
조선과 고려에 모두 있는 왕 이름 : 명종
조선과 고려에 모두 있는 왕 이름 : 고종
조선과 고려에 모두 있는 왕 이름은 총 13개 입니다
"""

korea_king = "태조,혜종,정종,광종,경종,성종,목종,현종,덕종,정종,문종,순종,선종,헌종,숙종,예종,인종,의종,명종,신종,희종,강종,고종,원조,충렬왕,충선왕,충숙왕,충혜왕,충목왕,충정왕,공민왕,우왕,창왕,공양왕"

chosun_king = "태조,정종,태종,세종,문종,단종,세조,예종,성종,연산군,중종,인종,명종,선조,광해군,인조,효종,현종,숙종,경종,영조,정조,순조,헌종,철종,고종,순종"


#딕셔너리 강의 실습에서 배웠던 알고리즘을 활용해봤습니다.

# 중복되는 왕 이름과 수를 출력하는 함수
def kingCount():
    totalCount = 0                                                                      # totalCount: 중복되는 왕 이름의 수
    kingDict = dict()                                                                   # kingDict: 고려와 조선 왕을 모두 가진 딕셔너리

    korea_king_list = korea_king.split(',')                                             # korea_king_list: 고려의 왕 리스트
    chosun_king_list = chosun_king.split(',')                                           # chosun_king_list: 조선의 왕 리스트
    kingList = korea_king_list + chosun_king_list                                       # kingList : 고려와 조선의 왕 리스트를 합한 리스트

    for val in kingList:                                                                # kingList의 길이만큼 반복
        kingDict[val] = kingDict.get(val, 0) + 1                                            # kingDict에 kingList의 값을 KEY에, 중복되는 숫자를 VALUE에 대입하는 알고리즘

    for key, value in kingDict.items():                                                 # kingDict.items()의 길이만큼 키,값을 반환하는 포문
        if int(value) > 1 :                                                                 # 조선과 고려의 중복되는 왕이 2명 이상일 때
            totalCount += 1                                                                     # totalCount + 1
            print(f'조선과 고려에 모두 있는 왕 이름 : {key}')                                     # 조선과 고려의 중복되는 왕 이름 출력

    print(f'조선과 고려에 모두 있는 왕 이름은 총 {totalCount}개 입니다')                    # totalCount 출력


# 실행코드
kingCount()

