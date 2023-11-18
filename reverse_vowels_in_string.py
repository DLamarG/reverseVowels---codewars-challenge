def reverse_vowels(s):
    import re
    if s=="":
        return s
    vow = ('a','e','i','o','u', 'A','E','I','O','U')
    vowels = []
    new_L = []
    lst1 = list(s)
    for i in lst1:
        if i in vow:
            vowels.append(i)
            new_L.append('-_')
        if re.match(r'[\D]', i) and i not in vow:
            new_L.append(i)
    rev_vow = list(reversed(vowels))
    fin_chg = []
    for j in new_L:
        if re.match(r'[\D]', j) and j!='-_':
            fin_chg.append(j)
        if j=='-_':
            first_char = rev_vow.pop(0) if len(rev_vow) > 0 else []
            fin_chg.append(first_char)
    return ''.join(fin_chg)

print(reverse_vowels("Hello!"))#--> "Holle!"
print(reverse_vowels("Tomatoes"))#--> "Temotaos"
print(reverse_vowels("Reverse Vowels In A String"))#--> "RivArsI Vewols en e Streng"