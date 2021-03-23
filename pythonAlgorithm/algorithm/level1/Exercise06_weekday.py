import datetime

def solution(a,b):
    #datetime 라이브러리 이용, %a -> 요일을 글자로 ex. Tue
    answer = datetime.datetime(2016,a,b).strftime('%a').upper()
    return answer

a = 5
b = 24
solution(a,b)