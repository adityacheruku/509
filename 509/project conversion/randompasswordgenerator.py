def password_generator():
    from string import ascii_letters,digits

    import random

    letters = list(ascii_letters)
    numbers = list(digits)
    symbols = ['@','$','^','&','*','&','?','|','>','<']

    count_letters = int(input('how many letters do u want '))
    count_symbols = int(input('How many symbols do you want '))
    count_numbers = int(input('How many numbers do you want '))

    password_list = []

    for i in range(1, count_letters):
        password_list += random.choice(letters)

    for i in range(1, count_numbers):
        password_list += random.choice(numbers)
    
    for i in range(1, count_symbols):
        password_list += random.choice(symbols)
    

    random.shuffle(password_list)
    final_answer = ' '
    for i in password_list:
        final_answer += i

    return(final_answer) 


pas = password_generator()

print(pas)
