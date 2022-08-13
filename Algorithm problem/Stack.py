# 使用List的末尾作为栈顶 时间复杂度为O(1)
# 如果使用List的开头作为栈顶 时间复杂度为o(n)

class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)

""" # 括号匹配算法
def parcheck(strs):
    balance = True
    i = 0
    s = Stack()
    while i < len(strs) and balance:
        str = strs[i]
        if str in "([{":
            s.push(str)
        else:
            if s.isEmpty():
                balance = False
            else:
                top = s.pop()
                if not match(top,str):
                    balance = False
        i += 1
    if balance and s.isEmpty():
        return True
    else:
        return False
def match(opener,closer):
    openers = '([{'
    closers = ')]}'
    return openers.index(opener) == closers.index(closer)


print(parcheck('(()){}'))
print(parcheck('((()))){{}[][]))(())})))')) """

""" # 十进制转换为十六进制以下的数字
def baseconver(number, base):
    dig = "0123456789ABCDEF"
    s =Stack()
    newstr = ''
    while number > 0:
        rem = number % base
        s.push(rem)
        number = number // base
    while not s.isEmpty():
        newstr += dig[s.pop()]
    return newstr

print(baseconver(25,6))
print(baseconver(44,15)) """

""" # 中缀表达式转换为后缀表达式
def infixTopostfix(infix):
    priority = {}
    priority["*"] = 3
    priority["/"] = 3
    priority["+"] = 2
    priority["-"] = 2
    priority["("] = 1

    s = Stack()
    postfix = []
    tokenlist = infix.split()
    
    for token in tokenlist:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in '0123456789':
            postfix.append(token)

        elif token == '(':
            s.push(token)

        elif token == ')':
            toptoken = s.pop()
            while toptoken != '(':
                postfix.append(toptoken)
                toptoken = s.pop()

        else:
            while (not s.isEmpty()) and (priority[s.peek()] >= priority[token]):
                postfix.append(s.pop())
            s.push(token)

    while not s.isEmpty():
        postfix.append(s.pop())

    return ' '.join(postfix)

print(infixTopostfix('A * B + C - D')) """

# 后缀表达式求值
def postfixEval(postfix):
    opstack = Stack()
    tokenlist = postfix.split()

    for token in tokenlist:
        if token in '0123456789':
            opstack.push(int(token))
        else:
            operand2 = opstack.pop()
            operand1 = opstack.pop()
            res = domath(token, operand1, operand2)
            opstack.push(res)

    return opstack.peek()

def domath(op, op1, op2):
    if op == '+':
        return op1 + op2
    elif op == '-':
        return op1 - op2
    elif op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2
    else:
        s = "cannot do math apart from '+-*/'"
        return s

print(postfixEval('7 8 + 3 2 + /'))