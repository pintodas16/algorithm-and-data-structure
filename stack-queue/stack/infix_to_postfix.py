



def prece(ch):
    if(ch == '^'):
        return 3
    elif ch== '*' or ch=='/':
        return 2
    elif ch == '+' or ch == '-':
        return 1
    else:
        return 0
def top(stack):
    return stack[len(stack)-1]

def in_to_post(s):
    
    stack = list()
    result = ''
    for i in s : 
        if (i>='a' and i<='z') or (i>='A' and i<='Z') or (i>='0' and i<='9'):
            result += i
        elif i == '(':
            stack.append(i)
        elif i == ')':
            
            while (top(stack)!= '('):
                result += top(stack)
                stack.pop()
            stack.pop()
        else:
            while (len(stack) !=0 and prece(top(stack)) >= prece(i) ):
                result += top(stack)
                stack.pop()
            stack.append(i)
    
    while (len(stack) != 0):
        result += top(stack)
        stack.pop()
        
    print(result)
        

in_to_post("3+5*(5-3)")
in_to_post("3+5*(5/5)-2^2")