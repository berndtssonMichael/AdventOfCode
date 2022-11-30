import pathlib

# define data-file
ROOT_DIR = pathlib.Path(__file__).parent.parent
# input_file = ROOT_DIR / 'test/test.txt'
input_file = ROOT_DIR / '2021/input/16.txt'

input_data = open(input_file, 'r').readlines()[0]


# convert input_data to hex string
hex_string = ''.join(bin(int(char, 16))[2:].zfill(4) for char in input_data)


version_sum = 0 # store answer for A

def read_packages(input, start_pos):
    global version_sum
    # header info version and type_id
    calc = 0
    version = int(input[start_pos:start_pos + 3], 2) # pos 1-3
    version_sum += version
    id = int(input[start_pos + 3:start_pos + 6], 2) # pos 4-6

    start_pos += 6
    if id == 4:  # literal
        found_bit = True
        literal = ''
        while found_bit:
            bit = input[start_pos:start_pos + 6]
            found_bit = input[start_pos:start_pos + 1]  == '1'  # is first char 1 then we found a 5-bit
            literal += input[start_pos + 1:start_pos + 5]
            start_pos += 5
        return start_pos, int(literal, 2)
    else:  # operator
        calc = [0,1,-1,0,-0,-1,-1,-1][id]
        type = int(input[start_pos])
        assert type in (0, 1)
        start_pos +=  1
        count_packages = 0
        if type == 0:  # 15 bits defines size of next package
            # size = input[start_pos:start_pos + 15]
            next_package_size = int(input[start_pos:start_pos + 15], 2)
            start_pos += 15
            count_packages = next_package_size
        elif type == 1:  # 11 bits defines number of sub-package
            no_of_sub  = int(input[start_pos:start_pos + 11], 2)
            start_pos += 11
            count_packages = no_of_sub
        while count_packages:
            # is there more?
            pos, val = read_packages(input, start_pos)
            count_packages -= pos - start_pos if type == 0 else 1 #
            start_pos = pos
            if calc == -1:
                calc = val
            elif id == 0: # sum
                calc += val
            elif id == 1: # product
                calc *= val
            elif id == 2: # min
                calc = min(calc, val)
            elif id == 3: # max
                calc = max(calc, val)
            elif id == 5: # gt
                calc = (calc > val)
            elif id == 6: # lt
                calc = (calc < val)
            elif id == 7: # eq
                calc = (calc == val)
            if calc is True:
                calc = 1
            if calc is False:
                calc = 0
        return start_pos, calc


_, sum = read_packages(hex_string, 0)

print(f'version_sum: {version_sum}')
print(f'Part B: {sum}')

# 10626195124371
