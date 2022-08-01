# 모두를 위한 파이썬 PY4E 
# 1주차 팀 과제
# 팀: 턴태코치_2팀 / 작성자: jm / 작성일: 220717


"""
📌Q1. 파이썬으로 컴퓨터에게 우리가 원하는 일을 시킬 수 있다고 하였습니다.
     파이썬으로 할 수 있는 일은 어떤 것들이 있고, 나는 그중에서 무엇을 하고 싶은지 적어봅시다.


A_noas. 파이썬은 인공지능 개발, 데이터 마이닝, 작업 자동화, 드롭박스 같은 웹 어플리케이션 개발 등이 가능합니다. 저는 다양한 기능 중 데이터 마이닝에 치중하여 웹에서 제가 원하는 정보를 얻고 이를 정리해주는 프로그램을 만드는 것을 목표로 하고 있습니다.

A_jm. 파이썬을 통해 AI, 데이터사이언스, 웹 개발을 할 수 있다고 알고있습니다. 저는 파이썬을 통해 웹 백엔드 직무를 담당하고싶습니다.





📌Q2. 파이썬 코딩을 하기에 앞서 하드웨어를 이해하는 것이 중요하다고 했습니다.
     하드웨어 아키텍쳐에서 CPU와 Main Memory 그리고 Secondary Memory의 역할을
     간단하게 정리하여 봅시다.

A.
CPU:
- 하드웨어 중 제어장치로, 프로그램이 돌아갈 작업을 처리합니다. 주기억장치에서 프로그램 명령어와 데이터를 읽어와 처리하고 명령어의 수행 순서를 제어합니다.
- 중앙처리장치. 프로그램의 명령어를 해석하고 얻은 데이터를 처리 및 제어하는 장치입니다.

Main Memory:
- 주기억장치. 현재 CPU가 처리하고있는 내용을 저장하는 장치입니다. 용량이 크고 처리속도가 빠릅니다.
- CPU가 처리하고 있는 데이터와 명령어를 일시적으로 저장하는 역할을 합니다. 전원이 차단되면 일시적으로 저장된 모든 정보가 사라진다는 특징이 있습니다. 

Secondary Memory:
- Main memory의 단점을 보완하기 위한 기억 장치입니다. Main memory보다 속도는 느리지만 전원이 차단되어도 저장된 정보가 사라지지 않습니다.
- 보조기억장치. 물리적인 디스크가 연결되어있는 기억장치입니다. 비교적 처리속도가 느리지만 저장된 데이터가 사라지지 않고 영구적으로 보관 가능합니다.





📌Q3. 파이썬은 우리의 명령을 이해하지 못했을 때, 친절하게 Error Message를 통해
     어떤 명령을 이해하지 못했는지 알려줍니다.  그것을 보고 코드의 버그를 수정해가는 과정을
     Debugging이라고 합니다. 이것은 코딩에 있어서 매우 중요합니다.
     따라서, Error Message에 대해서 이해하는 시간을 가져봅시다.
     강의에서는 SyntaxError, ValueError, TypeError 3가지가 등장했습니다.

    1. 각각의 Error를 발생시키는 코드를 2가지씩 만들어보고
    2. Debugging한 코드도 만들어 봅시다.
    3. 그리고 그 밖에 다른 Error도 3가지를 찾아 그 Error를 발생시키는 코드와
    4. Debugging한 코드를 1가지씩 만들어 봅시다.


eTest1 = "Hello"
eTest2 = 123
eTest3 = 12.3

#             #
# SyntaxError #
#             #

printt("Hello")
# print("Hello")

print(Hello)
# print("Hello")

Kage = int(input(한국 나이를 입력해주세요 ))
# Kage = int(input("한국 나이를 입력해주세요 "))


if y = str('yes'):
    y = -1
if y = str('no'):
    y = -2
#
if y == str('yes'):
    y = -1
if y == str('no'):
    y = -2
#


#            #
# ValueError #
#            #

x = int('0.1')
print(x)
#
x = int('1')
print(x)
#

x = float('파이썬')
print(x)
#
x = float('0.5')
print(x)
#

x = str(0.1)
y = int(x)
# y = x


#           #
# TypeError #
#           #

x = 'python'
y = 'fun'
print(x*y)
#
x = 'python'
y = 'fun'
print(x*y)
#

x = 'hello'
y = 123
print(x+y)
#
x = 'hello'
y = 'world'
print(x+y)
#

eResult = eTest1+eTest2
# eResult = eTest2

eTest3/eTest2
# float타입으로 int타입을 나눗셈할 수 없음

print(eTest1 > 1)
# 문자열을 int와 비교연산을 할 수 없음

eTest1 = int("abc" + 3)
# int로 정의된 값에 문자열과 int를 덧셈할 수 없음



#                   #
# ZeroDivisionError #
#                   #

x = 2
y = 0
print(x%y)
#
x = 2
y = 1
print(x%y)
#


#                  #
# IndentationError #
#                  #

x = 2
while x < 10:
x = x + 2
print(x)

#
x = 2
while x < 10:
     x = x + 2
print(x)

#반복문 뒤에 블럭 처리 미작성시 오류
#


#           #
# NameError #
#           #


x = 2
while x < 10:
x = x + 2
prin(x)
#print(x)



📌Q4. 강의에서 미국과 유럽의 엘리베이터 층수를 변환하는 프로그램이 나왔습니다.
      그와 비슷하게 우리는 한국 나이를 미국 나이로 변환하는 프로그램을 코딩 해봅시다.
hint: 미국 나이는 생일이 지났는지 안지났는지가 중요하죠!
birth = int(input("생일이 지났습니까? 맞으면 0 아니면 -1 : "))

A:

# 방법1
kAge = 0
print("안녕하세요!\n")
print("한국 나이를 미국 나이로 변환하는 프로그램입니다.\n")
kAge = int(input("한국 나이를 두자리 숫자로 입력해주세요 : "))
birth = int(input("생일이 지났습니까? 맞으면 0 아니면 -1 : "))
print("당신의 미국 나이입니다 : ", kAge+birth , " 살이시네요!")

# 방법2-1 : 강의 내용 활용
Kage = int(input("한국 나이를 입력해주세요 "))
Standard = int(input("생일이 지났습니까? 지났으면 '0', 지나지 않았으면 '-1'를 입력해주세요 " ))
USage = Kage -1 + Standard
print("당신의 미국 나이는", USage, "세 입니다.")


# 방법2-2 : 조건문 활용
x = int(input("한국 나이를 입력해주세요 "))
y = str(input("생일이 지났습니까? 지났으면 'yes', 지나지 않았으면 'no'를 입력해주세요 " ))
if y == str('yes'):
    y = -1
if y == str('no'):
    y = -2
print("당신의 미국 나이는", x + y, "세 입니다.")

"""



