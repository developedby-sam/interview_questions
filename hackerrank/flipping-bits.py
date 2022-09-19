def flipping_bits(number):
    xor = '11111111111111111111111111111111'
    # converts decimal to 32 bit binary
    bin32 = '{:032b}'.format(number)
    return int(xor, base=2) ^ int(bin32, base=2)


print(flipping_bits(2147483647))
