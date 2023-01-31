def euclideanAlgoirthm(a, b):
    if a < b:
        return euclideanAlgoirthm(a, b-a)
    if b < a:
        return euclideanAlgoirthm(a-b, a)
    return a, b
        
        
print(euclideanAlgoirthm(24, 36))
#output is: (12, 12)