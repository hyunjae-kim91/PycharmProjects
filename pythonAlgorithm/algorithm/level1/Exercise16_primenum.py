"""
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)

제한 조건
n은 2이상 1000000이하의 자연수입니다.
입출력 예
n	result
10	4
5	3
입출력 예 설명
입출력 예 #1
1부터 10 사이의 소수는 [2,3,5,7] 4개가 존재하므로 4를 반환

입출력 예 #2
1부터 5 사이의 소수는 [2,3,5] 3개가 존재하므로 3를 반환
"""
n = 12

# print(set(range(2,n+1))-set(range(2,13,2)))


#[인터넷 참고] 에라토스테네스의 체 : 1을 제외하고 작은 숫자부터 배수를 리스트에서 지워나가면서 원하는 숫자까지 지워나가는 방법
def solution(n):
    # False는 1 또는 합성수, True는 소수 -> 처음 [False, False]는 0과 1 (리스트는 0부터 시작이기 때문에)
    a= [False,False] + [True] * (n-1)
    prime_list = []
    # 2부터 하나씩 소수 여부(True) 확인
    for i in range(2 , n + 1):
        # True면 소수 리스트에 추가
        if a[i]:
            prime_list.append(i)
        # i*2부터 n까지 step마다 합성수를 False로 만든다. (i*2인 이유는 i는 앞에서 걸러지지 않는 경우 소수라 생각, 걸러지면 어차피 False)
        for j in range(i*2, n+1, i):
            a[j] = False
    print(len(prime_list))

solution(n)






#[첫 풀이] 효율성 x
def solution_x(n):
    answer = 0
    not_prime = 0
    for i in range(2, n + 1):
        for j in range(1, int(math.sqrt(i)) + 1):
            if i // j != i and i % j == 0:
               not_prime += 1
               break
    print(n - 1 - not_prime)
    return answer

