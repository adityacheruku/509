def convertor(data):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    if isinstance(data, int):
        return alphabets[data]
    else:
        data = data.lower()
        for i in range(26):
            if data == alphabets[i]:
                return i

def encryption(data,shift):
    enc_word = ''
    for word in data:
        pos = convertor(word)
        pos = (pos+shift)%26
        new_word = convertor(pos)
        enc_word += new_word

    return enc_word

def decryption(data,shift):
    return encryption(data,-shift)

def main():
    opt = int(input('choose...\n1.classic ceaser\n2.shift-n ceaser\n'))
    shifter = 0
    if(opt==1):
        shifter = 3    
    elif(opt ==2):
        shifter = int(input('Enter the shift/key value : '))
    
    data = input('Enter the word for encrypting : ')
    enc_word = encryption(data,shifter)
    print('Encripted Word : ',enc_word)
    encripted_word = input('Enter the ncripted word : ')
    dec_word = decryption(encripted_word,shifter)
    print('decripted  Word : ',dec_word)  

if __name__ == "__main__":
    main()