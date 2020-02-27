"""CPU functionality."""

import sys


# **No longer need these since I label them in the switchbranch**
# LDI = 0b10000010
# PRN = 0b01000111
# HLT = 0b00000001
# MUL = 10100010



class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        # hold up to 256 bytes of memory
        self.ram = [0] * 256
        # * general purpose registers
        self.reg = [0] * 8 
        # Program Counter, Address of the currently executing instruction
        self.pc = 0
        # Sp
        self.sp = 7
        # Memory Address Register, holds the memory address we're reading or writing
        self.mar = 0
        # Memory Data Register, holds the value to write or the value just read
        self.mdr = 0
        # Branch table holding functions and the IR Opcode value
        self.branchtable = {}
        self.branchtable[0b10000010] = {'instruction_name':'LDI', 'retrieve': self.LDI_handler}
        self.branchtable[0b01000111] = {'instruction_name':'PRN', 'retrieve': self.PRN_handler}
        self.branchtable[0b00000001] = {'instruction_name':'HLT', 'retrieve': self.HLT_handler}
        self.branchtable[0b10100010] = {'instruction_name':'MUL', 'retrieve': self.alu}

    



    def load(self, filename):
        """Load a program into memory."""
        print(f"---Loading File---\n {filename}")
        try:
            address = 0
            # opening the file
            with open(filename) as f:
                # read through all the lines
                for line in f:
                    # parse out the comments
                    comment_split = line.strip().split("#")

                    # cast the numbers from strings into ints
                    value = comment_split[0].strip()

                    # ignore any blank lines
                    if value == "":
                        continue

                    num = int(value,2)
                    self.ram[address] = num
                    address += 1

        
        # if there is no file
        except FileNotFoundError:
            # return error message
            print("File not found")
            # exit prog
            sys.exit(2)

        # check if file was called for load in
        if len(sys.argv) != 2:
            print(f"Please include file name. Ex/ python -filename-")
            sys.exit(1)

        # address = 0

        # # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]

        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1

    def LDI_handler(self,a):
        print(f"\n--Running LDI--")
        # print(f"Op_a: {operand_a}, Op b: {operand_b}")
        address = self.ram_read(self.pc + 1)
        value = self.ram_read(self.pc + 2)

        self.reg_write(address, value)
        self.pc += 3        

    def PRN_handler(self,a):
        print(f"\n--Printing--")
        address = self.ram_read(self.pc + 1)

        self.reg_read(address)
        self.pc += 2

    def HLT_handler(self,a):
        print(f"\n--Finished--")
        sys.exit(2)


    def ram_read(self, mar):
        '''
        `ram_read()` should accept the address to read and return the value stored there.
        '''

        # mar holds the Address
        # mdr holds the Value

        return self.ram[mar]


    def ram_write(self,mdr, mar):
       ''' 
       `raw_write()` should accept a value to write, and the address to write it to.
       '''
       self.ram[mar] = mdr
       return self.ram[mar]

    def reg_read(self, mar):
        return self.reg[mar]


    def reg_write(self, mar, mdr):
        self.reg[mar] = mdr
        print(f"Self.reg[{mar}: {self.reg[mar]}]")
        # return self.reg[mar]



    def alu(self, op):
        """ALU operations."""   
        
        reg_a = self.ram_read(self.pc + 1)
        reg_b = self.ram_read(self.pc + 2)
        # print(f"self.reg_read(reg_a): {self.reg_read(self.pc + 1)} * self.reg_read(reg_b): ")

        if op == "ADD":
            print(f"--ADD--")
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc

        # Multiply the values in two registers together and store the result in registerA.
        elif op == "MUL":
            print(f"--Multiplying--")
            value = self.reg_read(reg_a) * self.reg_read(reg_b)
            self.reg_write(reg_a,value)
        else:
            raise Exception("Unsupported ALU operation")

        self.pc += 3

    def HLT(self):
        sys.exit(0)

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""

        while True:

            # Grabbing the instructions from RAM
            IR = self.ram[self.pc]
            # print(f"PC at start: {self.pc}, IR: {IR}, operand_a: {operand_a}, operand_b : {operand_b}")
            # print(f"{self.ram}")

            # Grab instructions from branchtable 
            get = self.branchtable[IR]

            # Accessing correct instruction from the branchtable
            # Calling the correct handler from Branchtable
            # Same as calling: 
                # if IR == LDI:
                    # self.LDI_handler()
            get['retrieve'](get["instruction_name"])

            # if IR == LDI:
            #     self.LDI_handler()
            # elif IR == PRN:
            #     print(f"\n--Printing--")
            #     self.reg_read(operand_a)
            #     self.pc += 2
            # elif IR == HLT:
            #     print(f"\n--Stopping--")
            #     sys.exit(0)






