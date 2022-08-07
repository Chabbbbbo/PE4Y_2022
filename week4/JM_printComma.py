
"""
📌Q1. 우리는 큰 수를 나타낼 때 3자리마다 , 를 찍어서 구분해 줍니다. 파이썬에서는 아래와 같이 쉽게 나타낼 수 있습니다.

# f"{숫자:,}"
print(f"{1000:,}")

하지만 이번 미션에서는 숫자를 입력 받고 3자리마다 ,를 찍어주는

함수를 만들어 봅시다.


🔽출력 예시

make_comma(1000000)
1,000,000

"""

def getNumber():
    num = input("숫자를 입력해주세요: ")
    if num.isnumeric():
        return num
    else:
        print("잘못된 값을 입력하셨습니다.")
        return getNumber()


print("\n******************************************")
print("입력한 숫자에 ','를 삽입하는 프로그램입니다.")
print("*********************************************")

num = int(getNumber())

print(f"make_comma({num})")
print(format(num, ","))
