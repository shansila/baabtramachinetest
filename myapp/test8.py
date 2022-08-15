def findCommon(ar1, ar2, ar3, n1, n2, n3):
 
    # Initialize starting indexes for ar1[], ar2[] and ar3[]
    i, j, k = 0, 0, 0
 
    # Iterate through three arrays while all arrays have elements
    while (i < n1 and j < n2 and k < n3):
 
        # If x = y and y = z, print any of them and move ahead
        # in all arrays
        if (ar1[i] == ar2[j] and ar2[j] == ar3[k]):
            print (ar1[i]),
            i += 1
            j += 1
            k += 1
 
        # x < y
        elif ar1[i] < ar2[j]:
            i += 1
 
        # y < z
        elif ar2[j] < ar3[k]:
            j += 1
 
        # We reach here when x > y and z < y, i.e., z is smallest
        else:
            k += 1
 
 
# Driver program to check above function
ar1 = [10,11,12,13,14,15]
ar2 = [12,13,14,15,16]
ar3 = [14,15,16,17,18]
n1 = len(ar1)
n2 = len(ar2)
n3 = len(ar3)
print('coomon elements are')
findCommon(ar1, ar2, ar3, n1, n2, n3)