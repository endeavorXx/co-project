# Note - writing assembly
#        <label-name>:              <always use a semi-colon just after labelname>
#  add next instructions in next line afterwards

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
        w.write(f"Error at line number : {line_num}..\.. Misuse of labels as variables\n")
        print("Misuse of labels as variables")

    for i in range(len(list1)):
        if label == list1[i][0]:
            islabel = 1
            b = decimal_to_binary(i)
            ss += sevenbitbin(b)
            return ss
        
    if islabel == 0:
        print(f"Error at line number : {line_num}..\.. undeclared label type : {label}")


def sevenbitbin(abc):
    a = len(abc)
    return ("0" * (7 - a) + abc)

var_add={}
var_count=0

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
w = open("output.txt", "w")
nlines = len(f.readlines())
f.seek(0)

sentence_list = f.read().strip().split("\n")

# It removes blank lines in between the program
for line in sentence_list:
    if line == "":
        sentence_list.remove(line)

List_of_words = [line.split() for line in sentence_list if line.split()[0]!="var"]

f.seek(0)

ishalt = 0
lasthalt = 0

flagreg = "0"*12 + "0000"  #last 4 bits are indicator of V L G E

if nlines>128:
    w.write("More no of instructions than expected")        # assembler can handle only 128 lines of instruction
    print("More no of instructions than expected")

for i in range(nlines):
    query = f.readline().strip().split(" ")
    if query == ['']:
        continue
    
    if i==nlines-1:
        length = len(query)
        if length==1:
            if (query[0]=="hlt"):
                lasthalt = 1
        elif length==2:
            if (query[1]=="hlt"):
                lasthalt = 1

    code = ""

    # Type A instruction
    print(query)
    if query[0] == "var":

        if (i>var_count):
            w.write(f"at line number {i} variable must be declared at the beginning\n")
            print("variable must be declared at the beginning")
        var_add[query[1]] = sevenbitbin(decimal_to_binary(var_count))
        var_count += 1  

    elif query[0] == "add":
        code += opcode["add"]
        code += "00"
        try:
            if ((query[1] or query[2] or query[3]) not in (registers)):
                w.write(f"wrong register name declared at line number {i}\n")
                print("wrong register name")

            if (query[3]=="FLAGS"):
                w.write(f"Error at line number {i} Illegal use of Flag register\n")
            
            code += registers[query[1]]
            code += registers[query[2]]
            code += registers[query[3]] + "\n"
            w.write(code)
        except:
            w.write(f"General Synatx Error at line number {i}\n")

    elif query[0] == "sub":
        code += opcode["sub"]
        code += "00"
        try:
            if ((query[1] or query[2] or query[3]) not in (registers)):
                w.write(f"wrong register name declared at line number {i}\n")
                print("wrong register name")

            if (query[3]=="FLAGS"):
                w.write(f"Error at line number {i} Illegal use of Flag register\n")
            
            code += registers[query[1]]
            code += registers[query[2]]
            code += registers[query[3]] + "\n"
            w.write(code)
        except:
            w.write(f"General Synatx Error at line number {i}\n")

    elif query[0] == "mul":
        code += opcode["mul"]
        code += "00"
        try:
            if ((query[1] or query[2] or query[3]) not in (registers)):
                w.write(f"wrong register name declared at line number {i}\n")
                print("wrong register name")
            
            if (query[3]=="FLAGS"):
                w.write(f"Error at line number {i} Illegal use of Flag register\n")
            
            code += registers[query[1]]
            code += registers[query[2]]
            code += registers[query[3]] + "\n"
            w.write(code)
        except:
            w.write(f"General Synatx Error at line number {i}\n")

    elif query[0] == "xor":
        code += opcode["xor"]
        code += "00"
        try:
            if ((query[1] or query[2] or query[3]) not in (registers)):
                w.write(f"wrong register name declared at line number {i}\n")
                print("wrong register name")
            
            if (query[3]=="FLAGS"):
                w.write(f"Error at line number {i} Illegal use of Flag register\n")
            
            code += registers[query[1]]
            code += registers[query[2]]
            code += registers[query[3]] + "\n"
            w.write(code)
        except:
            w.write(f"General Synatx Error at line number {i}\n")

    elif query[0] == "or":
        code += opcode["or"]
        code += "00"
        try:
            if (query[1] or query[2] or query[3]) not in (registers):
                w.write(f"wrong register name declared at line number {i}\n")
                print("wrong register name")
            
            if (query[3]=="FLAGS"):
                w.write(f"Error at line number {i} Illegal use of Flag register\n")
            
            code += registers[query[1]]
            code += registers[query[2]]
            code += registers[query[3]] + "\n"
            w.write(code)
        except:
            w.write(f"General Synatx Error at line number {i}\n")

    elif query[0] == "and":
        code += opcode["and"]
        code += "00"
        try:
            if (query[1] or query[2] or query[3]) not in (registers):
                w.write(f"wrong register name declared at line number {i}\n")
                print("wrong register name")
            
            if (query[3]=="FLAGS"):
                w.write(f"Error at line number {i} Illegal use of Flag register\n")
            
            code += registers[query[1]]
            code += registers[query[2]]
            code += registers[query[3]] + "\n"
            w.write(code)
        except:
            w.write(f"General Synatx Error at line number {i}\n")

    # Type B instruction
    elif (query[0] == "mov"):
        try:
            if (query[2][0] == "$"):
                code += opcode["mov"][0]
                code += "0"
                
                if (query[1] not in registers):
                    w.write(f"wrong register name declared at line number {i}\n")
                    print("wrong register name")
                
                code += registers[query[1]]
                num = int(query[2][1:])        
                
                if (num>=0 and num<=127):
                    code += sevenbitbin(decimal_to_binary(num)) + "\n"
                else:
                    w.write("value error!! Imm have range: [0,127]\n")
                    print("value error!! Imm have range: [0,127]")        
            else:
                if (query[1] or query[2]) not in registers:
                    w.write(f"wrong register name declared at line number {i}\n")
                    print("wrong register name")
                else:
                    code +=opcode[query[0]][1] + "00000" + registers[query[1]] + registers[query[2]] + "\n"
            w.write(code)
        except:
            w.write(f"General Synatx Error at line number {i}\n")

    elif query[0] == "rs":
        code += opcode["rs"]
        code += "0"
        try:
            if query[1] not in registers:
                w.write(f"wrong register name declared at line number {i}\n")
                print("wrong register name")

            if query[1] == "FLAGS":
                w.write(f"Error at line number {i} Illegal use of Flag register\n")

            code += registers[query[1]]
            num = int(query[2][1:])

            if (num>=0 and num<=127):
                code += sevenbitbin(decimal_to_binary(num)) + "\n"

            else:
                w.write("value error!! Imm have range: [0,127]\n")
                print("value error!! Imm have range: [0,127]")
            w.write(code)

        except:
            w.write(f"General Synatx Error at line number {i}\n")

    elif query[0] == "ls":
        code += opcode["ls"]
        code += "0"
        try:
            if query[1] not in registers:
                w.write(f"wrong register name at line number {i}\n")
                print("wrong register name")
            
            if query[1] == "FLAGS":
                w.write(f"Error at line number {i} Illegal use of Flag register\n")
            
            code += registers[query[1]]
            num = int(query[2][1:])
            
            if (num>=0 and num<=127):
                code += sevenbitbin(decimal_to_binary(num)) + "\n"
            else:
                w.write(f"value error!! Imm have range: [0,127] at line number {i}\n")
                print("value error!! Imm have range: [0,127]")
                exit()
            w.write(code)
        except:
            w.write(f"General Synatx Error at line number {i}\n")

    # Type C instruction

    elif ((len(query) == 3) & (query[0] == "div" or query[0] == "not" or query[0] == "cmp") ):
        try:
            if(query[1] and query[2]) in (registers):
                code += opcode[query[0]] + "00000" + registers[query[1]] + registers[query[2]] + "\n"
                w.write(code)
            else:
                w.write(f"wrong register name at line number {i}\n")
                print("wrong register name")
        except:
            w.write(f"General Synatx Error at line number {i}\n")

    # Type D instruction

    elif (query[0]=="ld") or (query[0]=="st"):
        try:
            if query[1] not in registers:
                w.write(f"wrong register name at line number {i}\n")
                print("wrong register name")
            
            if query[2] not in var_add:
                w.write(f"at line number {i}, undeclared variable type :{query[2]}\n")
                print(f"undeclared variable type :{query[2]}")
            
            code+=opcode[query[0]]+"0"+ registers[query[1]]+var_add[query[2]]+"\n"
            w.write(code)
        except:
            w.write(f"General Synatx Error at line number {i}\n")

    # Type E instruction

    elif query[0] == "jmp":
        code += opcode["jmp"]
        code += "0000"
        try:
            code += Find_addr(query[1]+":", List_of_words, i) + "\n"
            w.write(code)
        except:
            w.write(f"General Synatx Error at line number {i}\n")

    elif query[0] == "jlt":
        code += opcode["jlt"]
        code += "0000"
        try:
            code +=Find_addr(query[1]+":", List_of_words, i) + "\n"
            w.write(code)
        except:
            w.write(f"General Synatx Error at line number {i}\n")

    elif query[0] == "jgt":
        code += opcode["jgt"]
        code += "0000"
        try:
            code +=Find_addr(query[1]+":", List_of_words, i) + "\n"
            w.write(code)
        except:
            w.write(f"General Synatx Error at line number {i}\n")

    elif query[0] == "je":
        code += opcode["je"]
        code += "0000"
        try:
            code +=Find_addr(query[1]+":", List_of_words, i) + "\n"
            w.write(code)
        except:
            w.write(f"General Synatx Error at line number {i}\n")

    # Type F instruction
    elif (len(query)==1):
        try:
            if query[0] == "hlt":
                ishalt = 1
                code += opcode["hlt"]
                code += "0"*11 + "\n"
                w.write(code)
        except:
            w.write(f"General Synatx Error at line number {i}\n")

    elif(len(query)==2):
        try:
            Find_addr(query[0],List_of_words,i)         # checks whether a correct label is used or not by checking address 
            if(query[1]=="hlt"):
                ishalt = 1
                code += opcode["hlt"]
                code += "0"*11 + "\n"
                w.write(code)
        except:
            w.write(f"General Synatx Error at line number {i}\n")

    else:
        w.write(f"Error at line number {i}..\..wrong instruction name\n")
        print(f"Error at line number {i}..\..wrong instruction name ")


if ishalt==0:
    print("Missing hlt instruction")
    w.write("Missing hlt instruction\n")
if lasthalt==0:
    print("Last instruction not hlt type")
    w.write("Last instruction not hlt type")