#Python Program to check if given array is Monotonic.
arr1=[1,2,3,4,5]
arr=[12,10,7,4,2]
arr3=[32,46,10,5,70,80,99]
# def ismonotonic(arr):
#    return (all(arr[i]<=arr[i+1] for i in range(0, len(arr)-1)) or all(arr[i]>=arr[i+1] for i in range(0, len(arr)-1)))
# print(ismonotonic(arr))
def is_mono(arr):
   a=1;b=1;
   l1=len(arr)
   for i in range(0,len(arr)-1):
      if(arr[i]>=arr[i+1]):
         a=a+1
      elif(arr[i]<=arr[i+1]):
         b=b+1
   if(a==l1 or b==l1):
      return True
   else:
      return False

print(is_mono(arr))
