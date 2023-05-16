# Note - writing assembly
#        <label-name>:              <always use a semi-colon just after labelname>
import sys


def decimal_to_binary(num):
    "This function takes integer number and returns a string of binary no converts from decimal"
    binary = ""
    while num != 0:
        binary += str(num % 2)
        num = num // 2
    binary = binary[::-1]  # reverses string
    return binary


def Find_addr(label, list1, line_num):
    "This function finds the address of a label used for jump statements"
    ss = ""
    islabel = 0                     # label should not be a variable
    if (label in var_add):
        print(
            f"Error at line number : {line_num+1}..\.. Misuse of labels as variables")
        print("Misuse of labels as variables")

    for i in range(len(list1)):
        if label == list1[i][0]:
            islabel = 1
            b = decimal_to_binary(i)
            ss += sevenbitbin(b)

    if islabel == 0:
        print(
            f"Error at line number : {line_num+1}..\.. undeclared label type : {label}")
    else:
        return ss


def sevenbitbin(abc):
    a = len(abc)
    return ("0" * (7 - a) + abc)


var_add = {}
var_count = 0

labels = {}

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

l = []
for i in sys.stdin:
    l.append(i)
nlines = len(l)
sentence_list = l

# It removes blank lines in between the program
length = len(sentence_list)
cpy = sentence_list.copy()
for i in range(length):
    if cpy[i] == "":
        sentence_list.remove(cpy[i])

List_of_words = [line.split()
                 for line in sentence_list if line.split()[0] != "var"]
var_num = 0
for line in sentence_list:
    if line.split()[0] != "var":
        var_num += 1


ishalt = 0
lasthalt = 0
error_code = 0

flagreg = "0"*12 + "0000"  # last 4 bits are indicator of V L G E

if nlines > 128:
    # assembler can handle only 128 lines of instruction
    error_code = 1
    print("More no of instructions than expected")
    print("More no of instructions than expected")

void_lines = 0
for i in range(nlines):
    query = sentence_list[i].split()

    # statement - label1: mov R1 R2 should be executed
    if query[0].endswith(":"):
        labels[query[0]] = sevenbitbin(
            decimal_to_binary(i-var_count-void_lines))
        query.remove(query[0])

    if query == ['']:
        void_lines += 1
        continue

    if i == nlines-1:
        length = len(query)
        if length == 1:
            if (query[0] == "hlt"):
                lasthalt = 1
        elif length == 2:
            if (query[1] == "hlt"):
                lasthalt = 1

    code = ""

    # Type A instruction
    if query[0] == "var":

        if (i > var_count):
            error_code = 1
            print("variable must be declared at the beginning")
        var_add[query[1]] = sevenbitbin(decimal_to_binary(var_num))
        var_num += 1
        var_count += 1

    elif query[0] == "add":
        code += opcode["add"]
        code += "00"
        try:
            if ((query[1] or query[2] or query[3]) not in (registers)):
                error_code = 1
                print("wrong register name")

            if (query[3] == "FLAGS"):
                error_code = 1
                print(
                    f"Error at line number {i+1} Illegal use of Flag register")

            code += registers[query[1]]
            code += registers[query[2]]
            code += registers[query[3]]
            print(code)
        except:
            error_code = 1
            print(f"General Syntax Error at line number {i+1}")

    elif query[0] == "sub":
        code += opcode["sub"]
        code += "00"
        try:
            if ((query[1] or query[2] or query[3]) not in (registers)):
                error_code = 1
                print("wrong register name")

            if (query[3] == "FLAGS"):
                error_code = 1
                print(
                    f"Error at line number {i+1} Illegal use of Flag register")

            code += registers[query[1]]
            code += registers[query[2]]
            code += registers[query[3]]
            print(code)
        except:
            error_code = 1
            print(f"General Synatx Error at line number {i+1}")

    elif query[0] == "mul":
        code += opcode["mul"]
        code += "00"
        try:
            if ((query[1] or query[2] or query[3]) not in (registers)):
                error_code = 1
                print("wrong register name")

            if (query[3] == "FLAGS"):
                error_code = 1
                print(
                    f"Error at line number {i+1} Illegal use of Flag register")

            code += registers[query[1]]
            code += registers[query[2]]
            code += registers[query[3]]
            print(code)
        except:
            error_code = 1
            print(f"General Synatx Error at line number {i+1}")

    elif query[0] == "xor":
        code += opcode["xor"]
        code += "00"
        try:
            if ((query[1] or query[2] or query[3]) not in (registers)):
                error_code = 1
                print("wrong register name")

            if (query[3] == "FLAGS"):
                error_code = 1
                print(
                    f"Error at line number {i+1} Illegal use of Flag register")

            code += registers[query[1]]
            code += registers[query[2]]
            code += registers[query[3]]
            print(code)
        except:
            error_code = 1
            print(f"General Synatx Error at line number {i+1}")

    elif query[0] == "or":
        code += opcode["or"]
        code += "00"
        try:
            if (query[1] or query[2] or query[3]) not in (registers):
                error_code = 1
                print("wrong register name")

            if (query[3] == "FLAGS"):
                error_code = 1
                print(
                    f"Error at line number {i+1} Illegal use of Flag register")

            code += registers[query[1]]
            code += registers[query[2]]
            code += registers[query[3]]
        except:
            error_code = 1
            print(f"General Syntax Error at line number {i+1}")

    elif query[0] == "and":
        code += opcode["and"]
        code += "00"
        try:
            if (query[1] or query[2] or query[3]) not in (registers):
                error_code = 1
                print(f"wrong register name declared at line number {i+1}")

            if (query[3] == "FLAGS"):
                error_code = 1
                print(
                    f"Error at line number {i+1} Illegal use of Flag register")

            code += registers[query[1]]
            code += registers[query[2]]
            code += registers[query[3]]
            print(code)
        except:
            error_code = 1
            print(f"General Synatx Error at line number {i+1}")

    # Type B instruction
    elif (query[0] == "mov"):
        try:
            if (query[2][0] == "$"):
                code += opcode["mov"][0]
                code += "0"

                if (query[1] not in registers):
                    error_code = 1
                    print(
                        f"wrong register name declared at line number {i+1}")
                    print("wrong register name")

                code += registers[query[1]]
                num = int(query[2][1:])

                if (num >= 0 and num <= 127):
                    code += sevenbitbin(decimal_to_binary(num))
                else:
                    error_code = 1
                    print("value error!! Imm have range: [0,127]")
                    print("value error!! Imm have range: [0,127]")
            else:
                if (query[1] or query[2]) not in registers:
                    error_code = 1
                    print(
                        f"wrong register name declared at line number {i+1}")
                else:
                    code += opcode[query[0]][1] + "00000" + \
                        registers[query[1]] + registers[query[2]]
            print(code)
        except:
            error_code = 1
            print(f"General Syntax Error at line number {i+1}")

    elif query[0] == "rs":
        code += opcode["rs"]
        code += "0"
        try:
            if query[1] not in registers:
                error_code = 1
                print(f"wrong register name declared at line number {i+1}")

            if query[1] == "FLAGS":
                error_code = 1
                print(
                    f"Error at line number {i+1} Illegal use of Flag register")

            code += registers[query[1]]
            num = int(query[2][1:])

            if (num >= 0 and num <= 127):
                code += sevenbitbin(decimal_to_binary(num))

            else:
                error_code = 1
                print("value error!! Imm have range: [0,127]")

            print(code)

        except:
            error_code = 1
            print(f"General Syntax Error at line number {i+1}")

    elif query[0] == "ls":
        code += opcode["ls"]
        code += "0"
        try:
            if query[1] not in registers:
                error_code = 1
                print(f"wrong register name at line number {i+1}")

            if query[1] == "FLAGS":
                error_code = 1
                print(
                    f"Error at line number {i+1} Illegal use of Flag register")

            code += registers[query[1]]
            num = int(query[2][1:])

            if (num >= 0 and num <= 127):
                code += sevenbitbin(decimal_to_binary(num))
            else:
                error_code = 1
                print(
                    f"value error!! Imm have range: [0,127] at line number {i}")
                exit()
            print(code)
        except:
            error_code = 1
            print(f"General Syntax Error at line number {i+1}")

    # Type C instruction

    elif (query[0] == "div" or query[0] == "not" or query[0] == "cmp"):
        try:
            if (len(query) != 3):
                error_code = 1
                print(
                    f"Error at line number {i+1} can't compare more than 2 registers")
                continue
            if (len(query) == 3):
                if (query[1] and query[2]) in (registers):
                    code += opcode[query[0]] + "00000" + \
                        registers[query[1]] + registers[query[2]]
                    print(code)
                else:
                    error_code = 1
                    print("wrong register name")
        except:
            error_code = 1
            print(f"General Syntax Error at line number {i+1}")

    # Type D instruction

    elif (query[0] == "ld") or (query[0] == "st"):
        try:
            if query[1] not in registers:
                error_code = 1
                print("wrong register name")

            if query[2] not in var_add:
                error_code = 1
                print(f"undeclared variable type :{query[2]}")
                continue

            code += opcode[query[0]]+"0" + \
                registers[query[1]]+var_add[query[2]]
            print(code)
        except:
            error_code = 1
            print(f"General Syntax Error at line number {i+1}")

    # Type E instruction

    elif query[0] == "jmp":
        code += opcode["jmp"]
        code += "0000"
        try:
            code += Find_addr(query[1]+":", List_of_words, i)
            print(code)
        except:
            error_code = 1
            print(f"General Synatx Error at line number {i+1}")

    elif query[0] == "jlt":
        code += opcode["jlt"]
        code += "0000"
        try:
            code += Find_addr(query[1]+":", List_of_words, i)
            print(code)
        except:
            error_code = 1
            print(f"General Synatx Error at line number {i+1}")

    elif query[0] == "jgt":
        code += opcode["jgt"]
        code += "0000"
        try:
            code += Find_addr(query[1]+":", List_of_words, i)
            print(code)
        except:
            error_code = 1
            print(f"General Synatx Error at line number {i+1}")

    elif query[0] == "je":
        code += opcode["je"]
        code += "0000"
        try:
            code += Find_addr(query[1]+":", List_of_words, i)
            print(code)
        except:
            error_code = 1
            print(f"General Synatx Error at line number {i+1}")

    # Type F instruction

    elif (query[0] == "hlt" or (len(query) == 2 and query[1] == "hlt")):
        ishalt = 1
        try:
            if query[0] == "hlt":
                code += opcode["hlt"]
                code += "0"*11
                print(code)
            elif query[1] == "hlt":
                # checks whether a correct label is used or not by checking address
                Find_addr(query[0], List_of_words, i)
                code += opcode["hlt"]
                code += "0"*11
                print(code)
        except:
            error_code = 1
            print(f"General Syntax error at line number {i+1}")

    else:
        error_code = 1

        print(f"Error at line number {i+1} wrong instruction name ")


if ishalt == 0:
    error_code = 1
    print("Missing hlt instruction")

if lasthalt == 0:
    error_code = 1
    print("Last instruction not hlt type")
