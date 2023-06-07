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

def binary_to_decimal(bin):
    n = len(bin) - 1
    num = 0
    for i in bin:
        num += int(i)*(2**n)
        n = n-1
    return num

def decimal_to_binary3(num):
    binary = ""
    while num != 0:
        binary += str(num % 2)
        num = num // 2
    binary = binary[::-1]
    return (3-len(binary))*"0"+binary

def decimal_to_binary1(num):
    binary = ""
    while num != 0:
        binary += str(num % 2)
        num = num // 2
    binary = binary[::-1]
    return binary

def float_to_decimal(a):
    b=a[3:]
    c="1."+b
    e=binary_to_decimal(a[:3])
    cc=e-4
    if cc>0:
        f=str(float(c)(10*(e-3)))
    else:
        f="0."+"0"*(-1*cc)+"1"+c.split(".")[1]
    count=0
    g=f.split(".")
    
    count+=binary_to_decimal(g[0])
    expo=-1
    for i in range (0,len(g[1])):
        if(int(g[1][i])==1):
            count+=2**(expo)
            expo-=1
        else:
            expo-=1
            continue
            
    return count

def decimal_to_float(a):
    aa=""
    b=""
    c=a%1 #remainder
    d=a//1 #whole no.
  
    e=0
    while(e!=5):
        if c*2>=1:
            b+="1"
            c=c*2-1
        else:
            b+="0"
            c=c*2
        e+=1
    aa=decimal_to_binary1(int(d))
    pos=aa+"."+b
    expo=0
    pos=str(round(float(pos),5))
    if float(pos)>1:
        while(float(pos)>2):
            nn=pos.split(".")
            pos=nn[0][0:-1]+"."+nn[0][-1]+nn[1]
            expo+=1
        return decimal_to_binary(expo+3) + (pos.split(".")[0]+"." + pos.split(".")[1][0:5] +"0"*(5-len(pos.split(".")[1]))).split(".")[1]
    else:
        pos=str(round(float(pos),5))
        while(float(pos)<1):
            pos=str(round(float(pos)*10,5))
            expo-=1
            
        nn=pos.split(".")
        pos = pos + "0"*(5-len(nn[1]))
        sx=pos.split(".")
        ans=decimal_to_binary(expo+3) + sx[1]
        
        return ans

def Find_addr(label, list1, line_num):
    "This function finds the address of a label used for jump statements"
    ss = ""
    islabel = 0                     # label should not be a variable
    if (label in var_add):
        print(f"Error at line number : {line_num+1}..\.. Misuse of labels as variables")
            
    for i in range(len(list1)):
        if label == list1[i][0]:
            islabel = 1
            b = decimal_to_binary(i)
            ss += sevenbitbin(b)

    if islabel == 0:
        print(f"Error at line number : {line_num+1}..\.. undeclared label type : {label}")       
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
    "hlt": "11010",
    "addf": "10000",
    "subf": "10001",
    "movf": "10010",
    "bs": "10110",
    "bc": "10111",
    "clz": "11000",
    "clo": "11001",
    "bt": "10101"
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
# f = open("input.txt")
# l = f.readlines()

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
            print(f"Error at line number {i+1} variable must be declared at the beginning")
        var_add[query[1]] = sevenbitbin(decimal_to_binary(var_num))
        var_num += 1
        var_count += 1

    elif query[0] == "add":
        code += opcode["add"]
        code += "00"
        try:
            if ((query[1] or query[2] or query[3]) not in (registers)):
                error_code = 1
                print(f"Error at line number {i+1} wrong register name")

            if (query[3] == "FLAGS"):
                error_code = 1
                print(f"Error at line number {i+1} Illegal use of Flag register")
                    
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
                print(f"Error at line number {i+1} wrong register name")

            if (query[3] == "FLAGS"):
                error_code = 1
                print(f"Error at line number {i+1} Illegal use of Flag register")
                    
            code += registers[query[1]]
            code += registers[query[2]]
            code += registers[query[3]]
            print(code)
        except:
            error_code = 1
            print(f"General Syntax Error at line number {i+1}")

    elif query[0] == "mul":
        code += opcode["mul"]
        code += "00"
        try:
            if ((query[1] or query[2] or query[3]) not in (registers)):
                error_code = 1
                print(f"Error at line nummber {i+1} wrong register name")

            if (query[3] == "FLAGS"):
                error_code = 1
                print(f"Error at line number {i+1} Illegal use of Flag register")
                  
            code += registers[query[1]]
            code += registers[query[2]]
            code += registers[query[3]]
            print(code)
        except:
            error_code = 1
            print(f"General Syntax Error at line number {i+1}")

    elif query[0] == "xor":
        code += opcode["xor"]
        code += "00"
        try:
            if ((query[1] or query[2] or query[3]) not in (registers)):
                error_code = 1
                print("wrong register name")

            if (query[3] == "FLAGS"):
                error_code = 1
                print(f"Error at line number {i+1} Illegal use of Flag register")

            code += registers[query[1]]
            code += registers[query[2]]
            code += registers[query[3]]
            print(code)
        except:
            error_code = 1
            print(f"General Syntax Error at line number {i+1}")

    elif query[0] == "or":
        code += opcode["or"]
        code += "00"
        try:
            if (query[1] or query[2] or query[3]) not in (registers):
                error_code = 1
                print(f"Error at line number {i+1} wrong register name")

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
            print(f"General Syntax Error at line number {i+1}")

    elif query[0] == "addf":
        code += opcode["addf"]
        code += "00"
        try:
            if ((query[1] or query[2] or query[3]) not in (registers)):
                error_code = 1
                print(f"Error at line number {i+1} wrong register name")

            if (query[3] == "FLAGS"):
                error_code = 1
                print(f"Error at line number {i+1} Illegal use of Flag register")
                    
            code += registers[query[1]]
            code += registers[query[2]]
            code += registers[query[3]]
            print(code)
        except:
            error_code = 1
            print(f"General Syntax Error at line number {i+1}")

    elif query[0] == "subf":
        code += opcode["subf"]
        code += "00"
        try:
            if ((query[1] or query[2] or query[3]) not in (registers)):
                error_code = 1
                print(f"Error at line number {i+1} wrong register name")

            if (query[3] == "FLAGS"):
                error_code = 1
                print(f"Error at line number {i+1} Illegal use of Flag register")
                    
            code += registers[query[1]]
            code += registers[query[2]]
            code += registers[query[3]]
            print(code)
        except:
            error_code = 1
            print(f"General Syntax Error at line number {i+1}")

    # Type B instruction
    elif (query[0] == "mov"):
        try:
            if (query[2][0] == "$"):
                code += opcode["mov"][0]
                code += "0"

                if (query[1] not in registers):
                    error_code = 1
                    print(f"wrong register name declared at line number {i+1}")
                    
                code += registers[query[1]]
                num = int(query[2][1:])

                if (num >= 0 and num <= 127):
                    code += sevenbitbin(decimal_to_binary(num))
                else:
                    error_code = 1
                    print(f"Error at line number {i+1} value error!! Imm have range: [0,127]")
            else:
                if (query[1] or query[2]) not in registers:
                    error_code = 1
                    print(f"wrong register name declared at line number {i+1}")                       
                else:
                    code += opcode[query[0]][1] + "00000" + \
                        registers[query[1]] + registers[query[2]]
            print(code)
        except:
            error_code = 1
            print(f"General Syntax Error at line number {i+1}")
    
    elif (query[0] == "movf"):
        # try:
            if (query[2][0] == "$"):
                if (query[1] not in registers):
                    error_code = 1
                    print(f"wrong register name declared at line number {i+1}")
                    
                code += opcode["movf"]
                code += "0"
                code += registers[query[1]]
                flt = query[2][1:]
                flt = decimal_to_float(float(flt))
                if len(flt)<=8:
                    code += flt
                else:
                    error_code = 1
                    print(f"Error at line number {i+1} value error!! Imm value not valid floating point")
                print(code)
        # except:
        #     error_code = 1
        #     print(f"General Syntax Error at line number {i+1}")

    elif query[0] == "rs":
        code += opcode["rs"]
        code += "0"
        try:
            if query[1] not in registers:
                error_code = 1
                print(f"wrong register name declared at line number {i+1}")

            if query[1] == "FLAGS":
                error_code = 1
                print(f"Error at line number {i+1} Illegal use of Flag register")                    
            code += registers[query[1]]
            num = int(query[2][1:])

            if (num >= 0 and num <= 127):
                code += sevenbitbin(decimal_to_binary(num))

            else:
                error_code = 1
                print("Error at line number {i+1} value error!! Imm have range: [0,127]")

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
                print(f"Error at line number {i+1} Illegal use of Flag register")
                    
            code += registers[query[1]]
            num = int(query[2][1:])

            if (num >= 0 and num <= 127):
                code += sevenbitbin(decimal_to_binary(num))
            else:
                error_code = 1
                print(f"value error!! Imm have range: [0,127] at line number {i}")                    
            print(code)
        except:
            error_code = 1
            print(f"General Syntax Error at line number {i+1}")

    elif query[0] == "bs":
        code += opcode["bs"]
        code += "0"
        try:
            if query[1] not in registers:
                error_code = 1
                print(f"wrong register name at line number {i+1}")

            if query[1] == "FLAGS":
                error_code = 1
                print(f"Error at line number {i+1} Illegal use of Flag register")

            code += registers[query[1]]
            imm = int(query[2][1:])
            if (imm>=1 and imm<=16):  
                code += sevenbitbin(decimal_to_binary(imm))
            else:
                print(f"Error at line number {i+1} Imm have range:[1,16]")
            print(code)
        except:
            print(f"General syntax error at line number {i+1}")       

    elif query[0] == "bc":
        code += opcode["bc"]
        code += "0"
        try:
            if query[1] not in registers:
                error_code = 1
                print(f"wrong register name at line number {i+1}")

            if query[1] == "FLAGS":
                error_code = 1
                print(f"Error at line number {i+1} Illegal use of Flag register")

            code += registers[query[1]]
            imm = int(query[2][1:])
            if (imm>=1 and imm<=16):  
                code += sevenbitbin(decimal_to_binary(imm))
            else:
                print(f"Error at line number {i+1} Imm have range:[1,16]")
            print(code)
        except:
            print(f"General syntax error at line number {i+1}")    

    elif query[0] == "bt":
        code += opcode["bt"]
        code += "0"
        try:
            if query[1] not in registers:
                error_code = 1
                print(f"wrong register name at line number {i+1}")

            if query[1] == "FLAGS":
                error_code = 1
                print(f"Error at line number {i+1} Illegal use of Flag register")

            code += registers[query[1]]
            imm = int(query[2][1:])
            if (imm>=1 and imm<=16):  
                code += sevenbitbin(decimal_to_binary(imm))
            else:
                print(f"Error at line number {i+1} Imm have range:[1,16]")
            print(code)
        except:
            print(f"General syntax error at line number {i+1}")    
    # Type C instruction

    elif (query[0] == "div" or query[0] == "not" or query[0] == "cmp" or query[0] == "clz" or query[0] == "clo"):
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
                    print(f"Error at line number {i+1} wrong register name")
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
            print(f"General Syntax Error at line number {i+1}")

    elif query[0] == "jlt":
        code += opcode["jlt"]
        code += "0000"
        try:
            code += Find_addr(query[1]+":", List_of_words, i)
            print(code)
        except:
            error_code = 1
            print(f"General Syntax Error at line number {i+1}")

    elif query[0] == "jgt":
        code += opcode["jgt"]
        code += "0000"
        try:
            code += Find_addr(query[1]+":", List_of_words, i)
            print(code)
        except:
            error_code = 1
            print(f"General Syntax Error at line number {i+1}")

    elif query[0] == "je":
        code += opcode["je"]
        code += "0000"
        try:
            code += Find_addr(query[1]+":", List_of_words, i)
            print(code)
        except:
            error_code = 1
            print(f"General Syntax Error at line number {i+1}")

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

# f.close()
