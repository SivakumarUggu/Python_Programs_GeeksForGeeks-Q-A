arr=[1,2,3,4,5,6,7]
print(f'Array before rotation:\n',arr)
k=2
for i in range(1,k+1):
    temp=arr[-1]

    for j in range(-1,-len(arr),-1):
        arr[j]=arr[j-1]

    arr[0]=temp

print(f'Array after right rotation:\n',arr)