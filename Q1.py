#rotate array 

def rotatearray(arr):

    new_arr=[]
    for i in range(len(arr)-1, -1, -1):

        new_arr.append(arr[i])
        
    return new_arr

print(rotatearray("roots"))