# Python Program for n\’th multiple of a number in Fibonacci Series.

list2=[]
a,b=0,1
N=int(input('Enter number of elements in the series you want: '))
print(a,b, end=' ')
for i in range(3,N+1):
    new_ele=b+a
    print(new_ele, end=' ')
    list1 = []
    for j in range(1,new_ele+1):
        if new_ele%j==0:
            list1.append(j)
    print(list1)
    list2.append(list1)
    b, a = new_ele, b
print(list2)



