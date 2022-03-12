arr = [54,26,93,17,77,31,44,55,20]

def bubbleSortNotOptimized():
    for j in range(len(arr)-1, 0 ,-1):
        for i in range(j):
            temp = 0
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
    print(arr)
    
def bubbleSortOptimized():
    for j in range(len(arr)-1, 0, -1):
        for i in range(j):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
    print(arr)

print('#1 Bubble Sort sem optimização')  
bubbleSortNotOptimized()
print('--------------------------------------------')
print('#2 Bubble Sort optimizado')  
bubbleSortOptimized()