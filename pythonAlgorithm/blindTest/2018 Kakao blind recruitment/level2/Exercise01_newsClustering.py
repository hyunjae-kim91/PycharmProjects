
def solution_1(str1, str2):
    str1_list = [str1[i].upper() + str1[i + 1].upper() for i in range(0, len(str1) - 1) if
                 ord('A') <= ord(str1[i].upper()) <= ord('Z') and ord('A') <= ord(str1[i + 1].upper()) <= ord('Z')]
    str2_list = [str2[i].upper() + str2[i + 1].upper() for i in range(0, len(str2) - 1) if
                 ord('A') <= ord(str2[i].upper()) <= ord('Z') and ord('A') <= ord(str2[i + 1].upper()) <= ord('Z')]

"""
    if b == 0:
        answer = 65536
    else:
        answer = int(65536*a/b)

    return answer
"""

def solution(str1,str2):
    strings = []
    for string in [str1,str2]:
        conv = string.upper()
        convs = {}
        for i in range(len(conv)-1):
            word = conv[i] + conv[i+1]
            if word.isalpha():
                convs[word] = convs.get(word, 0) + 1
        strings.append(convs)

    str1, str2 = strings
    interaction = []
    for s1 in str1:
        if s1 in str2:
            interaction += [s1 for _ in range(min(str1[s1],str2[s1]))]

    union = []
    union_keys = list(str1.keys()) + list(str2.keys())

    for j in set(union_keys):
        union += [j for _ in range(max(str1.get(j,0),str2.get(j,0)))]

    n = len(interaction) / len(union) if len(union) != 0 else 1
    return int(n * 65536)



print(solution('handshake','shake hands'))
#print(solution('E=M*C^2', 'e=m*c^2'))



def solution(str1, str2):

    list1 = [str1[n:n+2].lower() for n in range(len(str1)-1) if str1[n:n+2].isalpha()]
    list2 = [str2[n:n+2].lower() for n in range(len(str2)-1) if str2[n:n+2].isalpha()]
    print(list1)
    print(list2)

    tlist = set(list1) | set(list2)
    print(tlist)
    res1 = [] #합집합
    res2 = [] #교집합

    if tlist:
        for i in tlist:
            res1.extend([i]*max(list1.count(i), list2.count(i)))
            res2.extend([i]*min(list1.count(i), list2.count(i)))
        answer = int(len(res2)/len(res1)*65536)
        return answer

    else:
        return 65536

print(solution('handshake', 'shake hands'))
#print(solution('E=M*C^2', 'e=m*c^2'))

a = [1]
a.extend([1]*2)
print([1]*2)
print(a)