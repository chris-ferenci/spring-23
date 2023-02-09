# Prompt
# Write a Python Function that takes in an integer input (say 129) and returns a string that names each digit separately ("one two nine").

# Sample I/P: 547

# Sample O/P: "five four seven"


def numToString():
    while True:
        num = int(input("Enter a number:"))
        numList = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

        numStr = str(num)

        numOut = ''

        for i in numStr:
            numOut += ' ' + numList[int(i)]

        stripped_numOut = numOut.strip()
        print(stripped_numOut)
    

numToString()
