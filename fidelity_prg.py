data = 100
def fact(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact*i
    return fact 
print(fact(10))

def reverse_no(num):
    rev_num = 0
    while num != 0:
        rem = num % 10
        rev_num = (rev_num * 10) + rem
        num = num // 10
    return rev_num
print(reverse_no(112))