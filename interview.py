import csv

with open('finalInput.txt', 'r') as file:
    finalData = file.read()

with open('testInput.csv', newline='') as f:
    reader = csv.reader(f)
    testData = list(reader)[0]


# Task: write code that given an input string of variable length returns the first index of a packet. A packet is preceeded by 4 unique characters in a row.


def getIndex(Input, markerLength):
    """ Sample Solution implemented in python"""
    buffer = set()
    # Need to check from when on there is a sequence of four distinct characters
    for i in range(len(Input)):
        # Iterate through and
        for j in range(i, i + markerLength):
            buffer.add(Input[j])
        if len(buffer) == markerLength:
            return i + markerLength
        else:
            buffer.clear()

    return -1

def getIndex2(Input, markerLength):
    """My interview solution when finished"""
    buffer = []
    for i in range(len(Input)):
        if len(buffer) > 0:
            if Input(i) in buffer:
                # If new character is in the buffer: empty it excluding new character
                while buffer[0] != Input(i):
                    del buffer[0]
            else:
                buffer.append(Input(i))
                if len(buffer) == markerLength:
                    return i + 1


def tester(markerLength, Function):
    print("\nTesting test datasets with function ", Function.__name__)
    solution = [5,6,10,11]
    # testInput=[TestInput1,TestInput2,TestInput3,TestInput4]
    output = []
    for i in range(4):
        output.append(Function(testData[i], markerLength))
        if output[i] != solution[i]:
            print("Test case Nr. ", i + 1, ": Wrong result. Output index is ",output[i], "but should be ", solution[i] )
        else:
            print("Test case Nr. ", i + 1, ": Correct result. Output index is ", output[i])



if __name__ == "__main__":
    marker_length = 4
    tester(marker_length, getIndex)
    tester(marker_length, getIndex2)
    print("\nIndex of testData: ", getIndex(finalData, marker_length))

