def ListSubSet(myset, chosen):
    
    if len(myset) == 0:
        return [chosen]
    else:
        first = myset[0]
        rest = myset[1:len(myset)]
        print(first, rest)
        including = chosen + first
        withChosen = ListSubSet(rest , including)
        excluding  = chosen
        withoutChosen = ListSubSet(rest,excluding)
        return withChosen + withoutChosen
        
myset = "AB"
print(ListSubSet(myset,""))
