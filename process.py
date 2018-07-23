import re

numbers = re.findall('\d+', '5x + 2y = 5')

print(numbers[0])

print(numbers[1])

print(numbers[2])


input = 'x(4x(3x)) = (2y)'.replace(" ", "")
print(input)

# Step 1: Equal sign (=)

equal = input.find('=')

leftside = input[0:equal]
rightside = input[equal+1:]

print(leftside)
print(rightside)


# Step 2: Brackets ()
# Procedure:
"""
1. Find first ( and first )
2. delete from initial string and replace it with V1, V2 ... 
3. Store that string 


Exception: x(3x(5x)) so if in this bracket part, other brackets are present, continue with the inner part
"""

bracket1 = input.find('(')
bracket2 = input.find(')')

brackets = input[bracket1+1:bracket2]
print(brackets)


# Must be a for loop untill ???

if '(' in brackets:
    tempbracket = brackets.find('(')
    print(tempbracket)
    newposbracket = tempbracket + bracket1

else:
    print("There are no other brackets")

tempinput = input

# Next lines of code need to be fixed

tempinput.replace(tempinput[newposbracket:bracket2], 'V1')

print(tempinput)