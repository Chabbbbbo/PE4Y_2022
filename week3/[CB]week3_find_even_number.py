'''
📌Q3. 2개의 숫자를 입력하여 그 사이에 짝수만 출력하는 함수를 만들어 봅시다. 
그리고 중앙값도 함께 출력 해봅시다.
(단, 중앙값이 짝수가 아닐 경우에는 중앙값은 출력을 하지 않고, 짝수인 수만 출력한다)

- 중앙값: 정중앙에 있는 값

- 출력 예시 

첫 번째 수 입력 : 1
두 번째 수 입력 : 11
2 짝수
4 짝수
6 짝수
6 중앙값
8 짝수
10 짝수
'''

def find_even_number(n, m):
    if (n > m):
        temp = m
        m = n
        n = temp

    num_list = []
    for i in range(n,m+1):
        num_list.append(i)
    
    middle_num = int(len(num_list) /2)
    idx = 0
    for num in num_list:
        if ((idx == middle_num) and (num_list[middle_num] % 2 ==0)):
            print(num, '중앙값')
        elif (num % 2 == 0):
            print(num, '짝수')
        idx += 1

print('두 숫자 사이에 짝수 값만 찾아주는 마법의 컴퓨터!')
try:
    n = int(input('첫번째 수를 입력해주세요 : '))
    m = int(input('두번째 수를 입력해주세요 : '))
    find_even_number(n,m)
except:
    print('를 입력해주세요!')
