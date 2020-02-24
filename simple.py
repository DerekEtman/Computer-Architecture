import sys

PRINT_BEEJ = 1
HALT       = 2
PRINT_NUM  = 3
SAVE       = 4
PRINT_REGISTER = 5
ADD        = 6




memory = [
    PRINT_BEEJ,
    SAVE,
    65,
    2,
    SAVE,
    20,
    3,
    ADD,
    2,
    3,
    PRINT_REGISTER,
    2,
    HALT
]

register = [0] * 8
pc = 0 #Program Counter


while True:
    command = memory[pc]

    if command == PRINT_BEEJ:
        print("Beej!")
        pc += 1
    elif command == PRINT_NUM:
        num = memory[pc + 1]
        print(num)
        pc += 2
    elif command == SAVE:
        # Save a value to a register
        num =  memory[pc + 1]
        reg = memory[pc + 2]
        register[reg] = num
        pc += 3
    elif command == PRINT_REGISTER:
        # Print the value in the register
        reg = memory[pc + 1]
        print(register[reg])
        pc += 2
    elif command == ADD:
        # ADD 2 registers, store the result in the first reg
        reg_a = memory[pc + 1]
        reg_b = memory [pc + 2]
        register[reg_a] += register[reg_b]
        pc += 2
    elif command == HALT:
        sys.exit(1)
    else:
        print(f"I do not know that command: {command}")
        sys.exit(1)





