def Print_even(n):
    if n>0:
        print(2*n,end=" ")
        Print_even(n-1)
even=Print_even(10)
print(even)

def sum_even(n):
    if n==0:
        return 0
    s=2*n + sum_even(n-1)
    return s
    
even=sum_even(10)
print("Sum of 10 even no",even)