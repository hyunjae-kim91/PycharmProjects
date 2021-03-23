from itertools import permutations

def divide(expression,operator):
    exp_list = []
    temp = ""
    for i in expression:
        if i not in operator:
            temp += i
        else:
            temp = int(temp)
            exp_list.append(temp)
            exp_list.append(i)
            temp = ""
    exp_list.append(int(temp))
    return exp_list

def operate(str, num_1, num_2):
    if str == '-':
        return num_1 - num_2
    elif str == '*':
        return num_1 * num_2
    else:
        return num_1 + num_2


def solution(expression):
    operator = ['-', '*', '+']
    answer = []
    exp_list = divide(expression, operator)
    operator_list = list(permutations(operator,3))
    for tmp in operator_list:
        temp_list = exp_list
        for i in tmp:
            stack = []
            while temp_list:
                stack.append(temp_list[0])
                if stack[-1] == i:
                    #print(stack[-1], stack[-2], exp_list[j+1])
                    temp_number = operate(stack[-1],stack[-2],temp_list[1])
                    stack = stack[:len(stack)-2]
                    stack.append(temp_number)
                    temp_list = temp_list[2:]
                else:
                    temp_list = temp_list[1:]
            temp_list = stack
        answer.append(abs(temp_list[0]))
    return max(answer)

#좋은 풀이
def solution(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            print(e)
            temp = [f"({i})" for i in e.split(b)]
            print(temp)
            temp_list.append(f'({b.join(temp)})')
            print(temp_list)
        answer.append(abs(eval(a.join(temp_list))))
        print("답 : ", answer)
    return max(answer)

expression = "100-200*300-500+20"
#expression = "50*6-3*2"

print(solution(expression))


print(eval("20/30"))
# f접두사로 {} 불러올 수 있다.
# eval 함수는 문자열 받아서 문자열 내 식 계산 (강력한 도구이나 매우 위험해서 사용 조심)
