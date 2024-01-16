from decimal import Decimal
import inflect
import traceback

def sum_digits(n):
    while n >= 10:
        # Convert the number to a list of digits and sum them
        n = sum(int(digit) for digit in str(n))
    return n

def odd_data(name):
    new_name = ''
    i = 0
    while i < len(name):
        new_name += name[i]
        i += 2
    return new_name

def even_data(name):
    new_name = ''
    i = 1
    while i < len(name):
        new_name += name[i]
        i += 2
    return new_name

def generator():
    final = []
    T = int(input('T: '))
    for _ in range(T):
        input_details = input()
        try:
            final_password = actual(input_details)
            final.append(final_password)
        except Exception as e:
            print(f"Runtime Error: {e}")
            traceback.print_exc()
            final.append("Invalid")
    for i in range(len(final)):
        print(final[i])

def actual(input_details):
    input_details = str(input_details)
    try:
        ind = input_details.index(' ')
        number = input_details[:ind]
        name = input_details[ind + 1:]

        x = Decimal(number)
        scientific_notation = f"{x:E}"

        dot = scientific_notation.index('.')
        e = scientific_notation.index('E')

        decimal_part = int(scientific_notation[dot + 1:e])
        decimal_sum = sum_digits(decimal_part)

        p = inflect.engine()
        numerical = p.number_to_words(scientific_notation[:dot])

        part_1 = ''.join([word[:3] for word in numerical.split()]) + scientific_notation[dot] + \
                 p.number_to_words(decimal_sum) + 'e' + ('+' if scientific_notation[e + 1] == '+' else '') + \
                 p.number_to_words(scientific_notation[e + 2:])

        if int(scientific_notation[e + 2:]) % 2 != 0:
            new_name = odd_data(name)
        else:
            new_name = even_data(name)

        final_password = part_1 + '@' + new_name
        return final_password

    except Exception as e:
        raise e

generator()
