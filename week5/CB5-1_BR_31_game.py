'''
📌Q1. 여러분 혹시 베스킨라빈스31 게임을 아시나요? 
1부터 31까지 숫자를 플레이어들끼리 번갈아 외치다가 31을 외치는 사람이 패배하는 게임인데요.
이번엔 이 게임을 파이썬 함수로 만들어 봅시다. 
지성이 없이 숫자를 랜덤하게 외치는 컴퓨터와 대결을 해보겠습니다.

😲조건1 - 나의 턴에서는 숫자를 직접 입력하며 한 번 입력 후에 space 한 번으로 구분
😲조건2 - 나와 컴퓨터 모두 한 턴에 1회 ~ 3회까지만 숫자를 외칠 수 있음
😲조건3 - 외쳐진 숫자보다 1큰 수만 외칠수 있음 (ex: 5 다음엔 무조건 6)
위 조건이 안맞을 경우 다시 입력'''

import random


br_list = [0]

def br31(number_list):
    for i in number_list:
        br_list.append(i)
    print(f'현재 숫자 : {br_list[-1]}')

    computer_num = random.randint(1,3)

    for i in range(computer_num):
        next = int(br_list[-1]) + 1
        if (next > 31) :
            return 
        print(f'컴퓨터 : {next}')
        br_list.append(next)

    print(f'현재 숫자 : {br_list[-1]}')
    return

    

    
def main_print():
    print('''
    컴터가! 좋아하는! 랜덤! 게임! 게임~ 스타트!

    베스킨~ 라빈쓰~ 써리~원!
    귀엽고~ 깜찍하게~ 써리~원! >_<///
    (연속하는 숫자를 3개까지 입력할 수 있습니다>_< )
    ''')


def main():
    main_print()
    while(br_list[-1] < 31):
        try:
            number = input("My turn! 숫자를 입력해주세요(space로 구분) : ")
            number_list = number.split(' ')
        except:
            print('숫자로 입력해주세요!')
            continue
        
        br31(number_list)
    
    print('31 당첨! 마셔라~~~')

if __name__ == "__main__":
	main()