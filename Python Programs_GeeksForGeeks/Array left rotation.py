# Python Program for array left rotation
a=[1,2,3,4,5,6]
print('Array before rotation:\n',a)
k=2
for i in range(1,k+1):
    temp=a[0]

    for j in range(0,len(a)-1):
        a[j]=a[j+1]

    a[-1]=temp
print('Array after K times left rotation:\n',a)





