import random
def transp(q):
    l=[]
    for i in q:
        l.append([])
    i=0
    while i!=9:
        ii=0
        while ii!=9:
            l[i].append(q[(ii//3)+3*(i//3)][ii-3*(ii//3)+3*(i%3)])
            ii+=1
        i+=1
    c=[]
    for i in q:
        c.append([])
    i=0
    while i!=9:
        ii=0
        while ii!=9:
            c[i].append(l[ii][i])
            ii+=1
        i+=1
    return(q,l,c)
def possib(q):
    l=transp(q)[1]
    c=transp(q)[2]
    a=[]
    for i in q:
        a.append([])
        for ii in q:
            a[-1].append([])
    i=1
    while i!=10:
        ii=0
        while ii!=9:
            iii=0
            while iii!=9:
                if i not in q[ii] and q[ii][iii]==0 and i not in l[(iii//3)+(ii//3)*3] and i not in c[iii%3+(ii%3)*3]:
                    a[ii][iii].append(i)
                iii+=1
            ii+=1
        i+=1            
    return(a)
def obv(q):
    a=possib(q)
    qlin=[]
    for i in q:
        qlin.append(i.copy())
    i=1
    while i!=10:
        ii=0
        while ii!=9:
            i4=0
            iii=0
            while iii!=9:
                for i5 in a[ii][iii]:
                    if i5==i:
                        i4+=1
                iii+=1
            if i4==1:
                i6=0
                while i6!=9:
                    if i in a[ii][i6]:
                        qlin[ii][i6]=i
                    i6+=1
            ii+=1
        i+=1
    
#"""
    a=possib(qlin)
    i=1
    while i!=10:
        ii=0
        while ii!=9:
            i4=0
            iii=0
            while iii!=9:
                if len(a[ii][iii])==1:
                    qlin[ii][iii]=a[ii][iii][0]
                iii+=1
            ii+=1
        i+=1
#"""

    return (qlin)
def obvs(q):
    i=0
    while i==0:
        qlin=obv(q)
        if qlin==q:
            i=1
        if qlin!=q:
            q=[]
            for j in qlin:
                q.append(j.copy())
    return (qlin)
def rand(q):
    a=possib(q)
    qlin=[]
    for i in q:
        qlin.append(i.copy())
    r=random.choice(a)
    i=a.index(r)
    ii=0
    while ii==0:
        rr=random.choice(r)
        if r==[[],[],[],[],[],[],[],[],[]]:
            return(q)
        if rr!=[]:
            ii=1
    ii=r.index(rr)
    qlin[i][ii]=random.choice(rr)
    return (qlin)
def check(q):
    i=1
    if q ==None:
        return None
    qlin=(obvs(rand(obvs(q))))
    alin=possib(qlin)
    while i!=10:
        ii=0
        while ii!=9:
            if i not in qlin[ii]:
                iii=0
                S=0
                while iii!=9:
                    if i not in alin[ii][iii]:
                        S+=1
                    iii+=1
                if S==9:
                    return None
            ii+=1
        i+=1
    return(qlin)
def achar(q):
    i=0
    while i<250:
        #print(i)
        qlin=check(q)
        if qlin == None:
            continue
        else:
            S=0
            for ii in qlin:
                S+=sum(ii)
            if S==405:
                return (qlin) 
        i+=1
def dubachar(q):
    i=0
    while i<250:
        print(i)
        qlin=check(check(q))
        if qlin == None:
            continue
        else:
            S=0
            for ii in qlin:
                S+=sum(ii)
            if S==405:
                return (qlin) 
        i+=1
def Main():
    0
q=[[0,5,0,0,0,6,0,0,0],[1,7,0,0,0,0,0,2,0],[0,0,4,5,0,0,0,0,0],[0,0,8,0,0,0,0,1,0],[9,1,0,0,0,6,0,0,2],[0,7,0,0,0,9,0,0,0],[0,6,0,3,0,0,0,0,0],[4,5,0,0,0,0,0,0,9],[0,0,7,0,8,0,0,0,0]]
#q=[[5,4,0,0,0,0,0,7,8],[8,1,0,0,0,4,9,0,0],[0,0,0,0,0,0,0,0,2],[0,6,9,0,2,0,1,0,5],[0,0,0,0,0,0,0,0,0],[3,0,5,0,7,0,4,6,0],[2,0,0,0,0,0,0,0,0],[0,0,3,1,0,0,0,7,9],[7,1,0,0,0,0,0,3,6]]
#print((obvs(q)))
#print(obvs(rand(obvs(q))))
#print(transp(q)[1])
print (achar(q))