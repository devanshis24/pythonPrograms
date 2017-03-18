def  doesNotIntersectStrightLines(n, a1,a2,b1,b2,c1,c2,d1,d2):
    x = "false1"
    if (a1 == b1 or a2 == b2) and (c1 == d1 or c2 == d2):
        if (a1 == b1 and c1 == d1 and a1 != c1) or (a2 == b2 and c2 == d2 and a2 != c2) :
            x = "true0"
        elif a1 == b1:
            if c1 == d1:
                if c1 > a2 and d1 < b2:
                    x = "false2"
            elif c2 == d2:
                if c2 > a2 and d2 < b2:
                    x = "false3"
            else:
                x ="true"
        elif a2 == b2:
            if c1 == d1:
                if c1 > a1 and d1 < b1:
                    x = "false 4"
            elif c2 == d2:
                if c2 > a1 and d2 < b1:
                    x = "false5"
            else:
                x ="true1"
        else:
            x = "true2"
    else:
        x = "true3"
    print x
    
