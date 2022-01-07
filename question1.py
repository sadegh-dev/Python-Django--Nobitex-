def separator(ls):
    elist = []
    olist = []
    for x in ls :
        if x % 2 == 0 :
            elist.append(x)
        else :
            olist.append(x)
    result = (elist,olist)
    return (result)
