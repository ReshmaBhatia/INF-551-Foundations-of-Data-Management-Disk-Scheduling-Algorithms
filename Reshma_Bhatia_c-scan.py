import sys
input = open(sys.argv[-1], 'r')
line1 = input.readline().rstrip('\n')
line2 = input.readline()

head = int(line1)
#print 'head=',head

list = line2.split(',')
for t in list:
    list[list.index(t)] = int(t)
#print 'intlist=',list

equalist=[]
for t in range(0,len(list)):
    if list[t]== head:
        equalist.append(list[t])
#print 'equalist=',equalist

list = [x for x in list if x != head]
#print 'nlist=',list

LargerArray = []
SmallerArray = []

for l in list:
    if (l > head):
        LargerArray.append(l)
    else:
        SmallerArray.append(l)

#print'LargerArray=',LargerArray
#print 'SmallerArray=',SmallerArray

LargeAscSsort = sorted(LargerArray, key=int)
SmallAscSort = sorted(SmallerArray, key=int)
#print 'LargeAscSort=',LargeAscSsort
#print 'SmallAscSort=',SmallAscSort
FinalList=[]
if len(equalist)>=1:
    for t in equalist:
        FinalList.append(t)
for x in LargeAscSsort:
    FinalList.append(x)
for y in SmallAscSort:
    FinalList.append(y)
print( ", ".join( repr(e) for e in FinalList ) )
Addition=0
if len(SmallAscSort)==0 and len(LargeAscSsort)>=1:
    Addition=max(LargeAscSsort)-head
elif len(SmallAscSort)>=1 and len(LargeAscSsort)==0:
    Addition=199-head+199+max(SmallAscSort)
elif len(SmallAscSort)==0 and len(LargeAscSsort)==0:
    Addition =0
else:
    Addition = 199-head+199+max(SmallAscSort)

print Addition