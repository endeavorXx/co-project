def decimal_to_7binary(num):
    "This function takes integer number and returns a string of binary no converts from decimal"
    binary = ""
    while num != 0:
        binary += str(num % 2)
        num = num // 2
    binary = binary[::-1]  # reverses string
    n = len(binary)
    binary = "0"*(7-n) + binary
    return binary

def binary_to_decimal(bin):
    n = len(bin) - 1
    num = 0
    for i in bin:
        num += int(i)*(2**n)
        n = n-1    
    return num

def sixteen_bit_binary(text):
    text = "0"*9 + text
    return text

opcode = {
    "add": "00000",
    "sub": "00001",
    "mov": ["00010", "00011"],
    "ld": "00100",
    "st": "00101",
    "mul": "00110",
    "div": "00111",
    "rs": "01000",
    "ls": "01001",
    "xor": "01010",
    "or": "01011",
    "and": "01100",
    "not": "01101",
    "cmp": "01110",
    "jmp": "01111",
    "jlt": "11100",
    "jgt": "11101",
    "je": "11111",
    "hlt": "11010"
}

registers = {
    "R0": "000",
    "R1": "001",
    "R2": "010",
    "R3": "011",
    "R4": "100",
    "R5": "101",
    "R6": "110",
    "FLAGS": "111"
}

f = open("simin.txt")

mem = f.readlines()
print(mem)

pc = "0"*7

reg_file = {
    "R0":"0"*16,
    "R1":"0"*16,
    "R2":"0"*16,
    "R3":"0"*16,
    "R4":"0"*16,
    "R5":"0"*16,
    "R6":"0"*16,
    "FLAGS":"0"*16                  # V / L / G / E
}

while True:

    query = mem[binary_to_decimal(pc)].strip()           # for removing trailing "\n"

    opcode = query[0:5]

    # Type B 
    if opcode == "00010":
        pc = decimal_to_7binary(binary_to_decimal(pc) + 1)
        reg_code = query[6:9]
        for key in registers:
            if registers[key] == reg_code:
                reg_type = key
        reg_file[reg_type] = sixteen_bit_binary(query[9:]) 

    if opcode == "1101":
        break

f.close()