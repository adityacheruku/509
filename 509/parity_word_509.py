size = int(input('Enter the size of the data word'))
DataWord = input('Enter the DataWord')
length = len(DataWord)
if length != size:
    print('Enter correct length word')
choice = int(input('Choice of parity:\n1.EVEN 2.ODD\n'))
count = DataWord.count('1')
if choice == 1:
    if count % 2 == 1:
        print('Parity computed ::')
        print('DataWord constructed', DataWord + '1')
    else:
        print('Parity computed ::0')
        print('DataWord constructed', DataWord + '0')
elif choice == 2:
    if count % 2 == 1:
        print('Parity computed ::0')
        print('DataWord constructed', DataWord + '0')
    else:
        print('Parity computed ::1')
        print('DataWord constructed', DataWord + '1')
