def pushZerosToEnd(arr, n): 
    count = 0
    for i in range(n): 
        if arr[i] != 0:
           arr[count] = arr[i] 
           count+=1            
    while count < n: 
          arr[count] = 0
          count += 1
arr = [0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
n = len(arr) 
arr.sort()
pushZerosToEnd(arr, n) 
print(arr)
