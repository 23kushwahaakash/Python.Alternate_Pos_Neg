lst1=[-5,-10,3,1,10,-6]
lst2=[0]*len(lst1)
pos1,pos2=0,1
for n in lst1:
    if n<0:
        lst2[pos2]=n
        pos2+=2
    else:
        lst2[pos1]=n
        pos1+=2
print(lst2)

