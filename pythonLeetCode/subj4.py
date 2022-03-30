#最长公共前缀
#!/usr/bin/python3 

def longestCommonPrefix():
    strs = ["cir", "car"]
    res=''
    #commonStrs = list(zip(strs[0],strs[1],strs[2]))
    commonStrs = list(zip(*strs))

    for i in commonStrs:
        if len(set(i)) == 1:
            res = res + i[0]
        else:
            break

    print(res)

longestCommonPrefix()