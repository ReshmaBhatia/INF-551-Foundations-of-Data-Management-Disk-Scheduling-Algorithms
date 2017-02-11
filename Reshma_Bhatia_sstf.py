import sys
input = open(sys.argv[-1], 'r')
line1 = input.readline().rstrip('\n')
line2 = input.readline()

head = int(line1)
#print 'head=',head

list = line2.split(',')
for t in list:
    list[list.index(t)] = int(t)
#print list

addition=0
xlist=[]
def work(head,addition,list):
    if head >99 :
        Flag=1
    else:
        Flag=0
    #newlist = []
    explist=[]
    minlist=[]
    for t in list:
    #newlist.append(head-t)
        explist.append(abs(head-t))
    #print '  explist', explist
    #print '  newlist', newlist
    if explist.count(min(explist))>1:
        indices=[i for i, v in enumerate(explist) if v == min(explist)]
        #print indices,'indices'
        for i in indices:
            minlist.append(list[i])
        #print minlist, 'minlist'
        if len(set(minlist))>1:
            if Flag==0:
                #print 'r'
                a=min(explist)
                head=min(minlist)
            else:
                #print 'c'
                a=min(explist)
                head=max(minlist)
        else:
            a=min(explist)
            head=minlist[0]

    else:
        a = min(explist)
        head = list[explist.index(a)]
    #print a
    #print explist.index(a)
    #print list[newlist.index(a)]
    xlist.append(head)
    #print a
    addition=addition+a
    #print addition
    #head =list[newlist.index(a)]
    list[list.index(head)]=sys.maxint
    #print list
    return head,addition,list

for t in range(0,len(list)):
    head,addition,list=work(head,addition,list)
#print head
print( ", ".join( repr(e) for e in xlist ) )
print addition
#print list



