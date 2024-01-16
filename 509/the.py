def perform_or_operation(binary1, binary2):
    # Ensure that the binary strings have the same length
    length = max(len(binary1), len(binary2))
    binary1 = binary1.zfill(length)
    binary2 = binary2.zfill(length)

    result = ''
    for bit1, bit2 in zip(binary1, binary2):
        # Perform OR operation for each pair of bits
        result += '1' if bit1 == '1' or bit2 == '1' else '0'

    return result

# Example Usage:
binary_num1 = '1101'
binary_num2 = '1010'

result = perform_or_operation(binary_num1, binary_num2)

print(f'The result of {binary_num1} OR {binary_num2} is: {result}')
