def reverse_number(n):
    sign=1
    if n<0:
        sign=-1
        n=-n
        
    rev=0
    while n>0:
        rev= rev * 10 + (n % 10)
        n//=10
    return sign*rev

n=int(input(" "))
print(reverse_number(n))
