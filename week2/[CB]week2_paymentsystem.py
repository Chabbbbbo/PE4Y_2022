"""
📌Q2. 월급을 입력하면 연봉을 계산해주는 계산기를 만들어 봅시다. 세전 연봉과 세후 연봉을 함께 출력하도록 해봅니다.
   📑아래의 세율 표를 토대로 만들어주세요(단, 실제 세율과 다를 수 있습니다!)
 
 1200만원 이하 : 6%
 4600만원 이하 : 15%
 8800만원 이하 : 24%
 1억 5천만원 이하 : 35%
 3억원 이하 : 38%
 5억원 이하 : 40%
 5억원 초과 : 42%
"""


def tariff_cal(year_pay):
    if (year_pay >= 1200):
        tariff = 0.06
    elif (year_pay >= 4600):
        tariff = 0.15
    elif (year_pay >= 8800):
        tariff = 0.24
    elif (year_pay >= 15000):
        tariff = 0.15
    elif (year_pay >= 30000):
        tariff = 0.38
    elif (year_pay >= 50000):
        tariff = 0.40
    else:
        tariff = 0.42
    return tariff
    

def main_print():
    print('''
    ============== 세전/세후 연봉 계산기 =============
    월급을 입력해주시면 세전/세후 연봉을 계산해드립니다:)
    ''')


def main():
    main_print()
    while(1):
        try:
            month_pay = int(input('월급을 숫자로 입력해주세요(단위:만원) : '))
            if (month_pay == 0):
                print('월급이 만원 미만입니다. 다시 입력해주세요.\n')
                continue
        except:
            print('월급을 숫자로 입력해주세요 :)\n')
            continue
        year_pay = month_pay * 12
        tariff = tariff_cal(year_pay)
        real_year_pay = int(year_pay * (1 - tariff))
        print('='*40)
        print('계산 금액은 만원단위로 나타냅니다.')
        print(f'- 세전 연봉 : {year_pay}만원\n- 세후 연봉 : {real_year_pay}만원')
        print('='*40)

        print('계산을 계속하시겠습니까?')
        choice = input('계속 하시려면 enter를 눌러주세요. (다른 키를 입력하면 프로그램이 종료됩니다)')
        if (choice == ''):
            continue
        else:
            print('연봉계산기를 종료합니다:)')
            break

if __name__ == "__main__":
	main()
