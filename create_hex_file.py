def xcreate_hex_file(file_name, pattern):
    # Calculate the number of repetitions needed to fill 4 KB
    #pattern_length = len(pattern)
    #repetitions = 4096 // pattern_length
    #remainder = 4096 % pattern_length

    # Generate the content with the desired pattern
    #content = pattern * repetitions + pattern[:remainder]

    # Write the content to the file
    with open(file_name, 'wb') as file:
        file.write(bytes.fromhex(pattern))

if __name__ == "__main__":
    file_name = "hex_file.bin"
    x5x1   = '0100000000000000000011111111111111111111222222222222222222223333333333333333333344444444444444444444'
    x5x2   = '0200000000000000000011111111111111111111222222222222222222223333333333333333333344444444444444444444'
    x5x3   = '0300000000000000000011111111111111111111222222222222222222223333333333333333333344444444444444444444'
    x5x4   = '0400000000000000000011111111111111111111222222222222222222223333333333333333333344444444444444444444'
    x5x5   = '0500000000000000000011111111111111111111222222222222222222223333333333333333333344444444444444444444'
    x5x6   = '0600000000000000000011111111111111111111222222222222222222223333333333333333333344444444444444444444'
    x5x7   = '0700000000000000000011111111111111111111222222222222222222223333333333333333333344444444444444444444'
    x5x8   = '0800000000000000000011111111111111111111222222222222222222223333333333333333333344444444444444444444'
    x5x9   = '0900000000000000000011111111111111111111222222222222222222223333333333333333333344444444444444444444'
    x5x10  = '1000000000000000000011111111111111111111222222222222222222223333333333333333333344444444444444444444'
    x5x11  = '1100000000000000000011111111111111111111222222222222222222223333333333333333333344444444444444444444'
    x5x12  = '1200000000000000000011111111111111111111222222222222222222223333333333333333333344444444444444444444'
    x5x13  = '1300000000000000000011111111111111111111222222222222222222223333333333333333333344444444444444444444'
    x5x14  = '1400000000000000000011111111111111111111222222222222222222223333333333333333333344444444444444444444'
    x5x15  = '1500000000000000000011111111111111111111222222222222222222223333333333333333333344444444444444444444'
    x5x16  = '1600000000000000000011111111111111111111222222222222222222223333333333333333333344444444444444444444'
    x5x17  = '1700000000000000000011111111111111111111222222222222222222223333333333333333333344444444444444444444'
    x5x18  = '1800000000000000000011111111111111111111222222222222222222223333333333333333333344444444444444444444'
    x5x19  = '1900000000000000000011111111111111111111222222222222222222223333333333333333333344444444444444444444'
    x5x20  = '2000000000000000000011111111111111111111222222222222222222223333333333333333333344444444444444444444'

    one_k = x5x1+x5x2+x5x3+x5x4+x5x5+x5x6+x5x7+x5x8+x5x9+x5x10+x5x11+x5x12+x5x13+x5x14+x5x15+x5x16+x5x17+x5x18+x5x19+x5x20

#hexedit /home/kali/Desktop/OSWE/SQLi/Postgres/hex_file.bin
#hexedit /var/www/html/uploads/hex_file
#create_hex_file(file_name+'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF')
#create_hex_file(file_name, one_k+one_k+'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF')
   # print(f"File '{file_name}' created with a size of 4 KB and content pattern '{desired_pattern}'.")
