from subcatchments import DataField

class ss:

    def __init__(self):
        self.name = ''
        self.area = 4
        self.imperv = 5
        self.perv = 3

        self.value = {}


s = ss()
s.name = "suraj"

s.value[s.name] = [55, 144]

a = 'area'

vars(s)[a] = 10

print(vars(s))

d = DataField("Suraj_Kamble", "Suraj Kamble")



print(s.value)


def read_subcatchment_data(file_name):

    print(file_name)

    with open(file_name, 'r') as inp_file:

        print(file_name)

        lines = inp_file.readlines()

        print(lines)

        lines1 = inp_file.read()

        print(lines1)

        # print lines
        # print "\n after"

    # subcatchments_data = []

    lines2 = ""

    for line_num in range(len(lines)):

        if lines[line_num] == "[SUBCATCHMENTS]\n":
            print("In if")
            lines2 = read_section_data(lines, line_num, lines1)
            break

    print("Lines 2: ")
    print(lines2)

    with open(file_name, 'w') as f:
        f.write(lines2)


def read_section_data(lines, line_num, lines1):
    data = ""

    while not (lines[line_num + 1].startswith("[")):
        data += lines[line_num]

        line_num += 1
    print("DATA: ")
    print(data)

    data1 = data

    data1 = data1.replace("0.0158", "500")

    lines1.replace(data, data1)

    print("Lines: ")
    print(data1)

    return lines1

read_subcatchment_data("/Users/surajkamble/Documents/SWMM2PEST/ppvmnt16val2_copy.inp")

sss = "name date 11 200        0.5    100   20"



s_list1 = sss.split(" ")

s_list = sss.split()

print(s_list)

print("s_list1: ")

print(s_list1)

s_list[4] = "#srfc_strg#"

print(s_list)

for i in range(len(s_list1)):
    if s_list1[i] == "":
        s_list.insert(i, s_list1[i])

print("sss: ")
print(sss)


print(' '.join(s_list))





