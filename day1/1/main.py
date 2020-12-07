with open("input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [int(x.strip()) for x in content]
numbers = set(content)
print(len(numbers))
# actual code starts here
for i in numbers:
    minus = 2020 - i
    if minus in numbers: # in is O(1) unless collisions
        result = minus * i
        break
print("answer: " + str(result))