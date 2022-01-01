from sys import argv
from enum import Enum

class InsType(Enum):
    INSTRUCTION = 0
    OPERATION = 1
    COMMAND = 2
    CALL = 4

instructions = {

    "=": ["mov", 2],

    "&": ["and", 2],
    "|": ["or", 2], 

    "-": ["sub", 2],
    "--": ["dec", 1],

    "+": ["add", 2],
    "++": ["inc", 1],

    "*": ["mul", 2],
    "**": ["imul", 2],

    "/": ["div", 2],
    "//": ["idiv", 2],

    "!|": ["xor", 2],
    "!": ["not", 1],
    "=-": ["neg", 1],
}

keywords = [
    "global"
]

#user generated
labels = []

registers = {
    "rax": 8, "eax": 4, "ax": 2, "ah": 1, "al": 1,
    "rcx": 8, "ecx": 4, "cx": 2, "ch": 1, "cl": 1,
    "rdx": 8, "edx": 4, "dx": 2, "dh": 1, "dl": 1,
    "rbx": 8, "ebx": 4, "bx": 2, "bh": 1, "bl": 1,
    "rsp": 8, "esp": 4, "sp": 2, "spl": 1,
    "rbp": 8, "ebp": 4, "bp": 2, "bpl": 1,
    "rsi": 8, "esi": 4, "si": 2, "sil": 1,
    "rdi": 8, "edi": 4, "di": 2, "dil": 1,
    "r8": 8, "r8d": 4, "r8w": 2, "r8b": 1,
    "r9": 8, "r9d": 4, "r9w": 2, "r9b": 1,
    "r10": 8, "r10d": 4, "r10w": 2, "r10b": 1,
    "r11": 8, "r11d": 4, "r11w": 2, "r11b": 1,
    "r12": 8, "r12d": 4, "r12w": 2, "r12b": 1,
    "r13": 8, "r13d": 4, "r13w": 2, "r13b": 1,
    "r14": 8, "r14d": 4, "r14w": 2, "r14b": 1,
    "r15": 8, "r15d": 4, "r15w": 2, "r15b": 1
}

chars = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "[",
    "]",
    "_",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

def translate(file):
    newfile = ''

    lines = []
    with open(file, 'r') as f:
        lines = f.readlines()

    lines_new = []
    for i in lines:
        segments = []
        num = 0
        type = 0
        for e in i:
            if e in chars:
                if type == 1:
                    num = len(segments)
                type = 0
                if num == len(segments):
                    segments.append("")
                segments[num] += e
            elif ord(e) > 32:
                if type == 0:
                    num = len(segments)
                type = 1
                if num == len(segments):
                    segments.append("")
                segments[num] += e
            else:
                num = len(segments)
        lines_new.append(segments)

    for i in range(len(lines_new)):

        line = ""
        pos = 0
        while len(lines_new[i]) != 0:

            if lines_new[i][pos] in registers:
                pos += 1
                pass

            elif lines_new[i][pos] in instructions:

                if pos%2 != 0:

                    instruction = instructions[lines_new[i][pos]]
                    line += instruction[0] + ' '
                    lines_new[i].pop(pos)
                    pos -= 1

                    for x in range(instruction[1]):
                        line += lines_new[i][pos]
                        lines_new[i].pop(pos)
                        if x != instruction[1]-1:
                            line += ", "

            else:
                print("At line: " + str(i) +" unknown character is present")
                break
        if len(line) != 0:
            newfile += line + '\n'

    return newfile

argv.pop(0)
if len(argv) < 1:
    print("No arguments!!!!!")
    exit(1)

pasm = translate(argv[0])

with open("pasm.pasm", 'w+') as f:
    f.write(pasm)