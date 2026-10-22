# Experiment 12: CRC (Cyclic Redundancy Check)

def mod2div(dividend, divisor):
    bits = list(dividend)
    divisor_len = len(divisor)

    for i in range(len(bits) - divisor_len + 1):
        if bits[i] == '1':
            for j in range(divisor_len):
                bits[i + j] = '0' if bits[i + j] == divisor[j] else '1'

    return ''.join(bits[-(divisor_len - 1):])


def valid_bits(value):
    return bool(value) and all(bit in '01' for bit in value)


data = input("Enter Data Bits: ").strip()
key = input("Enter Generator Polynomial: ").strip()

if not valid_bits(data) or not valid_bits(key) or len(key) < 2 or key[0] != '1':
    print("Enter valid binary data and a valid generator polynomial (starting with 1).")
else:
    appended_data = data + '0' * (len(key) - 1)
    remainder = mod2div(appended_data, key)
    codeword = data + remainder

    print("CRC Remainder:", remainder)
    print("Transmitted Codeword:", codeword)

    received = input("Enter Received Codeword: ").strip()

    if not valid_bits(received) or len(received) < len(key):
        print("Enter a valid received binary codeword.")
    else:
        check = mod2div(received, key)
        if all(bit == '0' for bit in check):
            print("No Error Detected")
        else:
            print("Error Detected")
