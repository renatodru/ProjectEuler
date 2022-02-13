


s = [1,2]
s += [(s := [s[1], s[0] + s[1]]) and s[1] for k in range(4*10**6)]
print(len(s))
soma = 0
for i in s:
    if i%2 == 0: soma +=i 

print(s)