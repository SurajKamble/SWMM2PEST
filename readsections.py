from subcatchments import Subcatchment


class ReadSections:

    def __init__(self):
        self.subcatchments_data = []
        print "In ReadSections.__init__()"
        pass

    def read_subcatchment_data(self, file_name):

        print file_name
        with open(file_name, 'r') as inp_file:

            print file_name

            lines = inp_file.readlines()

            # print lines
            # print "\n after"

        # subcatchments_data = []

        for line_num in range(len(lines)):

            if lines[line_num] == "[SUBCATCHMENTS]\n":
                sub_items = self.read_section_data(lines, line_num)

                print "Subcatchments: "
                print sub_items

                for item in sub_items:
                    if len(item) > 1:
                        item = item.split()
                        print item
                        sub = Subcatchment()  # Create and assign values to subcatchment objects.

                        sub.name = item[0]
                        sub.rain_gage = item[1]
                        sub.outlet = item[2]
                        sub.area.value = item[3]
                        sub.percent_impervious.value = item[4]
                        sub.width.value = item[5]
                        sub.percent_slope.value = item[6]
                        sub.curb_length.value = item[7]
                        if len(item) > 8:
                            sub.snow_pack.value = item[8]

                        self.subcatchments_data.append(sub)

            if lines[line_num] == "[SUBAREAS]\n":
                sub_items = self.read_section_data(lines, line_num)

                print sub_items
                for item, sub_data in zip(sub_items, self.subcatchments_data):

                    item = item.split()
                    print item
                    print "Sub Data: "
                    print sub_data
                    if item[0] == sub_data.name:
                        print "in If"
                        sub_data.n_imperv.value = item[1]
                        sub_data.n_perv.value = item[2]
                        sub_data.storage_depth_imperv.value = item[3]
                        sub_data.storage_depth_perv.value = item[4]
                        sub_data.percent_zero_impervious.value = item[5]
                        sub_data.subarea_routing.value = item[6]
                        if len(item) > 7:
                            sub_data.percent_routed.value = item[7]

            if lines[line_num] == "[INFILTRATION]\n":
                sub_items = self.read_section_data(lines, line_num)

                for item, sub_data in zip(sub_items, self.subcatchments_data):

                    item = item.split()
                    print item
                    print "Sub Data: "
                    print sub_data

                    if item[0] == sub_data.name:
                        sub_data.suction.value = item[1]
                        sub_data.hydraulic_conductivity.value = item[2]
                        sub_data.initial_moisture_deficit.value = item[3]

            if lines[line_num] == "[LID_USAGE]\n":
                sub_items = self.read_section_data(lines, line_num)

                for item in sub_items:
                    item = item.split()

                    print "LID USAGE: "

                    print item[0]

                    for sub_data in self.subcatchments_data:

                        print sub_data.name

                        if item[0] == sub_data.name:
                            sub_data.control_name.value = item[1]
                            sub_data.number_replicate_units.value = item[2]
                            sub_data.area_each_unit.value = item[3]
                            sub_data.top_width_overland_flow_surface.value = item[4]
                            sub_data.percent_initially_saturated.value = item[5]
                            sub_data.percent_impervious_area_treated.value = item[6]
                            sub_data.send_outflow_pervious_area.value = item[7]
                            sub_data.detailed_report_file = item[8]
                            if len(item) > 9:
                                sub_data.subcatchment_drains_to = item[9]

        return self.subcatchments_data


    #@staticmethod
    def read_section_data(self, lines, line_num):

        data = ""

        while not (lines[line_num + 1].startswith("[")):
            data += lines[line_num]

            line_num += 1
        # print data

        # print data.split("\n")
        items = []
        for item in data.split("\n"):

            if not (item.startswith("[") or item.startswith(";") or item == ""):
                items.append(item)
                # print item
        # print items
        return items

    '''
    def read_input_data(self, inp_file):
        with open(inp_file, 'r') as inp_file:
            #all_inp_data = inp_file.read()

            #sections = all_inp_data.index("[SUBCATCHMENTS]")#re.findall(r'\[SUBCATCHMENTS\]', all_inp_data)
            #print all_inp_data[1244 + len("[SUBCATCHMENTS]")]

            lines = inp_file.readlines()
            print lines
            print "\n after"
            for line_num in range(len(lines)):
                if lines[line_num] == "[SUBCATCHMENTS]\n":
                    items = self.read_section_data(lines, line_num)
                    self.subcathments = []
                    for item in items:
                        if item != "":
                            self.subcathments.append(Subcatchment(item.split()))
                    for s in self.subcathments:
                        print s.get_all()


                if lines[line_num] == "[SUBAREAS]\n":
                    items = self.read_section_data(lines, line_num)
                    self.sub_areas = []
                    for item in items:
                        if item != "":
                            self.sub_areas.append(SubArea(item.split()))

                    for s in self.sub_areas:
                        print s.get_all()


                if lines[line_num] == "[INFILTRATION]\n":
                    items = self.read_section_data(lines, line_num)
                    self.inflitrations = []
                    for item in items:
                        if item != "":
                            self.inflitrations.append(Infiltration(item.split()))

                    for s in self.inflitrations:
                        print s.get_all()

                if lines[line_num] == "[LID_CONTROLS]\n":
                    items = self.read_section_data(lines, line_num)
                    self.lid_controls = []
                    for item in items:
                        if item != "" and len(item.split()) > 2:

                            self.lid_controls.append(LIDControls(item.split()))

                    for s in self.lid_controls:
                        print s.get_all()

                if lines[line_num] == "[LID_USAGE]\n":
                    items = self.read_section_data(lines, line_num)
                    self.lid_usages = []
                    for item in items:
                        if item != "":
                            self.lid_usages.append(LIDUsage(item.split()))

                    for s in self.lid_usages:
                        print s.get_all()

    '''

'''
subcatchments_data = ReadSections().read_subcatchment_data("UMD0111.inp")
print subcatchments_data

for sub in subcatchments_data:
    print vars(sub)
    # print sub.name + " " + str(sub.rain_gage) + " " + str(sub.outlet) + " " + str(sub.n_imperv) + " " + str(sub.n_perv) + " " + str(sub.storage_depth_imperv)
'''

'''
{'curb_length': '0', 'percent_routed': 100.0, 'percent_impervious': '100', 'tag': '', 'snow_pack': '',
'top_width_overland_flow_surface': '0', 'subcatchment_drains_to': '', 'area': '0.224', 'width': '143.000000',
'n_imperv': '.020000000', 'number_replicate_units': '0', 'percent_impervious_area_treated': '0',
'percent_initially_saturated': '0', 'storage_depth_imperv': '1', 'percent_slope': '.100000000', 'description': '',
'send_outflow_pervious_area': '0', 'detailed_report_file': '', 'n_perv': '0.24', 'storage_depth_perv': '5',
'control_name': 'None', 'outlet': 'LID', 'suction': '99.441', 'subarea_routing': 'OUTLET',
'percent_zero_impervious': '100', 'name': 'Roadway', 'rain_gage': '01-11-2006_Storm',
'initial_moisture_deficit': '0.378', 'hydraulic_conductivity': '7.112', 'area_each_unit': '0'}
'''