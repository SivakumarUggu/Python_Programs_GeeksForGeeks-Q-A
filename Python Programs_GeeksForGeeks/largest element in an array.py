# Python Program to find largest element in an array.

arr=[12,54,23,19,34]
max=0
for num in arr:
    if num>max:
        max=num
print(f'Largest number in given array is: {max}')