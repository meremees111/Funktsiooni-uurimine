
def leia_kasvamine(sisend):
    tuletis = diff(sisend)
    vaheldus_piirkond = solve(tuletis, x)
    intervalid = []
    i = 0
    while i < len(vaheldus_piirkond):
        if len(vaheldus_piirkond) > 1:
            intervalid.append(['-L', vaheldus_piirkond[0]])
            intervalid.append([vaheldus_piirkond[-1], 'L'])
            if vaheldus_piirkond.index(vaheldus_piirkond[i]) == 1:
                i += 1
            intervalid.append([vaheldus_piirkond[0], vaheldus_piirkond[1]])
            i += 1
        elif len(vaheldus_piirkond) == 1:
            intervalid.append(['-L', vaheldus_piirkond[0]])
            intervalid.append([vaheldus_piirkond[0], 'L'])
            i += 1
    for i in intervalid:
        if intervalid.count(i) > 1:
            intervalid.remove(i)
    print(intervalid)

leia_kasvamine(sisend)
