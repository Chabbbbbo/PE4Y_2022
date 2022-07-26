"""
📌Q3. 학생 이름과 점수를 입력하면 학점을 출력하는 학점 변환기를 만들어 봅시다.
이름과 점수, 학점 모두 출력하도록 해봅니다.
 
   📑아래의 학점표를 토대로 만들어주세요
A+ : 95~100점
A  : 90~94점
B+ : 85~89점
B  : 80~84점
C+ : 75~79점
C  : 70~74점
D+ : 65~69점
D  : 60~64점
F  : 60점 미만

   🔽출력 예시
# 이름과 점수 입력
grader("이호창", 99)

# 출력
학생이름 : 이호창
점수 : 99점
학점 : A+
"""
import re


def score_trans(score):
    if (score < 0):
        grade = 0
    elif (score < 60):
        grade = 'F'
    elif (score <= 64):
        grade = 'D'
    elif (score <= 69):
        grade = 'D+'
    elif (score <= 74):
        grade = 'C'    
    elif (score <= 79):
        grade = 'C+'
    elif (score <= 84):
        grade = 'B'
    elif (score <= 89):
        grade = 'B+'
    elif (score <= 94):
        grade = 'A'
    else:
        grade = 'A+'
    
    return grade

def main_print():
    print('''
    ================== 차보대학교 1학기 파이선 학점 결과 =================
    1학기 차보대 파이선 공부하시느냐 수고하셨습니다!

    학생 '이름'과 파이선 기말고사 '점수'를 입력해주시면 학점을 알려드립니다:)
    두근두근~ 과연 이번 학점은?
    ''')

def main():
    main_print()
    while(1):
        name = input('이름을 입력해주세요 : ')
        name_check = re.search('[0-9]+', name)
        if (name_check != None):
            print('엣헴... 이름을 제대로 입력해주세요\n')
            continue
        try:
            score = int(input('점수를 입력해주세요 : '))
        except:
            print('엣헴... 점수를 숫자 형태로 입력해주세요\n')
            continue

        grade = score_trans(score)
        if (grade == 0):
            print('점수가 0보다 낮습니다. 다시 입력해주세요\n')

        print('\n============ 학점 결과 ============')
        print('- 학생 이름 : ',name)
        print('- 입력 점수 : ',score)
        print('- 학점 결과 : ',grade)

        top_list = ['A+', 'A', 'B+', 'B']
        if not (grade in top_list):
            print('덧) 재이수를 추천드립니다.....')
        print('====================================')

                
        print('\n학점확인을 계속하시겠습니까?')
        choice = input('계속 하시려면 enter를 눌러주세요. (다른 키를 입력하면 프로그램이 종료됩니다)')
        if (choice == ''):
            continue
        else:
            print('연봉계산기를 종료합니다:)')
            break

if __name__ == "__main__":
	main()


