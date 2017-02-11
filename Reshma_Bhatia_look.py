import sys
input = open(sys.argv[-1], 'r')
line1 = input.readline().rstrip('\n')
line2 = input.readline()
head = int(line1)
#print 'head=',head
if head<=99:
    Flag=0
else:
    Flag=1

list = line2.split(',')
equalist=[]
for t in list:
    list[list.index(t)] = int(t)
#print 'list=',list
#print 'listlen=',len(list)
for t in range(0,len(list)):
    if list[t]== head:
        equalist.append(list[t])
        #list.remove(list[t])
#print 'equalist=',equalist

list = [x for x in list if x != head]
#print 'nlist=',list

explist=[]
for t in list:
    #newlist.append(head - t)
    explist.append(abs(head-t))
minlist=[]
if len(set(list))>1:
    if explist.count(min(explist))>1:
        indices=[i for i, v in enumerate(explist) if v == min(explist)]
        #print indices,'indices'
        for i in indices:
            minlist.append(list[i])
        #print minlist, 'minlist'
        if len(set(minlist))>1:
            if Flag==0:
                newhead=min(minlist)
            else:
                newhead=max(minlist)
        else:
            newhead=minlist[0]

    else:
        a = min(explist)
        newhead = list[explist.index(a)]
else:
    if len(list)==0:
        newhead=equalist[0]
    else:
        newhead=list[0]
#print 'newhead=', newhead
#print 'b', newlist



LargerArray = []
SmallerArray = []
for l in list:
    if (l > head):
        LargerArray.append(l)

    else:
        SmallerArray.append(l)


#print'LargerArray=',LargerArray
#print 'SmallerArray=',SmallerArray
FinalList = []
ALarger = []
Dsmall = []
if len(equalist)>=1:
    for t in equalist:
        FinalList.append(t)



Addition=0
if len(set(list))>1:
    if (newhead > head):
        ALarger = sorted(LargerArray, key=int)
        #print 'ALarger=',ALarger
        Dsmall = sorted(SmallerArray, key=int, reverse=True)
        #print 'DSmall=',Dsmall
        for x in ALarger:
            FinalList.append(x)
        for y in Dsmall:
            FinalList.append(y)
        #print FinalList

        Addition+= (max(ALarger)-head)
        if len(Dsmall)>=1:
            Addition+=(max(ALarger)-min(Dsmall))
        #print Addition

    else:
        Alarger = sorted(LargerArray, key=int)
        #print 'Alarger2=',Alarger
        Dsmall = sorted(SmallerArray, key=int, reverse=True)  # descending order
        #print 'Dsmall2=',Dsmall
        for y in Dsmall:

            FinalList.append(y)
        #print 'PinalList=',FinalList
        # FinalList.append(0)
        for x in Alarger:
            #print 'h='
            FinalList.append(x)
        Addition+=head-min(Dsmall)
        if len(Alarger)>=1:
            Addition+=(max(Alarger)-min(Dsmall))

else:
    for t in list:
        FinalList.append(t)
    Addition=abs(head-newhead)
print( ", ".join( repr(e) for e in FinalList ) )
print Addition
