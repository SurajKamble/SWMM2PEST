from readsections import ReadSections


class write_sections():
    def __init__(self, subcatchments_data, lid_controls_data):

        self.subcatchments_data = subcatchments_data
        self.lid_controls_data = lid_controls_data

    def write_template_data(self, subcatchments):

        """
    
        Find location of [SUBCATCHMENTS] and replace each subcatchment data with new data with parameter values replaced with 
        short parameter names. And then write the file with this new data.
        
        If sucatchment data if from index x to y, then replace x to y of the file with new data.
    
    
        """

        self.input_file_name = ReadSections.input_file_name

        self.read_subcatchment_data(self.input_file_name, self.subcatchments_data)

        self.tpl_file_name = self.input_file_name[:-3] + "tpl"

        self.replaced_file_lines = "ptf #\n" + self.string_of_file_lines



        with open(self.tpl_file_name, 'w') as tpl_file:

            tpl_file.write(self.replaced_file_lines)
            


        print("Replaced file lines: ")

        print(self.string_of_file_lines)

    def read_subcatchment_data(self, file_name, subcatchments):

        print(file_name)

        with open(file_name, 'r') as inp_file:

            print(file_name)

            self.list_of_file_lines = inp_file.readlines()

        with open(file_name, 'r') as inp_file:

            self.string_of_file_lines = inp_file.read()

            print("String of file lines after reading: ")
            print(self.string_of_file_lines)

            original_subcatchment_data = ""

        for line_num in range(len(self.list_of_file_lines)):

            if self.list_of_file_lines[line_num] == "[SUBCATCHMENTS]\n":

                print("line_num1: ")
                print(line_num)

                original_subcatchment_data = self.read_section_data(self.list_of_file_lines, line_num,
                                                                    self.string_of_file_lines)
                print("line_num2: ")
                print(line_num)

                self.replace_subcatchment_data(original_subcatchment_data, line_num, subcatchments)

                break

    def read_section_data(self, list_of_file_lines, line_num, string_of_file_lines):

        original_data = ""

        while not (list_of_file_lines[line_num + 1].startswith("[")):

            original_data += list_of_file_lines[line_num]

            line_num += 1

        print("DATA: ")
        print(original_data)

        return original_data

    def replace_subcatchment_data(self, original_subcatchment_data, line_num, subcatchments):

        current_index = 0

        for subcatchment in subcatchments:

            print((self.list_of_file_lines[line_num + 1].startswith("[") or
                           self.list_of_file_lines[line_num + 1].startswith(";") or
                               self.list_of_file_lines[line_num + 1] == ""))

            line_num += 1

            while not (self.list_of_file_lines[line_num].startswith("[")):

                if not (self.list_of_file_lines[line_num].startswith(";") or self.list_of_file_lines[line_num] == ""):

                    print(self.list_of_file_lines[line_num])

                    current_index = current_index + 1

                    individual_sub_data = ""

                    print(current_index)

                    if current_index == subcatchment.sub_index:

                        individual_sub_data = self.list_of_file_lines[line_num]

                        individual_sub_data_as_list_with_spaces = individual_sub_data.split(" ")

                        individual_sub_data_as_list = individual_sub_data.split()

                        for par in subcatchment.get_selected_subcatchment_pars():

                            print("par short name: ")
                            print(par.get_short_name())

                            individual_sub_data_as_list[par.index] = par.get_short_name()

                        for i in range(len(individual_sub_data_as_list_with_spaces)):
                            if individual_sub_data_as_list_with_spaces[i] == "":
                                individual_sub_data_as_list.insert(i, individual_sub_data_as_list_with_spaces[i])

                        print("data as list with spaces: ")
                        print(individual_sub_data_as_list)

                        replaced_sub_data = ' '.join(individual_sub_data_as_list)

                        replaced_sub_data += "\n"

                        print("Individual sub data: ")
                        print(individual_sub_data)

                        print("String of file lines before replacing: ")
                        print(self.string_of_file_lines)


                        self.string_of_file_lines = self.string_of_file_lines.replace(individual_sub_data, replaced_sub_data)

                        print("String of file lines: ")
                        print(self.string_of_file_lines)

                        print("replaced sub data: ")
                        print(replaced_sub_data)

                line_num += 1
