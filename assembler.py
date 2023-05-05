def decimal_to_binary(num):
    "This function takes integer number ansd returns a string of binary no convertes from decimal"
    binary = ""
    while num!=0:
        binary += str(num%2)
        num = num//2
    binary = binary[::-1]           #reverses string
    return binary

def choose_register(reg_num):
    "This function returns opcode of registers"
    return registers[reg_num]
    
def sevenbitbin(abc):
    a=len(abc)
    return ("0"*(7-a) + abc)

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



f = open("input.txt")
w = open("output.txt","a")
nlines = len(f.readlines())
f.seek(0)

for i in range(nlines):
    query = f.readline().strip().split(" ")
    code = ""
    print(query)
    # Type A instruction
    if query[0]=="add":
        code += opcode["add"]
        code += "00"
        code += choose_register(query[1])
        code += choose_register(query[2])
        code += choose_register(query[3]) +"\n"
        w.write(code)


    elif query[0]=="sub":
        code += opcode["sub"]
        code += "00"
        code += choose_register(query[1])
        code += choose_register(query[2])
        code += choose_register(query[3]) +"\n"
        w.write(code)


    elif query[0]=="mul":
        code += opcode["mul"]
        code += "00"
        code += choose_register(query[1])
        code += choose_register(query[2])
        code += choose_register(query[3]) +"\n"
        w.write(code)
   

    elif query[0]=="xor":
        code += opcode["xor"]
        code += "00"
        code += choose_register(query[1])
        code += choose_register(query[2])
        code += choose_register(query[3]) +"\n"
        w.write(code)
 

    elif query[0]=="or":
        code += opcode["or"]
        code += "00"
        code += choose_register(query[1])
        code += choose_register(query[2])
        code += choose_register(query[3]) +"\n"
        w.write(code)
   

    elif query[0]=="and":
        code += opcode["and"]
        code += "00"
        code += choose_register(query[1])
        code += choose_register(query[2])
        code += choose_register(query[3]) +"\n"
        w.write(code)
   

    # Type B instruction
    elif ((query[0] == "mov") & (query[2][0]=="$")):  
        code+=opcode["mov"][0]
        code += "0"
        code+=choose_register(query[1])
        num = int(query[2][1:])
        code+=sevenbitbin(decimal_to_binary(num)) +"\n"
        w.write(code)
    elif query[0] == "rs":
        code+=opcode["rs"]
        code += "0"
        code += choose_register(query[1])
        num = int(query[2][1:])
        code += sevenbitbin(decimal_to_binary(num)) + "\n"
        w.write(code)
    elif query[0] == "ls":
        code+=opcode["ls"] 
        code += "0"
        code += choose_register(query[1])
        num = int(query[2][1:])
        code += sevenbitbin(decimal_to_binary(num)) + "\n"
        w.write(code)
#Type C instruction 
    elif((len(query)==3) & (query[0]=="mov" or query[0]=="div" or query[0]=="not" or query[0]=="cmp") & (query[2] in registers)):
        code+=opcode[query[0]][1] + "00000" + registers[query[1]] + registers[query[2]] +"\n"
        w.write(code)
