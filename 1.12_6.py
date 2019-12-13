# coding=utf-8
#n1 = '235'
n1 = input()
n1 = str(n1)
ln = len(n1)
p = 'программист'
n = n1


if (n1):
        if ln == 1:
            n = int((str(n[-1])))
            if n == 1:
                print (n1),
                print (p)
            elif 2 <= n <= 4:
                 print (n1),
                 print (p + 'а')
            else:
                print (n1),
                print (p + 'ов')

        elif ln == 2:
            n = int(n)
            if 10 <= n <= 20:
                print (n1),
                print (p + 'ов')
            if 21 <= n <= 99:
                n = str(n)
                n = (n[-1])
                n = int(n)
                if n == 1:
                    print (n1),
                    print (p)
                elif 2 <= n <= 4:
                     print (n1),
                     print (p + 'а')
                else:
                    print (n1),
                    print (p + 'ов')

        elif ln == 3:
            n = int(n)
            if 100 <= n <= 120:
                n = int(n) % 100
                if n == 1:
                    print (n1),
                    print (p)
                elif 2 <= n <= 4:
                    print (n1),
                    print (p + 'а')
                else:
                    print (n1),
                    print (p + 'ов')
            elif 121 <= n <= 199:
                n = int(n) % 100
                n = n % 10
                if n == 1:
                    print (n1),
                    print (p)
                elif 2 <= n <= 4:
                    print (n1),
                    print (p + 'а')
                else:
                    print (n1),
                    print (p + 'ов')

        elif ln == 4:
            print (n1),
            print (p + 'ов')