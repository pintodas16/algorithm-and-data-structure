

def bubble(arr):
    length = len(arr)
    for i in range(length):
        for j in range(length-1):
            if arr[j]> arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
    return arr



if __name__ == "__main__":
    # arr = [5,4,3,2,1]
    # arr = [1,2,3,4,5]
    arr = [1,2,3,7,6,5]
    
    print("before the arr : ")
    print(arr)
    
    
    print("after sorted the array")
    ans = bubble(arr)
    print(ans)
    