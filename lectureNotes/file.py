#  Take an arg, load the values from that file and put it in an arg

import sys


print(sys.argv)


#  open the gile
if len(sys.argv) != 2:
    print("errorL: must have file name")
    sys.exit(1)

mem = [0] * 256
mem_pointer = 0


try:
    # open the file
    with open(sys.argv[1]) as f:
        # read all the lines
        for line in f:
            # parse out comments
            comment_split = line.split("#")
            # cast the numbers from strings to ints 
            value = comment_split[0]

            # ignore blank lines
            if value =="":
                continue

            print(value)
            num = int(num,2)
            mem[mem_pointer] = num
            mem_pointer += 1

            print("{num:08}: {num:d}")

except FileNotFoundError:
    print("file not found")
    sys.exit(2)




# populate a memory array