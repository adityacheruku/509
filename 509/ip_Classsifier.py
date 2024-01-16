ip_address = input('Enter the IP Address')


def find_class(bin_value):
    if bin_value[:1] == '0':
        print('Class A')
    elif bin_value[:2] == '10':
        print('Class B')
    elif bin_value[:3] == '110':
        print('Class C')
    elif bin_value[:4] == '1110':
        print('Class D')
    elif (bin_value[:4] == '1111'):
        print('Class E')


if '.' in ip_address:
    blocks = ip_address.split('.')
    field_1 = int(blocks[0])
    bin_value = bin(field_1)
    trash, binary = bin_value.split('b')
    act_binary = binary.zfill(8)
    find_class(act_binary)
elif (len(ip_address) == 32):
    find_class(ip_address[:4])
