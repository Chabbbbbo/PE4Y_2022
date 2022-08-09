'''
📌Q2. 어느날 여러분이 어떤 글을 읽고 있는데, 갑자기 특정 글자가 전체 글에서 몇개 들어있는지 궁금해졌습니다. 
그럼 한 번 파이썬 함수로 만들어 봅시다.

 - 글은 어떤 글이던 좋습니다. 인터넷에서 검색해서 복사 붙여넣기로 변수에 넣어 줍니다.

 - 변수에 담긴 글을 함수에 넣어주면 txt 파일로 저장도 함께 되도록 해줍니다.
'''


"""종목명	현재가	등락률	시가총액(억)	거래량 """

stock_top10 = '''삼성전자
005930
60,000
800800
-1.32%
3,581,870	15,732,380
LG에너지솔루션
373220
457,500
10,50010,500
+2.35%
1,070,550	583,882
SK하이닉스
000660
95,100
1,2001,200
-1.25%
692,330	3,024,190
삼성바이오로직스
207940
900,000
0
0.00%
640,566	36,195
LG화학
051910
671,000
19,00019,000
+2.91%
473,675	326,789
삼성전자우
005935
55,100
400400
-0.72%
453,411	737,066
NAVER
035420
265,500
7,0007,000
+2.71%
435,550	491,422
삼성SDI
006400
615,000
18,00018,000
+3.02%
422,902	314,942
현대차
005380
193,500
2,5002,500
-1.28%
413,448	930,935
카카오
035720
83,300
1,3001,300
+1.59%
370,642	1,501,390'''


def count_word(word):
    lines = stock_top10.split('\n')
    f = open("new_text.txt", 'w')
    for i in lines:
        f.write(i)

    plus = 0
    minus = 0
    plus_company = []
    minus_company = []

    for idx, line in enumerate(lines) :
        if '+' in line:
            plus += 1 
            plus_company.append(lines[idx-4])
        elif '-' in line:
            minus += 1
            minus_company.append(lines[idx-4])
    print(f'금일 코스피 10기업중 \n상승한 기업은 {plus}개, \n기업명 : {plus_company}')
    print(f'하락한 기업은 {minus}개, \n기업명 : {minus_company}')


count_word(stock_top10)
    
