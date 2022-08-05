

def selection(arr):
    length = len(arr)
    for i in range(length-1):
        index = i
        for j in range(i+1 , length):
            # if arr[i]<arr[j] : # desending order 
            if arr[i]>arr[j]: # assending order 
                index = j
                
        arr[i],arr[index] = arr[index],arr[i]
        # print(arr)
    return arr
                
    



if __name__ == "__main__":
    # arr = [5,4,3,2,1]
    arr = [1,2,3,4,5]
    
    print("before the arr : ")
    print(arr)
    
    
    print("after sorted the array")
    ans = selection(arr)
    print(ans)
    