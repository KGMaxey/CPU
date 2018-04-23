from myhdl import *

@block
def branch_calculator(In1_extended_imm, In2_pc_plus_4, BTA):

    @always(In1_extended_imm)
    def calc():
        BTA.next = intbv((In1_extended_imm * 4) + In2_pc_plus_4)

    return calc

@block
def jump_calculator(In1_instruction, In2_pc_plus_4, Jump_Address):

    @always(In1_instruction)
    def calc():
        temp = modbv((In1_instruction * 4), 0, 2**32)
        temp[32:28] = In2_pc_plus_4[32:28]
        Jump_Address.next = temp

    return calc