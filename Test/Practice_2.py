from PyQt5.QtWidgets import QFileDialog

fname = '/Users/surajkamble/Documents/SWMM2PEST/SWMMC-master/04-27-2011/pp16.txt'

with open(fname, 'r') as out_file:
    lines = out_file.readlines()

for line_num in range(len(lines)):
    if lines[line_num].startswith("-------"):
        start_line = line_num + 1

split_lines = lines[start_line].split(" ")

index_needed = 8

index = 0

print(' '.join(split_lines))

for i in range(len(split_lines)):

    if split_lines[i] != '':
        split_lines[i] += " "

l = ' '.join(split_lines)

print("L: " + l)

split_lines = l.split(" ")

print(split_lines)

index_got = 0

for i in range(len(split_lines)):

    if index == index_needed+1:
        print(i)
        index_got = i - 1
        print(split_lines[i-1])
        break

    if split_lines[i] != '':
        print(index)
        index += 1

location_start = 0

location_end = 0

for i in range(len(split_lines)):
    if i < index_got:
        if split_lines[i] == '':
            location_start += 1
        else:
            location_start += len(split_lines[i])
    if i == index_got:
        location_end = location_start + len(split_lines[i])

print(location_start)
print(location_end)

line_num = start_line

ins_lines = ""

obs_name = "dflow"

while line_num < len(lines):

    dstamp = lines[line_num].split()[0]

    dstamp = dstamp.split("-")[1]

    tstamp = lines[line_num].split()[1]

    tstamp = tstamp.split(":")[0] + tstamp.split(":")[1]

    print(dstamp + tstamp)

    #obs_name += tstamp

    line = "l1  [" + obs_name + dstamp + tstamp + "]" + str(location_start) + ":" + str(location_end) + "\n"

    ins_lines += line

    line_num += 1

print(ins_lines)


