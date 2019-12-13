# coding=utf-8
p = 'программист'

n1 = list(range(1001))
#i = input()
for i in n1:
    ln = len (str( i ))
    #print (i),
    #print (type(i)),
    #print (ln)

    if ln == 1:
        if i == 1:
            print (i) ,
            print (p)
        elif 2 <= i <= 4:
            print (i) ,
            print (p + 'а')
        else :
            print (i) ,
            print (p + 'ов')

    if ln == 2 :
        i1 = i % 10
        i2 = i // 10
        if 1 <= i2 < 2:
            if  1 <= i1 <= 9:
                print (i) ,
                print (p + 'ов')
        elif 2 <= i2 <= 9:
                if i1 == 1:
                    print (i) ,
                    print (p)
                elif 2 <= i1 <= 4:
                    print (i) ,
                    print (p + 'а')
                else :
                    print (i) ,
                    print (p + 'ов')

    if ln == 3 :
        i3 = i % 100
        i2 = i % 10
        i1 = i
        #print (i),
        #print (i3),
        #print (i2),
        #print (i1)
        ln1 = len(str(i3))
        if ln1 == 1:
            if i2 == 1:
                print (i) ,
                print (p)
            elif 2 <= i2 <= 4:
                print (i) ,
                print (p + 'а')
            else :
                print (i) ,
                print (p + 'ов')

        elif ln1 == 2 :
            if 11 <= i3 < 20:
                print (i) ,
                print (p + 'ов')
            elif i3 >= 2:
                if i2 == 1:
                    print (i) ,
                    print (p)
                elif 2 <= i2 <=4:
                    print (i) ,
                    print (p + 'а')
                else :
                    print (i) ,
                    print (p + 'ов')

    if ln == 4 :
        print (i) ,
        print (p + 'ов')