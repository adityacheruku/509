Flag = 'DLE'
End = 'ETX'
start = 'STX'
Data = input('Enter the Data: ')
count = 0
res = ' '
pos = 0

if Data.count(Flag) >= 1:
    count = 1
    pos = Data.index(Flag)
elif Data.count(start) >= 1:
    count = 1
    pos = Data.index(start)
elif Data.count(End) >= 1:
    count = 1
    pos += Data.index(End)
if count == 1:
    res = Flag+start+' '+Data[:pos]+'DLE'+Data[pos:]+' '+Flag+End
else:
    res = Flag+start+Data+Flag+End

print(res)
