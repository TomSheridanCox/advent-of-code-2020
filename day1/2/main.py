with open("input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [int(x.strip()) for x in content]
numbers = set(content)
print(len(numbers))
# actual code starts here
def findTrips():
    result = 0
    for i in numbers:
        minus = 2020 - i
        print("First minus: " + str(minus))
        for y in numbers:
            if y >= minus:
                continue
            second_minus = minus - y
            if second_minus in numbers:
                result = i * y * second_minus
                return result

print("answer: " + str(findTrips()))