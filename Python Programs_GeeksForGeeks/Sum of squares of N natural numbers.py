#Python Program for Sum of squares of first n natural numbers
n=int(input('Number of natural numbers:'))
sum=0
for num in range(1,n+1):
    num_square=num**2
    sum+=num_square
print(f'Sum of square of first n natural no. is:', sum)

