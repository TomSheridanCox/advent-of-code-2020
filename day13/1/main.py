with open("input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
earliest_timestamp = int(content[0])
buses = [int(bus) for bus in content[1].replace('x,','').split(',')]
print(earliest_timestamp)
print(buses)
# actual code starts here
for bus in buses:
    # int() cuts off decimal
    divided = int(earliest_timestamp/bus)
    print("{} / {} = {}".format(earliest_timestamp, bus, divided))
    multi = bus * divided
    print("{} * {} = {}".format(bus, divided, multi))
    added = multi + bus
    print("{} + {} = {}".format(multi, bus, added))
    diff = added - earliest_timestamp
    print("Diff for bus {} = {}".format(bus, diff))
    answer = bus * diff
    print(answer)
