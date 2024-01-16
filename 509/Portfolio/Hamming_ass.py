def parity(r,n,Data_word):
    for pos in r:
        bits = [int(Data_word[i-1]) for i in range(1, n+1) if (i & pos) != 0 and i != pos]
        parity = sum(bits) % 2
        Data_word[pos-1] = str(parity)
    
    return Data_word

def error(data,n,recieved):
    pos = [str(n-i) for i in range(n) if data[i]!=recieved[i]]
    return ''.join(pos)

def hamming():
    Data_size = int(input('Enter size of dataword: '))
    r_size = 1
    while 2**r_size < Data_size + r_size + 1:
        r_size +=1
    print('r is : ',r_size)
    n = r_size+Data_size
    print('n: ',n)
    Data_word = input('Enter the Data word: ')
    data = Data_word
    Data_word = list(Data_word)

    r = [2**i for i in range(r_size)]
    print('values of r are :\n')
    for i in range(len(r)):
        print(f"r{i+1}:",r[i]) 
    for j in range(n):
        if j in r:
            Data_word.insert(j-1,' ')

    codeWord = parity(r,n,Data_word)
    codeWord = ''.join(codeWord)
    print('codeword : ',codeWord)

    recieved_data = input('Enter recieved data: ')
    err_pos = error(data,Data_size,recieved_data)
    print('Error position : ',err_pos)

hamming()
