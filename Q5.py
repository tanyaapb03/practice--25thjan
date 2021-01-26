#There are two sorted arrays A and B of size m and n respectively. 
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

def median(a,b):
    m=len(a)
    n=len(b)
    median=(m+n)/2
    return median
print(median([2,4,5,6,7],[3,4,5,7]))


#Find the kth largest element in an unsorted array.
#  Note that it is the kth largest element in the sorted order, not the kth distinct element.

def largest(arr,k):
    arr=sorted(arr)
    print(arr)
    return arr[k]
print(largest([3,6,7,4],1))