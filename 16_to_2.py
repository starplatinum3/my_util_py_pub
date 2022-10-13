
x="EF"
bin_of_16=bin(int(x, 16))

print("bin_of_16",bin_of_16)
# bin_of_16 0b11101111

def beauty16_to_bin(hex):
    bin_of_16=bin(int(hex, 16))
    print("bin_of_16",bin_of_16)
    bin_of_16=bin_of_16[2:]
    print("bin_of_16",bin_of_16)
    bin_of_16=bin_of_16.zfill(8)
    print("bin_of_16",bin_of_16)
    return bin_of_16

beauty16_to_bin("EF")