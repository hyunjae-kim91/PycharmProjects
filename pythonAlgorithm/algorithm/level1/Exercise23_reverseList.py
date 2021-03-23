"""
자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

제한 조건
n은 10,000,000,000이하인 자연수입니다.
입출력 예
n	return
12345	[5,4,3,2,1]
"""

n = 12345

def solution(n):
    answer = [int(i) for i in str(n)][::-1]
    print(answer)
    return answer

solution(n)

#map함수 풀이
def solution_1(n):
    answer = list(map(int,reversed(str(n))))
    return answer

