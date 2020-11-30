def cipher(msg,key,op):

    #getting chars
    with open ("cripto_chars.txt", "r") as myfile:
        file_r = myfile.readlines()[4]
    file_find = file_r.find(' ')
    file_r2 = file_r.split()
    chars = ' '.join(file_r2)
    chars_n = int(len(chars) - 1)

    #getting equation
    with open ("cripto_chars.txt", "r") as myfile:
        eq_e = myfile.readlines()[6]
    eq_e2 = eq_e.split()
    eq_e = ''.join(eq_e2)

    #coded msg var
    code_msg = ''

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
    lis = [key]*(len(msg)+1)
    for i in range(1,len(lis)):
        if eq_e == 'default':
            if lis[i-2]%2==0:
                lis[i] = 1+sum(lis[i-2:i])
            if lis[i-2]%2!=0:
                lis[i] = int(lis[i-2]/5)
        else:
            eq = lambda x: eval(eq_e)
            lis[i] = eq(lis[i-1])
    lis = lis[1:]

    #Function
    for i in range(len(msg)):
        #function for coding
        if op == 'c':
            if msg[i] in chars:
                code_msg += chars[int((chars.find(msg[i]) - lis[i])%chars_n)]
            else:
                code_msg += msg[i]
        #Function for decoding
        if op == 'd':
            if msg[i] in chars:
                code_msg += chars[int((chars.find(msg[i]) + lis[i])%chars_n)]
            else:
                code_msg += msg[i]
    return code_msg
