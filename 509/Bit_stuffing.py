Data = input('Enter the Data: ')
init = 0
count = 0
flag = '01111110'
print(Data[init])
length = len(Data)
# G musukoni chey ra pooka
while (length >= init):
    if Data[init] == '1':
        count += 1
        if count == 6:
            Data = Data[:init] + '0' + Data[init:]
            count = 0
    elif Data[init] == '0':
        count = 0
    init += 1

print(flag+Data+flag)
