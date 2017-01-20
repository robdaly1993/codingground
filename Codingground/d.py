# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    #SUM OF INDEX/UP TO INDEX = SUM ON THE RIGHT
    sum_left = 0
    sum_right = sum(A)
    

        #iterate through A
    for i in A:
        sum_right = sum_right - A[i]
        
        if sum_left == sum_right:
            return i
        sum_left = sum_left + i
    return -1    
            #IF Satisfy condtion
                 #RETURN P[I]
    
    
    #RETURN -1
A = [-1, 3, -4, 5, 1, -6, 2, 1]    
print(solution(A))
    