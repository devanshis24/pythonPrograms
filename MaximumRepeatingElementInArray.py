def MaximumRepeatingElement(a_list):
    m = {}
    x = list()
    for i in a_list:
        if i in m:
            m[i] = m[i] + 1
        else:
            m[i] = 1

    l = list(m.values())
    maximum = max(l)
    smax = 0
    for i in l:
        if(i > smax and i<maximum):
            smax = i

    for i in a_list:
        if(m[i] == smax) and (i not in x):
            x.append(i)
            
    print x

def main():
    MaximumRepeatingElement([1,2,3,2,5,3,6,3,2,5,2,4,2,5])

main()
