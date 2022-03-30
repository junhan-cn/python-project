#罗马数字转整数

def romanToInt():
    strs="IV"
    roman = {'I':1, 'V':5, 'X':10, 'L':50,'C':100, 'D':500, 'M':1000 }
    result = 0
    strsLens = len(strs)

    for i in range(strsLens-1):
        if roman[strs[i]] < roman[strs[i+1]]:
            result -= roman[strs[i]]

    print(result+roman[strs[strsLens-1]])

romanToInt()
