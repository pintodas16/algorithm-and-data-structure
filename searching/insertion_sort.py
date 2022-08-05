


def insertation(arr):
    length = len(arr)
    
    for i in range(1,length):
        item = arr[i]
        
        j = i - 1
        
        while j>=0 and arr[j] > item : 
            arr[j+1] = arr[j]
            j-=1
            arr[j+1] = item 
    return arr


if __name__ == "__main__":
    arr = [5,4,3,2,1]
    
    print("before the arr : ")
    print(arr)
    
    
    print("after sorted the array")
    ans = insertation(arr)
    print(ans)
    