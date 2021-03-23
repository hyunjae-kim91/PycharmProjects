import collections
participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["marina", "josipa", "nikola", "filipa"]

#정렬 후, 비교 / 내가 푼 것
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            return answer
            break
    if answer == '':
        answer = participant[-1]
        return answer


#Python Dictionary (Hash 값 이용)
def solution1(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

#collections 라이브러리 사용으로 간단한 코딩
#collections.counter() 컨테이너에 동일한 값의 자료가 몇개인지를 파악하는데 사용하는 객체이다.

def solution2(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

#3.0 이후 버전에서 반환 값으로 리스트가 필요한 경우에는 list(a.keys())를 사용하면 된다.
#dict_keys, dict_values, dict_items 등은 리스트로 변환하지 않더라도 기본적인 반복(iterate) 구문(예: for문)을 실행할 수 있다.

solution2(participant, completion)