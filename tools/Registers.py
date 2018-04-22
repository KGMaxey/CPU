# Dictionary of all registers
from random import choice

# Dictionary of all normal registers
registers = {"$Zero": 0, "$r0": 0, "$0": 0,
             "$at": 1, "$1": 1,
             "$v0": 2, "$2": 2,
             "$v1": 3, "$3": 3,
             "$a0": 4, "$4": 4,
             "$a1": 5, "$5": 5,
             "$a2": 6, "$6": 6,
             "$a3": 7, "$7": 7,
             "$t0": 8, "$8": 8,
             "$t1": 9, "$9": 9,
             "$t2": 10, "$10": 10,
             "$t3": 11, "$11": 11,
             "$t4": 12, "$12": 12,
             "$t5": 13, "$13": 13,
             "$t6": 14, "$14": 14,
             "$t7": 15, "$15": 15,
             "$s0": 16, "$16": 16,
             "$s1": 17, "$17": 17,
             "$s2": 18, "$18": 18,
             "$s3": 19, "$19": 19,
             "$s4": 20, "$20": 20,
             "$s5": 21, "$21": 21,
             "$s6": 22, "$22": 22,
             "$s7": 23, "$23": 23,
             "$t8": 24, "$24": 24,
             "$t9": 25, "$25": 25,
             "$k0": 26, "$26": 26,
             "$k1": 27, "$27": 27,
             "$gp": 28, "$28": 28,
             "$sp": 29, "$29": 29,
             "$fp": 30, "$30": 30,
             "$ra": 31, "$31": 31,
             }

# Dictionary for registers writable in randomly generated code
writeable_registers = {
             "$at": 1, "$1": 1,
             "$v0": 2, "$2": 2,
             "$v1": 3, "$3": 3,
             "$a0": 4, "$4": 4,
             "$a1": 5, "$5": 5,
             "$a2": 6, "$6": 6,
             "$a3": 7, "$7": 7,
             "$t0": 8, "$8": 8,
             "$t1": 9, "$9": 9,
             "$t2": 10, "$10": 10,
             "$t3": 11, "$11": 11,
             "$t4": 12, "$12": 12,
             "$t5": 13, "$13": 13,
             "$t6": 14, "$14": 14,
             "$t7": 15, "$15": 15,
             "$s0": 16, "$16": 16,
             "$s1": 17, "$17": 17,
             "$s2": 18, "$18": 18,
             "$s3": 19, "$19": 19,
             "$s4": 20, "$20": 20,
             "$s5": 21, "$21": 21,
             "$s6": 22, "$22": 22,
             "$s7": 23, "$23": 23,
             "$t8": 24, "$24": 24,
             "$t9": 25, "$25": 25,
             "$k0": 26, "$26": 26,
             "$k1": 27, "$27": 27,
             }


# Returns a random register from the normal 32
def rand_register():
    return choice(list(registers.items()))[1]


# Returns a random register from the writable 27 used in randomly generated code
def rand_w_register():
    return choice(list(writeable_registers.items()))[1]

