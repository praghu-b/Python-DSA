x = int(input("Enter the size of the list: "))
arr = []

for i in range(x):
    arr[i] = int(input(f'Enter the value for index {i}: '))

print('Find the indexes...')

for i in range(arr):
    for j in range(i+1,arr):
        if arr[i]==arr[j]:
            print([i, j])