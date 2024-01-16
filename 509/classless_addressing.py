address = input('Enter addres with mask')
if "/" in address:
    address,mask = address.split('/')
    p_mask = int(mask)
else:
    print('Enter the mask too..')

def to_binary(data):
    bin_data = bin(data)
    loc = bin_data.index('b')
    bin_data = bin_data[loc+1:]
    return bin_data.zfill(8)
adr = []

for _ in address:
    adr = address.split('.')

address = ''
for ad in adr:
    address += to_binary(int(ad))

mask = '1'*p_mask + '0'*(32-p_mask)

def OR(data1,data2):
    result = ''
    for b1,b2 in zip(data1,data2):
        result += '1' if b1 == '1' or b2 == '1' else '0'
    return result
def comp(data):
    d = ''
    for s in data:
        if s == '0':
            d += '1'
        else:
            d += '0'
    return d
    
def AND(data1,data2):
    result = ''
    for b1,b2 in zip(data1,data2):
        result += '1' if b1 == '1' and b2 == '1' else '0'
    return result

starting_address = AND(mask,address)
starting_address = int(starting_address[24:],2)
ending_address = OR(comp(mask),address)
ending_address = int(ending_address[24:],2)
print('starting_address: ',starting_address,'\n','ending_address is: ',ending_address)