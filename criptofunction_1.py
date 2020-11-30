def cipher(message,key,tip):

    #getting chaars
    with open ("cripto_chars.txt", "r") as myfile:
        b = myfile.readlines()[4]
    d = b.find(' ')
    b1 = b.split()
    alfab = ' '.join(b1)
    alfab_n = int(len(alfab) - 1)

    #msg var
    newmsg = ''

    #key
    if type(key) == int or type(key) == float:
        key = int(key)
    else:
        key,key1 = str(key),0
        for i in key:
            key1 = key1+ord(i)
        key = key1
    while key>100:
        key= int(key/10)
    lis = [key]*(len(message)+1)
    for i in range(1,len(lis)):
        if lis[i-2]%2==0:
            lis[i] = 1+sum(lis[i-2:i])
        if lis[i-2]%2!=0:
            lis[i] = int(lis[i-2]/5)
    lis = lis[1:]

    #Function
    for i in range(len(message)):
        #function for coding
        if tip == 'c':
            if message[i] in alfab:
                newmsg += alfab[int((alfab.find(message[i]) - lis[i])%alfab_n)]
            else:
                newmsg += message[i]
        #Function for decoding
        if tip == 'd':
            if message[i] in alfab:
                newmsg += alfab[int((alfab.find(message[i]) + lis[i])%alfab_n)]
            else:
                newmsg += message[i]
    return newmsg
