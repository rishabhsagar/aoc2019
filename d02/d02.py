import sys

with open("input.data", "r") as f:
    d = f.readline().split(',')
    d = [int(x) for x in d]

def process(data, opers):
    opcode, pos1, pos2, pos3 = opers
    print("Processing params", opcode, pos1, pos2, pos3 )
    if opcode == 99:
        print("Output:", data)
        sys.exit(1)

    elif opcode == 1:
        v1 = data[pos1]
        v2 = data[pos2]
        data[pos3] = v1 + v2
    
    elif opcode == 2:
        v1 = data[pos1]
        v2 = data[pos2]
        data[pos3] = v1 * v2
    else:
        print("Unknown opcode", opcode)
    
    return data

if __name__ == "__main__":

    pointer = 0

    while (pointer < len(d)):
        if d[pointer] in [1,2,99]:
            d = process(d, d[pointer: pointer+4])
            #print(d[pointer: pointer+4])
        pointer = pointer + 4
    print("Output:", d)