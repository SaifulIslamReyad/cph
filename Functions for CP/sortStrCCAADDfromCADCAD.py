def sortStrCCAADDfromCADCAD(old):
    l=[]
    
    for i in old:
        l.append(old.index(i))
    l.sort()
    ll=[]
    for i in l:
        ll.append(old[i])
    new= '' .join(ll)
    return new
print(sortStrCCAADDfromCADCAD("CADCADCABCAB"))




