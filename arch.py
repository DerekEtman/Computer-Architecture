#  1. Truth Tanles
#  2. Transistor logic
#  3. File I/O in simple machine


'''
A or B

A      B      result
--------------------
1      0      1
0      1      1
0      0      0
1      1      1


A and B

A     B       result
--------------------
0     0        0
1     0        0
0     1        0
1     1        1

not (A and B)

A     B       result
--------------------
0     0        1
0     1        1
1     0        1
1     1        0

A xor B 

A     B       result
--------------------
0     0        0
0     1        1
1     0        1
1     1        0

not(a or not b) and b or not ( a or b) == not a

A    B     result
_______________________
0    0     1
0    1     1
1    0     0
1    1     0

for a in [False, True]:
    for b in [False, True]:
        print(f"{a} - {b} -- {not(a or not b) and b or not (a or b)}")

        
A    B     result
_______________________
0    0     1
0    1     1
1    0     0
1    1     0
'''

