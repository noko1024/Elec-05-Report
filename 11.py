
#AND回路
def AND(a,b):
    return a&b

#OR回路
def OR (a,b):
    return a|b

#NOT回路
def NOT(a):
    return a^1
#NOR回路
def NOR(a,b):
    return NOT(OR(a,b))

#XOR回路
def XOR(a,b):
    return NOR(AND(a,b),NOR(a,b))

#半加算器
def half_adder(a,b):
    sum = XOR(a,b)
    carry = AND(a,b)
    return sum,carry

def full_adder(a,b,carry):
    s1,c1 = half_adder(a,b)
    s2,c2 = half_adder(s1,carry)
    carry = OR(c1,c2)
    return s2,carry



def main():
    data = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]


    for i in data:
        a = i[0]
        b = i[1]
        carry = i[2]
        s,c = full_adder(a,b,carry)
        print(a,b,s,c)

main()