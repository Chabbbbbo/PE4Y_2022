'''
📌Q1. 우리는 큰 수를 나타낼 때 3자리마다 , 를 찍어서 구분해 줍니다. 
파이썬에서는 아래와 같이 쉽게 나타낼 수 있습니다.

# f"{숫자:,}"
print(f"{1000:,}")

하지만 이번 미션에서는 숫자를 입력 받고 3자리마다 ,를 찍어주는

함수를 만들어 봅시다.
'''


def print_comma(number):
    zero = 0
    num = ''
    for i in reversed(number):
        num = i + num
        zero += 1
        if (zero == 3):
            num = ',' + num
            zero = 0
    print(num)
        

number = input('숫자를 입력해주세요 : ')
    
if (number.isnumeric()):
    print_comma(number)
else:
    print('숫자를 입력해주세요!')
