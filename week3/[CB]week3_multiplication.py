'''
📌Q1. 숫자를 입력 받고 그 숫자의 구구단을 출력하는 함수를 만들어 봅시다. 
다만 아래의 조건을 만족해 주세요.
 - 조건 1: 홀 수 번째만 출력하기
 - 조건 2: 값이 50이하인 것만 출력하기
'''

def multiplication(number):
    print(f'====={number}단=====')
    for i in range(50):
        odd_num = 2*i + 1
        mul_num = number * odd_num
        if (mul_num <= 50):
            print(f'{number} X {odd_num} = {mul_num}')
        else:
            print('50이 넘어 종료합니다.')
            break

try:
    number = int(input('몇 단을 계산할까요?'))
    if (number > 0): 
        multiplication(number)
    else:
        print('계산을 위해 양수를 입력해주세요.')
except:
    print('숫자로 입력해주세요!')





    