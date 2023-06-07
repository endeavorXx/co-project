# Note - ISA only supports whole  number arithematic
import sys
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

def decimal_to_binary(num):
    "This function takes integer number and returns a string of binary no converts from decimal"
    binary = ""
    while num != 0:
        binary += str(num % 2)
        num = num // 2
    binary = binary[::-1]  # reverses string
    return binary

def print_reg():
    for reg in reg_file:
        print(" "+reg_file[reg],end="")
    print()

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
    if int(a) == 0:
        return 0
    a = a[8:]
    # print(a)
    b = a[3:]
    c = "1." + b
    cc = binary_to_decimal(a[:3])
    
    if cc > 0:
        f = str(float(c) * (10 ** (cc - 3)))
    elif cc == 0:
        f = c
    else:
        f = "0." + "0" * (-1 * cc) + "1" + c.split(".")[1]
    
    count = 0
    g = f.split(".")
    count += binary_to_decimal(g[0])
    expo = -1
    
    for i in range(0, len(g[1])):
        if int(g[1][i]) == 1:
            count += 2 ** expo
        expo -= 1
    
    return round(count,3)

def decimal_to_float(a):
    if a == 0:
        return "0"*8
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
        ans=decimal_to_binary3(expo+3) + (pos.split(".")[1] + "0"*(5-len(pos.split(".")[1])))[0:5]
        return ans
    else:
        pos=str(round(float(pos),5))

        while(float(pos)<1):
            pos=str(round(float(pos)*10,5))
            expo-=1
        
        nn=pos.split(".")
        pos = pos + "0"*(5-len(nn[1]))
        sx=pos.split(".")
        ans=decimal_to_binary3(expo+3) + sx[1][0:5]
        
        return ans
    
def sixteen_bit_binary(text):
    text = "0"*9 + text
    return text

def sixteen_bit_binaryf(text):
    text = "0"*8 + text
    return text

var_add={}

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
    "movf": "10010"
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

# f = open("output.txt")
# mem = f.readlines()

mem = []
for i in sys.stdin:
    mem.append(i + "\n")

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

# count = 0
temp_flag = "0"*16
while True:

    ## Execution_engine
    query = mem[binary_to_decimal(pc)].strip()              

    opcode = query[0:5]
    reg_file["FLAGS"] = "0"*16
    print(f"{pc}       ",end="")
    # Type A
    if opcode == "00000":

        temp_2 = binary_to_decimal(reg_file[registers[query[10:13]]])
        temp_3 = binary_to_decimal(reg_file[registers[query[13:16]]])
        if (temp_2+temp_3 >= 2**16):
            reg_file["FLAGS"] = reg_file["FLAGS"][:12] + "1" + reg_file["FLAGS"][13:]
            reg_file["R1"] = "0"*16
        else:
            reg_file[registers[query[7:10]]] = sixteen_bit_binary(decimal_to_7binary(temp_2+temp_3))

    if opcode == "00001":
        temp_2 = binary_to_decimal(reg_file[registers[query[10:13]]])
        temp_3 = binary_to_decimal(reg_file[registers[query[13:16]]])
        if (temp_3>temp_2):
            reg_file["R1"] = "0"*16
            reg_file["FLAGS"] = reg_file["FLAGS"][:12] + "1" + reg_file["FLAGS"][13:]
        else:                       
            reg_file[registers[query[7:10]]] = sixteen_bit_binary(decimal_to_7binary(temp_2-temp_3))

    if opcode == "00110":
        temp_2 = binary_to_decimal(reg_file[registers[query[10:13]]])
        temp_3 = binary_to_decimal(reg_file[registers[query[13:16]]])

        if (temp_2*temp_3>2**16):
            reg_file["R1"] = "0"*16
            reg_file["FLAGS"] = reg_file["FLAGS"][:12] + "1" + reg_file["FLAGS"][13:]           
        else:
            reg_file[registers[query[7:10]]] = sixteen_bit_binary(decimal_to_7binary(temp_2*temp_3))

    if opcode == "01010":
        temp_2 = binary_to_decimal(reg_file[registers[query[10:13]]])
        temp_3 = binary_to_decimal(reg_file[registers[query[13:16]]])
        reg_file[registers[query[7:10]]] = sixteen_bit_binary(decimal_to_7binary(temp_2 ^ temp_3))
        
    if opcode == "01011":
        temp_2 = binary_to_decimal(reg_file[registers[query[10:13]]])
        temp_3 = binary_to_decimal(reg_file[registers[query[13:16]]])
        reg_file[registers[query[7:10]]] = sixteen_bit_binary(decimal_to_7binary(temp_2 | temp_3))
        
    if opcode == "01100":
        temp_2 = binary_to_decimal(reg_file[registers[query[10:13]]])
        temp_3 = binary_to_decimal(reg_file[registers[query[13:16]]])
        reg_file[registers[query[7:10]]] = sixteen_bit_binary(decimal_to_7binary(temp_2 & temp_3))

    if opcode == "10000":
        # print(reg_file[registers[query[10:13]]])
        # print(reg_file[registers[query[13:16]]])
        temp_1 = float_to_decimal(reg_file[registers[query[10:13]]])
        temp_2 = float_to_decimal(reg_file[registers[query[13:16]]])
        # print(temp_1)
        # print(temp_2)
        if (len(decimal_to_float(temp_1+temp_2))>8):
            reg_file["R0"] = "0"*16
            reg_file["FLAGS"] = reg_file["FLAGS"][:12] + "1" + reg_file["FLAGS"][13:]  
        else:
            reg_file[registers[query[7:10]]] = sixteen_bit_binaryf(decimal_to_float(temp_1 + temp_2))
    
    if opcode == "10001":
        temp_1 = float_to_decimal(reg_file[registers[query[10:13]]])
        temp_2 = float_to_decimal(reg_file[registers[query[13:16]]])
        # print(temp_1)
        # print(temp_2)
        if (temp_2>temp_1):
            reg_file["R1"] = "0"*16
            reg_file["FLAGS"] = reg_file["FLAGS"][:12] + "1" + reg_file["FLAGS"][13:]
        else:
            reg_file[registers[query[7:10]]] = sixteen_bit_binaryf(decimal_to_float(temp_1 - temp_2))
    
    # Type B
    if opcode == "00010":
        reg_code = query[6:9]
        reg_type = registers[reg_code]
        reg_file[reg_type] = sixteen_bit_binary(query[9:])

    if opcode == "01000":
        reg_code = query[6:9]
        reg_type = registers[reg_code]
        num = binary_to_decimal(query[9:])
        for i in range(num):
            reg_file[reg_type] = "0" + reg_file[reg_type][0:-1]

    if opcode == "01001":
        reg_code = query[6:9]
        reg_type = registers[reg_code]
        num = binary_to_decimal(query[9:])
        for i in range(num):
            reg_file[reg_type] = reg_file[reg_type][1:]+"0"

    if opcode == "10010":
        reg_code = query[5:8]
        reg_type = registers[reg_code]
        reg_file[reg_type] = sixteen_bit_binaryf(query[8:])

    # Type C
    if opcode == "00011":
        reg1 = query[10:13]
        reg2 = query[13:16]
        reg_file[registers[reg1]] = temp_flag

    if opcode == "00111":
        temp_2 = binary_to_decimal(reg_file[registers[query[10:13]]])
        temp_3 = binary_to_decimal(reg_file[registers[query[13:16]]])
        if (temp_3 == 0):
            reg_file["FLAGS"] = reg_file["FLAGS"][:12] + "1" + reg_file["FLAGS"][13:]
            reg_file["R0"] = "0"*16 
            reg_file["R1"] = "0"*16 
        else:    
            reg_file["R0"] = sixteen_bit_binary(decimal_to_7binary(temp_2//temp_3))
            reg_file["R1"] = sixteen_bit_binary(decimal_to_7binary(temp_2 % temp_3))

    if opcode == "01101":
        reg_file[registers[query[7:10]]] = sixteen_bit_binary(decimal_to_7binary(~binary_to_decimal(reg_file[registers[query[10:13]]])))
        
    if opcode == "01110":
        temp_2 = binary_to_decimal(reg_file[registers[query[10:13]]])
        temp_3 = binary_to_decimal(reg_file[registers[query[13:16]]])

        if temp_2 == temp_3:
            reg_file["FLAGS"] = "0"*16
            reg_file["FLAGS"] = reg_file["FLAGS"][:15]+"1"
        elif temp_2 > temp_3:
            reg_file["FLAGS"] = "0"*16
            reg_file["FLAGS"] = reg_file["FLAGS"][:14] + "1"+ reg_file["FLAGS"][15]
        else:
            reg_file["FLAGS"] = "0"*16
            reg_file["FLAGS"] = reg_file["FLAGS"][:13] + "1"+ reg_file["FLAGS"][14:]
    
    #Type D
    if opcode=="00100":
        mem_add = query[9:16]
        if mem_add in var_add:
            reg_file[registers[query[6:9]]] = sixteen_bit_binary(decimal_to_7binary(var_add[mem_add]))
        else:
            var_add[mem_add] = 0
            
    if opcode=="00101":
        mem_add = query[9:16]
        var_add[mem_add] = binary_to_decimal(reg_file[registers[query[6:9]]])
    

    #Type E
    if opcode == "01111":
        pc = decimal_to_7binary(binary_to_decimal(query[9:16])-1)

    if opcode=="11100":
        if temp_flag[13]=="1":
            pc = decimal_to_7binary(binary_to_decimal(query[9:16])-1)

    if opcode=="11101":
        if temp_flag[14] == "1":
            pc = decimal_to_7binary(binary_to_decimal(query[9:16])-1)

    if opcode=="11111":
        if temp_flag[15] == "1":
            pc = decimal_to_7binary(binary_to_decimal(query[9:16])-1)

    if opcode == "11010":
        print_reg()
        break

    print_reg()
    temp_flag = reg_file["FLAGS"]
    pc = decimal_to_7binary(binary_to_decimal(pc) + 1)

for var in var_add :
    mem.append(sixteen_bit_binary(decimal_to_7binary(var_add[var]))+"\n")

for i in range(128-len(mem)):
    mem.append("0"*16+"\n")

for i in mem:
    print(i.strip())
# f.close()
