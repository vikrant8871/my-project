def Print_even(n):
    if n>0:
        print(2*n,end=" ")
        Print_even(n-1)
even=Print_even(10)
print(even)