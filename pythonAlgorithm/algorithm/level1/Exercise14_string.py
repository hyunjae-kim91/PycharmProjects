"""
문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요.
예를 들어 s가 a234이면 False를 리턴하고 1234라면 True를 리턴하면 됩니다.

제한 사항
s는 길이 1 이상, 길이 8 이하인 문자열입니다.
입출력 예
s	return
a234	false
1234	true
"""

s = '1234'

#문제 그대로 작성
def solution(s):
    try:
        if len(s)==4 or len(s) ==6:
            answer = True
        else:
            answer = False
        s = int(s)
    except:
        answer = False
    print(answer)

    return answer

#isdigit 함수 사용 (isalpha)
def solution1(s):
    print(s.isdigit() and len(s) in (4,6))
    return s.isdigit() and len(s) in (4,6)

#정규식 이용 (정규식 공부할 것...)
def solution2(s):
    import re
    print(bool(re.match("^(\d{4}|\d{6})$", s)))
    return bool(re.match("^(\d{4}|\d{6})$", s))

solution2(s)