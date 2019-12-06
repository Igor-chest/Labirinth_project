def hashFile(fileName):
    f = open(fileName, 'r')
    codfile = []
    for line in f:
        #codline=[]
        for char in line:
            cod = str(ord(char))
            cod = '0'*(3-len(cod))+cod
            for i in cod:
                codfile.append(int(i))
            #codline.append(cod)
        #codfile.append(''.join(codline))
    f.close()
    #print(codfile)
    fCode(codfile,False)
    f2 = open(fileName, 'w')
    for i in codfile:
        f2.write(i)
    f2.close()
    #print(codfile)


def unHash(fileName):
    f = open(fileName, 'r')
    for line in f:
        st = line
    codfile = []
    for i in st:
        codfile.append(int(i))
    fCode(codfile, True)
    st = "".join(codfile)
    #print(st)
    f.close()
    f2 = open(fileName, 'w')
    for i in range(0, len(st), 3):
        #print(st[i]+st[i+1]+st[i+2])
        #print(chr(int(st[i]+st[i+1]+st[i+2])))
        f2.write(chr(int(st[i]+st[i+1]+st[i+2])))
    f2.close()


def fCode(arrNumber, flag):
    #print(arrNumber)
    fib2 = [1, 1]
    pos = 0
    i = 0
    while pos < len(arrNumber):
        fib2[i % 2] += fib2[not i % 2]
        strNum = str(fib2[i % 2])
        i += 1
        #print(strNum)
        for j in strNum:
            if pos >= len(arrNumber):
                break
            #print(arrNumber[pos])
            arrNumber[pos] = str(((int(arrNumber[pos]) + (flag * (-1) + 1 * (not flag)) * int(j))) % 10)
            #print(arrNumber)
            pos += 1
    #print(arrNumber)


for i in ('point.txt', 'record.txt', 'save.txt', 'password.txt'):
    unHash(i)
    #hashFile(i)
#hashFile('test.txt')')
