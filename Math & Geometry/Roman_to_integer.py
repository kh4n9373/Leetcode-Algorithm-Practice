def romanToInt(s):
    hashmap = {
        'I' : 1,
        'V' : 5,
        'X' : 10, 
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
    res = 0
    for i in range(len(s)):
        if i-1 >= 0 and hashmap[s[i-1]] < hashmap[s[i]]:
            res = res + hashmap[s[i]] - 2*hashmap[s[i-1]]
        else:
            res += hashmap[s[i]]
        print(res)
    return res
print(romanToInt("MCMXCIV"))