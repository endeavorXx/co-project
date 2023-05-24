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
    "000": "R0",
    "001": "R1",
    "010": "R2",
    "011": "R3",
    "100": "R4",
    "101": "R5",
    "110": "R6",
    "111": "FLAGS"
}

f = open("output.txt")

mem = f.readlines()
print(mem)

pc = "0"*7

reg_file = {
    "R0": "0"*16,
    "R1": "0"*16,
    "R2": "0"*16,
    "R3": "0"*16,
    "R4": "0"*16,
    "R5": "0"*16,
    "R6": "0"*16,
    "FLAGS": "0"*16                  # V / L / G / E
}

while True:

    # for removing trailing "\n"
    query = mem[binary_to_decimal(pc)].strip()

    opcode = query[0:5]
    
    # Type A
    if opcode =="00000":

        temp_2= binary_to_decimal(reg_file[registers[query[10:13]]])
        temp_3= binary_to_decimal(reg_file[registers[query[13:16]]])
        reg_file[registers[query[7:10]]] = sixteen_bit_binary(decimal_to_7binary(temp_2+temp_3))
        
        
        
    if opcode == "00001":
        temp_2 = binary_to_decimal(reg_file[registers[query[10:13]]])
        temp_3 = binary_to_decimal(reg_file[registers[query[13:16]]])
        reg_file[registers[query[7:10]]] = sixteen_bit_binary(
            decimal_to_7binary(temp_2-temp_3))
        
    if opcode == "00110":
        temp_2 = binary_to_decimal(reg_file[registers[query[10:13]]])
        temp_3 = binary_to_decimal(reg_file[registers[query[13:16]]])
        reg_file[registers[query[7:10]]] = sixteen_bit_binary(
            decimal_to_7binary(temp_2*temp_3))
        
        

    if opcode == "01010":
        temp_2 = binary_to_decimal(reg_file[registers[query[10:13]]])
        temp_3 = binary_to_decimal(reg_file[registers[query[13:16]]])
        reg_file[registers[query[7:10]]] = sixteen_bit_binary(
            decimal_to_7binary(temp_2^temp_3))
    if opcode == "01011":

        temp_2 = binary_to_decimal(reg_file[registers[query[10:13]]])
        temp_3 = binary_to_decimal(reg_file[registers[query[13:16]]])
        reg_file[registers[query[7:10]]] = sixteen_bit_binary(
            decimal_to_7binary(temp_2|temp_3))
    if opcode == "01100":

        temp_2 = binary_to_decimal(reg_file[registers[query[10:13]]])
        temp_3 = binary_to_decimal(reg_file[registers[query[13:16]]])
        reg_file[registers[query[7:10]]] = sixteen_bit_binary(
            decimal_to_7binary(temp_2&temp_3))

    # Type B
    if opcode == "00010":
        reg_code = query[6:9]
        reg_type = registers[reg_code]
        reg_file[reg_type] = sixteen_bit_binary(query[9:])
    
    if opcode=="01000":
        print(reg_file[registers[query[6:9]]])
        for i in range(binary_to_decimal(query[9:16])):
            reg_file[registers[query[6:9]]] = "0"+reg_file[registers[query[6:9]]][0:-1]
    
    if opcode == "01001":
        print(reg_file[registers[query[6:9]]])
        for i in range(binary_to_decimal(query[9:16])):
            reg_file[registers[query[6:9]]] =reg_file[registers[query[6:9]]][1:]+"0"
        print(reg_file[registers[query[6:9]]])
        
        #Type C
    if opcode == "00011":
        reg1=query[10:13]
        reg2=query[13:16]
        reg_file[registers[reg1]]=reg_file[registers[reg2]]
        
    if opcode == "00111":
        temp_2 = binary_to_decimal(reg_file[registers[query[10:13]]])
        temp_3 = binary_to_decimal(reg_file[registers[query[13:16]]])
        reg_file["R0"] = sixteen_bit_binary(
            decimal_to_7binary(temp_2//temp_3))
        reg_file["R1"] = sixteen_bit_binary(
            decimal_to_7binary(temp_2%temp_3))
        
    if opcode == "01101":
        reg_file[registers[query[7:10]]] = sixteen_bit_binary(
            decimal_to_7binary(~binary_to_decimal(reg_file[registers[query[10:13]]])))
    if opcode == "01110":
        temp_2 = binary_to_decimal(reg_file[registers[query[10:13]]])
        temp_3 = binary_to_decimal(reg_file[registers[query[13:16]]])
        if temp_2 == temp_3:
            reg_file["FLAGS"] = reg_file["FLAGS"][:15]+"1"
        elif temp_2 > temp_3:
            reg_file["FLAGS"] = reg_file["FLAGS"][:14]+"1"+reg_file["FLAGS"][15]
        else:
            reg_file["FLAGS"] = reg_file["FLAGS"][:13] +"1"+reg_file["FLAGS"][14:]
        



            

    if opcode == "11010":
        break
    
    pc = decimal_to_7binary(binary_to_decimal(pc) + 1)

f.close()
