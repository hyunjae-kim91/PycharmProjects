def solution(s):
    midnum = int(len(s) / 2)
    if len(s) % 2 == 1:
        answer = s[midnum]
    else:
        answer = s[midnum - 1: midnum + 1]
    print(answer)
    return answer

#if문 사용하지 않고 리스트 슬라이싱 성격 이용해서 풀기

def solution1(s):
    print(s[(len(s) - 1) // 2: (len(s)) // 2 + 1])

s = 'abcde'
s_1 = 'qwer'
solution1(s_1)