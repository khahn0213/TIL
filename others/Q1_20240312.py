# 2024/03/12 - Nota
# ref: https://blog.encrypted.gg/936
# point: stack

# input : '({})' , '([{}[(){}]])', '([)]'
# output : YES YES NO

# the answer
def check_right_pair(input_str):
    if len(input_str) % 2 == 1: return 'NO'
    
    stack_list = []
    for i, b in enumerate(input_str):
        if b == '(' or b == '{' or b == '[':
            stack_list.append(b)
            continue
        if b == ')':
            if len(stack_list) == 0 or stack_list[-1] != '(':
                return 'NO'
            else:
                stack_list.pop()
        if b == '}':
            if len(stack_list) == 0 or stack_list[-1] != '{':
                return 'NO'
            else:
                stack_list.pop()
        if b == ']':
            if len(stack_list) == 0 or stack_list[-1] != '[':
                return 'NO'
            else:
                stack_list.pop()
    return 'YES'


# the previous answer.
def check_bracket(input_str):
    if len(input_str) % 2 == 1: return 'NO'
    
    # # ver.1
    # bracket_dict = {}
    # for i, b in enumerate(input_str):
    #     if b not in bracket_dict.keys():
    #         bracket_dict[b] = [i]
    #     else:
    #         bracket_dict[b].append(i)
    # ver.1-1
    bracket_dict = {'(':[], ')':[],
                    '{':[], '}':[],
                    '[':[], ']':[]}
    for i, b in enumerate(input_str):
        bracket_dict[b].append(i)
    
    # index of each bracket.
    bracket_0 = bracket_dict['(']
    bracket_1 = bracket_dict[')']
    bracket_2 = bracket_dict['{']
    bracket_3 = bracket_dict['}']
    bracket_4 = bracket_dict['[']
    bracket_5 = bracket_dict[']']

    sup_j = len(input_str) // 2
    for i in bracket_0:
        for j in range(sup_j+1):
            if i + 1 + 2*j in bracket_1: return 'YES' # This was a wrong approach, indeed.
            # but still, i want to try one more time with this solution.abs
    
if __name__=="__main__":
    s = '(((())))'
    s = '([[][{}[{()[]}][]]])'
    print(check_right_pair(s))

    





