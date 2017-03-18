def print2Smallest(arr, target):
 
    
    arr_size = len(arr)
    if arr_size < 2:
        print "Invalid Input"
        return
    # Two variables to maintain value and two to maintain difference
    nearest1 = nearest2 = temp1 = temp2 = 1000
    for i in range(0, arr_size):
        print "arr i: ",arr[i]

        # If current difference is smaller than smaller difference 
        # update both diferences and both values
        if abs(target-arr[i]) < temp1:
            temp2 = temp1
            temp1= abs(target-arr[i])
            nearest2 = nearest1
            nearest1 = arr[i]
            
 
        # If difference is in between smaler difference and second smaller
        # update second difference and secnd value
        elif (abs(target-arr[i]) < temp2 and arr[i] != nearest1):
            temp2 = abs(target-arr[i])
            nearest2 = arr[i]
            print "inside nearest2",nearest2
            
 
    if (nearest2 == 1000):
        print "No second smallest element"
    else:
        print 'The smallest element is',nearest1,'and' \
              ' second smallest element is',nearest2

    print nearest1+nearest2
    
def main():
    print2Smallest([21,6,27,18],22)

main()
