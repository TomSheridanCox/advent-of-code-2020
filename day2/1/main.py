from collections import Counter

with open("input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
print(len(content))
print(content)
# actual code starts here
valid_counter = 0
for line in content:
    split = line.split()
    print(split)
    char_lower_limit = int(split[0].split("-")[0])
    char_upper_limit = int(split[0].split("-")[1]) # duplicate split - shoot me
    required_char = split[1].split(":")[0]
    counted_password_chars = Counter(list(split[2]))
    print(str(char_lower_limit) + " < " + str(counted_password_chars[required_char]) + " < " + str(char_upper_limit))
    if char_lower_limit <= counted_password_chars[required_char] <= char_upper_limit:
        valid_counter += 1
    print(valid_counter)