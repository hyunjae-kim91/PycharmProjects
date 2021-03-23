def binary(n, a):
    notation = '0123456789ABCDEF'
    q, r = divmod(n, a)
    b = notation[r]
    return binary(q, a) + b if q else b

def solution(n, t, m, p):
    string = ""
    list_number = m * (t - 1) + p
    number = 0
    answer = ""
    while len(string) < list_number:
        string += str(binary(number,n))
        number += 1
    for i in range(t):
        answer += string[i * m + p - 1]
    return answer


print(solution(2,4,2,1))
print(solution(16,16,2,1))
print(solution(16,16,2,2))
#"0111"
#"02468ACE11111111"
#"13579BDF01234567"
#진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p 가 주어진다.