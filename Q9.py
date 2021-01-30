#Given an array of integers, find two numbers such that they add up to a specific target number.
#The function twoSum should return indices of the two numbers such that 
# they add up to the target, where index1 must be less than index2. 
# Please note that your returned answers (both index1 and index2) are not zero-based.

# /psuedo code 
# > create a function containg array and target as input> 
# > create two pointers and loop over the array in nested manner to compare 
# value at 0 index with all the others and soo on . with condition if their um == target 


def checksum(nums,target):
    result=[]
    pairs=[]
    

    for i in range(len(nums)):
        for j in range(len(nums)):
            if int(nums[i]+nums[j]) == target:
                
                pairs.append([{i:nums[i]},{j:nums[j]}])
                
            j=j+1
        i=i+1
    result.append(pairs)
           
    

    return result

print(checksum([2, 7, 11, 15],9))

    

        