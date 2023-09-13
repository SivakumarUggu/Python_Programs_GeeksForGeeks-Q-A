# Check if a given number is fibonacci number. note: N is a number in fibonacci series.
a, b=0, 1
list1=[]
list1.append(a)
list1.append(b)
no_of_elements=int(input('Enter number of elements you want in the fib series: '))
print(a, b, end=' ')
for i in range(3,no_of_elements+1):
    new_ele=b+a
    print(new_ele, end=' ')
    list1.append(new_ele)
    b, a=new_ele, b
print('\n',list1)
k=int(input('Enter a number you want to search in fib series: '))
if k in list1:
        print('Given number is present in the fib series.')
else:
        print('Given number does not exist in fib series.')


