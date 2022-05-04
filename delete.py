
def calculate(a,b,c,d,e,f,g,h,i,j,k,l):
    row1=[int(a),int(b),int(c),int(j)]
    row2=[int(d),int(e),int(f),int(k)]
    row3=[int(g),int(h),int(i),int(l)]
    for i in range(0,len(row1)):
        row1[i]=row1[i]/row1[0]
    while not row2[0]== 0:
        fac=row2[0]/row1[0]
        for i in range(0,len(row1)):
            row2[i]=row2[i]-(fac*row1
                             [i])
            row2[i]=row2[i]/row2[1]
        for i in range(0,len(row1)):
            row2[i]=row2[i]/row2[1]
            
    while not row3[0]== 0:
        fac=row3[0]/row1[0]
        for i in range(0,len(row1)):
            row3[i]=row3[i]-(fac*row1
                             [i])
        fac2=row3[1]/row2[1]    

        while not row3[1]==0:
            for i in range(0,len(row1)):
                row3[i]=row3[i]-(fac2*row2[i])

            for i in range(0,len(row1)):
                row3[i]=row3[i]/row3[2]

    print(row1)
    print(row2)
    print(row3)


while 0<1:   
    a=input("(1,1) or input 'd' for demo or 'q' to quit ")
    if a=="d":
        calculate(1,1,1,2,3,5,4,0,5,5,8,2)
            
    elif a=="q":
        break

    else:
        b=input()
        c=input()
        d=input()
        e=input()
        f=input()
        g=input()
        h=input()
        i=input()
        j=input()
        k=input()
        l=input()

        try:
            calculate(a,b,c,d,e,f,g,h,i,j,k,l)
        except:
            print("the given equations are not solvable")
            
