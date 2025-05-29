def Print_odd(n):
    if n>0:
        print(2*n-1,end=" ")
        Print_odd(n-1)
odd=Print_odd(20)
print(odd)