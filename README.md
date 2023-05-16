# co-project

Description :
The Assembler takes input from stdin and prints the corresponding binary code of the given assembly instruction. The program performs error handling by checking each line of instruction and prints a specific error if it finds any, along with the line number.

Example.

Input:
label: mov R1 $5
mov R2 55
add R1 R2 R1
cmp R1 R2 R3
sub R1 R1 R2
je label1
hlt

Output:
Error at line number 2 : General Syntax Error
Error at line number 4 : can't compare more than 2 registers
Error at line number 6 : undeclared label type : label1:
General Synatx Error at line number 6

The plus point of our program is that it can handle muliple error of the same instruction and generate output for the correct instruction.

Assembler contributions:-
Ayush - Making Instruction Type E and Debugging
Ramish - Making Intruction Type B and C and Debugging
Tushar - Making other instructions and debugging
Vashu - Making Tnstruction Type A and Handling Errors

