def decimal_to_binary(num):
    "This function takes integer number and returns a string of binary no converts from decimal"
    binary = ""
    while num != 0:
        binary += str(num % 2)
        num = num // 2
    binary = binary[::-1]  # reverses string
    return binary


def Find_addr(label, list1):
    "This function finds the address of a label used for jump statements"
    ss = ""
    for i in range(len(list1)):
        if label == list1[i][0]:
            b = decimal_to_binary(i)
            for j in range(7-len(b)):
                ss += "0"
            ss += b
            return ss


def choose_register(reg_num):
    "This function returns opcode of registers"
    return registers[reg_num]


def sevenbitbin(abc):
    a = len(abc)
    return ("0" * (7 - a) + abc)


var_add = {}
var_count = 0
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

f = open("input.txt")
w = open("output.txt", "a")
nlines = len(f.readlines())
f.seek(0)

sentence_list = f.read().split("\n")
List_of_words = [line.split() for line in sentence_list if line.split()[0] != "var"]
list2=[i[0] for i in List_of_words]
var_count=len(list2)
print(list2)

f.seek(0)

for i in range(nlines):
    query = f.readline().strip().split(" ")
    code = ""
    # Type A instruction
    if query[0] == "var":
        if len(query)==2:
            var_add[query[1]] = sevenbitbin(decimal_to_binary(var_count))
            var_count += 1
        else:
            w.write("Invalid Variable Declaration\n")
    elif query[0] == "add":
        if len(query)==4:
            if ((query[1] in registers) and (query[1] in registers) and (query[1] in registers)):
                code += opcode["add"]
                code += "00"
                if (query[1] == "FLAGS" or query[2] == "FLAGS" or query[3] == "FLAGS"):
                    w.write("illegal Use Of registers\n")
                    continue
                code += choose_register(query[1])
                code += choose_register(query[2])
                code += choose_register(query[3]) + "\n"
                w.write(code)
            else:
                w.write("illegal use of registers\n")
        else:
            w.write("Invalid Instruction\n")
    elif query[0] == "sub":
        if len(query)==4:
            if ((query[1] in registers) and (query[1] in registers) and (query[1] in registers)):
                code += opcode["sub"]
                code += "00"
                if (query[1] == "FLAGS" or query[2] == "FLAGS" or query[3] == "FLAGS"):
                    w.write("illegal Use Of registers\n")
                    continue
                code += choose_register(query[1])
                code += choose_register(query[2])
                code += choose_register(query[3]) + "\n"
                w.write(code)
            else:
                w.write("illegal use of registers\n")
        else:
            w.write("Invalid Instruction\n")

    elif query[0] == "mul":
        if len(query)==4:
            if ((query[1] in registers) and (query[1] in registers) and (query[1] in registers)):
                code += opcode["mul"]
                code += "00"
                if (query[1] == "FLAGS" or query[2] == "FLAGS" or query[3] == "FLAGS"):
                    w.write("illegal Use Of registers\n")
                    continue
                code += choose_register(query[1])
                code += choose_register(query[2])
                code += choose_register(query[3]) + "\n"
                w.write(code)
            else:
                w.write("illegal use of registers\n")
        else:
            w.write("Invalid Instruction\n")

    elif query[0] == "xor":
        if len(query)==4:
            if ((query[1] in registers) and (query[1] in registers) and (query[1] in registers)):
                code += opcode["xor"]
                code += "00"
                if (query[1] == "FLAGS" or query[2] == "FLAGS" or query[3] == "FLAGS"):
                    w.write("illegal Use Of registers\n")
                    continue
                code += choose_register(query[1])
                code += choose_register(query[2])
                code += choose_register(query[3]) + "\n"
                w.write(code)
            else:
                w.write("illegal use of registers\n")
        else:
            w.write("Invalid Instruction\n")

    elif query[0] == "or":
        if len(query)==4:
            if ((query[1] in registers) and (query[1] in registers) and (query[1] in registers)):
                code += opcode["or"]
                code += "00"
                if (query[1] == "FLAGS" or query[2] == "FLAGS" or query[3] == "FLAGS"):
                    w.write("illegal Use Of registers\n")
                    continue
                code += choose_register(query[1])
                code += choose_register(query[2])
                code += choose_register(query[3]) + "\n"
                w.write(code)
            else:
                w.write("illegal use of registers\n")

        else:
            w.write("Invalid Instruction\n")

    elif query[0] == "and":
        if len(query)==4:
            if ((query[1] in registers) and (query[1] in registers) and (query[1] in registers)):
                code += opcode["and"]
                code += "00"
                if (query[1] == "FLAGS" or query[2] == "FLAGS" or query[3] == "FLAGS"):
                    w.write("illegal Use Of registers\n")
                    continue
                code += choose_register(query[1])
                code += choose_register(query[2])
                code += choose_register(query[3]) + "\n"
                w.write(code)
            else:
                w.write("illegal use of registers\n")
        else:
            w.write("Invalid Instruction\n")

    # Type B instruction
    elif (query[0] == "mov"):
        if len(query)==3:
            if ((query[1] in registers)):
                if (query[2][0] == "$"):
                    code += opcode["mov"][0]
                    code += "0"
                    code += choose_register(query[1])
                    num = int(query[2][1:])
                    code += sevenbitbin(decimal_to_binary(num)) + "\n"
                    w.write(code)
                elif (query[2] in registers):
                    code += opcode[query[0]][1] + "00000" + \
                        registers[query[1]] + registers[query[2]] + "\n"
                    w.write(code)
                else:
                    w.write("invalid syntax use\n")
            else:
                w.write("illegal use of registers\n")
        else:
            w.write("Invalid Instruction\n")

    elif query[0] == "rs":
        if len(query)==3:
            if ((query[1] in registers)):
                code += opcode["rs"]
                code += "0"
                if (query[1] == "FLAGS" or query[2] == "FLAGS" ):
                    w.write("illegal Use Of registers\n")
                    continue
                code += choose_register(query[1])
                num = int(query[2][1:])
                code += sevenbitbin(decimal_to_binary(num)) + "\n"
                w.write(code)
            else:
                w.write("illegal use of registers\n")
        else:
            w.write("Invalid Instruction\n")

    elif query[0] == "ls":
        if len(query)==3:
            if ((query[1] in registers)):
                code += opcode["ls"]
                code += "0"
                if (query[1] == "FLAGS" or query[2] == "FLAGS"):
                    w.write("illegal Use Of registers\n")
                    continue
                code += choose_register(query[1])
                num = int(query[2][1:])
                code += sevenbitbin(decimal_to_binary(num)) + "\n"
                w.write(code)
            else:
                w.write("illegal use of registers\n")
        else:
            w.write("Invalid Instruction\n")

    # Type C instruction
    elif (query[0] == "div" or query[0] == "not" or query[0] == "cmp"):
        if len(query)==3:
            if ((query[1] in registers) and (query[2] in registers)):
                if (query[1] == "FLAGS" or query[2] == "FLAGS"):
                    w.write("illegal Use Of registers\n")
                    continue
                if (query[2] in registers):
                    code += opcode[query[0]] + "00000" + \
                        registers[query[1]] + registers[query[2]] + "\n"
                    w.write(code)
            else:
                w.write("illegal use of registers\n")
        else:
            w.write("Invalid Instruction\n")

    # type d instruction
    elif (query[0] == "ld" or query[0] == "st"):
        if len(query)==3:
            if ((query[1] in registers)):
                if (query[1] == "FLAGS" or (query[2] not in var_add)):
                    w.write("illegal Use Of registers or undeclared variables\n")
                    continue
                code += opcode[query[0]]+"0" + \
                    registers[query[1]]+var_add[query[2]]+"\n"
                w.write(code)
            else:
                w.write("illegal use of registers\n")
        else:
            w.write("Invalid Instruction\n")

    # Type E instruction

    elif query[0] == "jmp":
        if (len(query)==2) & (query[1]+":" in list2) :
            code += opcode["jmp"]
            code += "0000"
            code += Find_addr(query[1]+":", List_of_words) + "\n"
            w.write(code)
        else:
            w.write("Undeclared Label\n")

    elif query[0] == "jlt":
        if (len(query)==2) & (query[1]+":" in list2) :
            code += opcode["jlt"]
            code += "0000"
            code += Find_addr(query[1]+":", List_of_words) + "\n"
            w.write(code)
        else:
            w.write("Undeclared Label\n")

    elif query[0] == "jgt":
        if (len(query)==2) & (query[1]+":" in list2) :
            code += opcode["jgt"]
            code += "0000"
            code += Find_addr(query[1]+":", List_of_words) + "\n"
            w.write(code)
        else:
            w.write("Undeclared Label\n")

    elif query[0] == "je":
        if (len(query)==2) & (query[1]+":" in list2) :
            code += opcode["je"]
            code += "0000"
            code += Find_addr(query[1]+":", List_of_words) + "\n"
            w.write(code)
        else:
            w.write("Undeclared Label\n")


    # Type F instruction
    elif (len(query) == 1):
        if query[0] == "hlt":
            code += opcode["hlt"]
            code += "0"*11 + "\n"
            w.write(code)


    elif (len(query) == 2):
        if (query[1] == "hlt"):
            code += opcode["hlt"]
            code += "0"*11 + "\n"
            w.write(code)
    else:
        w.write("Invalid Syntax\n")
