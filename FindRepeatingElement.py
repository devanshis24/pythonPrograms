#Second maximum repeating number
def RemovemaxRepeating(n, int_list):
    elementCounts ={}
    if n > len(int_list):
        print "Not Vallid"
    else:
        for i in int_list:
            elementCounts[i] = elementCounts.setdefault(i,0) + 1
        if n in elementCounts.values():
            for item, count in elementCounts.items():
                if count == n:
                    print item
        else:
            print "No Element Repeats for n times"
                

def main():
    RemovemaxRepeating(5, [1,3,2,4,3,4,3,2])

main()
