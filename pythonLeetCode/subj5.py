# 有效的括号
#!/usr/bin/python3 

def isValide():
    s="()[]{}"
    tmp=['1']
    slen = len(s)
    for i in range(slen):
        if tmp[-1] == '(' and s[i] == ')':
            tmp.pop()
        elif tmp[-1] == '[' and s[i] == ']':
            tmp.pop()
        elif tmp[-1] == '{' and s[i] == '}':
            tmp.pop()
        else:
            tmp.append(s[i])
    if len(tmp) == 1:
        print("True")
        return True
    else:
        print("False")
        return False

        
isValide()
