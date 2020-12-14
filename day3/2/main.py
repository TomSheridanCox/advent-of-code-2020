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
    # -1 to deal with 1-based indexing
    char_lower_pos = int(split[0].split("-")[0]) - 1
    char_upper_pos = int(split[0].split("-")[1]) - 1 # duplicate split - shoot me
    required_char = split[1].split(":")[0]
    password_chars = list(split[2])
    lower_pos_check = password_chars[char_lower_pos] is required_char
    upper_pos_check = password_chars[char_upper_pos] is required_char
    if lower_pos_check != upper_pos_check: # effectively xor
        valid_counter += 1
    print(valid_counter)