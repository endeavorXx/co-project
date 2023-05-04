def decimal_to_binary(num):
    binary = ""
    while num!=0:
        binary += str(num%2)
        num = num//2
    binary = binary[::-1]
    return binary

opcode = {
    "add":"00000",
    "sub":"00001",
    "mov":["00010","00011"],
    "ld":"00100",
    "st":"00101",
    "mul":"00110",
    "div":"00111",
    "rs":"01000",
    "ls":"01001",
    "xor":"01010",
    "or":"01011",
    "and":"01100",
    "not":"01101",
    "cmp":"01110",
    "jmp":"01111",
    "jlt":"11100",
    "jgt":"11101",
    "je":"11111",
    "hlt":"11010"
}



registers = {
    "R0":"000",
    "R1":"001",
    "R2":"010",
    "R3":"011",
    "R4":"100",
    "R5":"101",
    "R6":"110",
    "FLAGS":"111"
             }

print(decimal_to_binary(12))