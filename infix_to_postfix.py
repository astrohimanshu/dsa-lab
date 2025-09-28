#%%
operator = {'+': 0, '-':0,'*':1,'/':1,'^':2}
def inf_to_post(exp):
    stack = []
    output = []
    for token in exp:
        if token.isalnum():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        elif token in operator.keys():
            while stack and operator[token] <= operator[stack[-1]]:
                output.append(stack.pop())
            stack.append(token)
    while stack:
        output.append(stack.pop())
    return ''.join(output)

expr = 'a+b'
print(inf_to_post(expr))


#%%
operand = {'+': 0, '-':0,'*':1,'/':1,'^':2}
a = '+'
print(a in operand.keys())
if []:
    print('sfdf')