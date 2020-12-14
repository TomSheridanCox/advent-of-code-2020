with open("example_input.txt") as f:
    content = f.readlines()
print(len(''.join(content)))
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
print(len(content[0]))
row_len = len(content[0]) - 1
# Thoughts:
# All the rows are the same length of 31 chars
# To go down one, we must always add the row length
# To go across three, we must always add 3 to the row length
# Therefore, we can join the input into a single string and step-through it
# at an appropriate increment, as dictated by the above rules! I think...
# actual code starts here
step = len(content[1]) + 3
num_trees_hit = 0
joined_map = list(''.join(content))
for idx in range(0,len(joined_map),step):
    print("idx = "  + str(idx))
    if joined_map[idx] == "#":
        joined_map[idx] = "X"
        num_trees_hit += 1
joined_map2 = ''.join(joined_map)
for idx in range(0, len(joined_map2), row_len):
    print(idx)
    print(row_len)
    a = ''.join(joined_map2[idx:idx+row_len])
    print(len(a))
print(num_trees_hit)