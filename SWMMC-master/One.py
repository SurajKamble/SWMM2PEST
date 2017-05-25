# Embedded file name: One.py
"""
Created on Tue Aug 09 13:17:32 2016

@author: SKamble
"""
import re
import os
import matplotlib.pyplot as plt
from scipy import linspace
import pyqtgraph as pg


#   Parameter class to create rows of parameters in the parameter data section
#   with (name, par_trans, value, minimum, maximum)
class Parameter(object):

    def __init__(self, name):
        self.name = name
        self.par_trans = ''
        self.value = ''
        self.l_val = ''
        self.h_val = ''

    def get_name(self):
        return self.name

    def set_value(self, value):
        self.value = value

    def set_l_val(self, l_val):
        self.l_val = l_val

    def set_h_val(self, h_val):
        self.h_val = h_val

    def get_value(self):
        return self.value
        
    def get_par_trans(self):
        return self.par_trans

    def get_l_value(self):
        return self.l_val

    def get_h_value(self):
        return self.h_val

    def get_all_vals(self):
        return (self.par_trans, self.value, self.l_val, self.h_val)

    def set_all_vals(self, vals):
        self.par_trans = vals[0]
        self.value = vals[1]
        self.l_val = vals[2]
        self.h_val = vals[3]


class Create_pst(object):
    
    par_objs = []
    num_of_out_pars = 0

    def __init__(self, *args, **kwargs):
        self.tpl_file_name = ""
        if len(args) == 1:
            self.par_objs = self.generate_pars(args[0])
        else:
            self.generate_ins(args[0], args[1])
            
            

    def generate_pars(self, f):
        with open(f, 'r') as tpl_fname:
            #pars = re.findall('#(\\w*)#', tpl_fname.read())
            #print tpl_fname.read()
            self.pars = re.findall(r'#(\s*\w+\s*)#', tpl_fname.read())
            par_objs = []
            print self.pars
            print type(f)
            tpl_file = f.split('/')[-1]
            self.tpl_file_name = tpl_file.split('.')[0]
            for par in self.pars:
                p = Parameter(par)
                par_objs.append(p)
            
            self.ctl_file_name = self.tpl_file_name + ".pst"
            self.ins_file_name = self.tpl_file_name + ".ins"
            self.ins_file_name1 = "report.ins"
            
           
            return par_objs
            
    # Estimated values of parameters
    def show_result(self, rec_file, out_name, field_file):
        #rec_file = self.ctl_file_name + ".rec"
        with open(rec_file, 'r') as f:
            res = re.findall(r'Adjustable parameters ----->(.*)Observations ----->', 
                             f.read(), flags=re.DOTALL)
            
            res_str = ''.join(res)
            print res_str
            
        with open(self.tpl_file_name + ".tpl", 'r')  as tpl_fname:   
            all_text = tpl_fname.read()

            all_text = all_text.replace("ptf #\n", "\b")
            
            for par in self.par_objs:
                #print "in for"
                print par.get_name()
                line = re.findall(par.get_name().strip() + r'(.*)', res_str)
                print line
                value = line[0].split()[0]
            
                print value
                
                
                #print all_text
                all_text = all_text.replace("#" + par.get_name() + "#", value)
                #all_text.replace("#" + self.pars[0] + "#", "sdfasdfs")
                #all_text[1571] = "sfsdfs"
                #print all_text[1571:1580]
                
                #index = all_text.index("#" + self.pars[0] + "#")
                
        #print self.par_objs
        
            #print "this is "
            #print line
        
            out_file_name = "\".\\" + self.tpl_file_name + ".txt\""
            #all_text = all_text.replace(out_file_name, "\"" + self.tpl_file_name + "_new.txt\"")
            all_text = all_text.replace(out_file_name, "\".\\" + self.tpl_file_name + "_new.txt\"")
            print all_text
            new_inp_file = self.tpl_file_name + "_new"
            print self.tpl_file_name
            

        with open(new_inp_file + ".inp", 'w') as new_f:
            print "in with"
            new_f.write(all_text)
            
        cmd_line = "swmm5110_test.exe " + " " + new_inp_file + ".inp " + \
                    new_inp_file + ".rpt " + new_inp_file + ".out\n"
        
        os.system(cmd_line)
        
        old_vals = []
        
        x_axis = []
        
        with open(self.tpl_file_name + ".txt", 'r') as old_inp:
            vals = re.findall(r'--------\n(.*)', old_inp.read(), flags=re.DOTALL)
            print "vals = "
            #print vals
            
            
            rows = ''.join(vals).split("\n")
            
            print rows
            
            pos = Create_pst.get_ins_line(out_name)[2]
            
            
            for col in rows:
                x_axis.append(col.split()[2])
                old_vals.append(col.split()[pos])
            
        new_vals = []
        
        with open(new_inp_file + ".txt", 'r') as new_inp:
            vals = re.findall(r'--------\n(.*)', new_inp.read(), flags=re.DOTALL)
            print "vals = "
            #print vals
            
            
            rows = ''.join(vals).split("\n")
            
            print rows
            
            pos = Create_pst.get_ins_line(out_name)[2]
            
            
            for col in rows:
                new_vals.append(col.split()[pos])
        
        
        lines = [ line1.rstrip('\n') for line1 in open(field_file) ]   
        print "lines = "
        print len(lines)
        print "new_vals = "
        print len(new_vals)
        
        
        #plt.plot(x_axis, old_vals, 'r', x_axis, lines, 'g')
        #x1 = plt.subplot(2,1,1)
        
        x = linspace(0, len(lines)-1, len(lines))
        #pg.plot(x, old_vals)
        #plt.show()
        
        return lines, old_vals, new_vals, x
        
        '''
        with open(self.tpl_file_name + ".inp", 'r+') as inp_fname:
            full_text = inp_fname.read()
            end = index + len(value)
            
            print full_text[index-5:1590]
            full_text.replace(full_text[index-5:1590], "sdfsfsdf")
            #print full_text
        '''
            
            
            
    def save_old_vals(self, field_fname, out_file, out_par):
        
        self.field_vals = [ line1.rstrip('\n') for line1 in open(field_fname) ] 
        
        with open(out_file, 'r') as old_out_f:
            vals = re.findall(r'--------\n(.*)', old_out_f.read(), flags=re.DOTALL)
            print "vals = "
            #print vals
            
            
            rows = ''.join(vals).split("\n")
            
            print rows
            
            pos = Create_pst.get_ins_line(out_par)[2]
            
            self.old_vals = []
            
            for col in rows:
                #x_axis.append(col.split()[2])
                self.old_vals.append(col.split()[pos])
                
            print "end of save_old_vals"
        
        
        
        
    def get_new_vals(self, out_file, out_par):
        
        with open(out_file, 'r') as new_out_f:
            vals = re.findall(r'--------\n(.*)', new_out_f.read(), flags=re.DOTALL)
            print "vals = "
            #print vals
            
            
            rows = ''.join(vals).split("\n")
            
            print rows
            
            pos = Create_pst.get_ins_line(out_par)[2]
            
            self.new_vals = []
            
            for col in rows:
                #x_axis.append(col.split()[2])
                self.new_vals.append(col.split()[pos])
                
            print "end of get new vals"
                
        return self.new_vals
        
        

    def fill_ctl_data_section(self, num_of_pars, num_of_obs, num_of_out_pars):
        
        with open(self.ctl_file_name, 'w') as ctlfile:
            
            print "in ctl section"
            print num_of_pars
            print num_of_obs
            sec = "  " + str(num_of_pars) + " " + str(num_of_obs) + \
                    "    " + "1     0     1\n" + \
                    "    1     " + str(num_of_out_pars) + " " + "single point   1   0   0\n" + \
                    "  5.0   2.0   0.3  0.03    10\n" + \
                    "  3.0   3.0 0.001  0\n" + \
                    "  0.1\n" + \
                    "   30  0.01     3     3  0.01     3\n" + \
                    "    1     1     1\n"  
                    
                    
            '''
            sec += " 1     0     1\n"
            sec += "  1     3 single point   1   0   0\n"
            sec += "  5.0   2.0   0.3  0.03    10\n"
            sec += "  3.0   3.0 0.001  0\n"
            sec += "  0.1\n"
            sec += "  30  0.01     3     3  0.01     3\n"
            sec += "  1     1     1\n"
            '''
            
            self.num_of_obs = int(num_of_obs)
            
            print sec
            ctlfile.write('pcf\n* control data\nrestart estimation\n')
            ctlfile.write(sec)
            
            

    def fill_par_data_section(self, parameters):
        
        with open(self.ctl_file_name, 'a') as ctlfile:
            
            ctlfile.write("* parameter groups\nparagroup  relative 0.01  0.0  switch  2.0 parabolic\n")
            ctlfile.write('* parameter data\n')
            for par in parameters:
                par_trans, val, l, h = par.get_all_vals()
                line = par.get_name() + '   ' + par_trans + '  relative  ' + val + ' ' + l + ' ' + h + ' ' + '   paragroup 1.0 0.0 1\n'
                ctlfile.write(line)



    def fill_obs_data_section(self, f, out_f, obs_name):
        """
        File format: 
            For each model output parameter, provide a separate file with just the
            field data for that parameter
        """
        print 'In obs_data method'
        line_num = 1
        lines = [ line.rstrip('\n') for line in open(f) ]
        print obs_name
        
        if out_f[-3:] == "txt":
            with open(self.ctl_file_name, 'a') as ctlfile:
                print 'inside with'
                #print os.environ['swmm5']
                ctlfile.write("* observation groups\nobsgroup\n")
                ctlfile.write('* observation data\n')
                for line in lines:
                    obs_line = obs_name + str(line_num) + '           ' + line + ' 1.0 obsgroup\n'
                    ctlfile.write(obs_line)
                    line_num += 1
        
        if out_f[-3:] == "rpt":
            lines = [ line.rstrip('\n') for line in open(f) ]
            with open(self.ctl_file_name, 'a') as ctlfile:
                ctlfile.write(obs_name + '           ' + line + ' 2.0 obsgroup\n')
                
                
    def fill_other_sections(self, num_of_out_pars):
        with open(self.ctl_file_name, 'a') as ctlfile:
            
            #SWMM5 and PEST have to be set as env. variables
            
            #swmm5 =  os.environ['swmm5']
            line = "* model command line\n" + "swmm5110_test.exe " + " " + self.tpl_file_name + ".inp " + \
                    self.tpl_file_name + ".rpt " + self.tpl_file_name + ".out\n"
            ctlfile.write(line)
            ctlfile.write("* model input/output\n")
            tpl_field = self.tpl_file_name + ".tpl  " + self.tpl_file_name + ".inp\n"
            ins_field = self.tpl_file_name + ".ins  " + self.tpl_file_name + ".txt"
            
            ctlfile.write(tpl_field)
            ctlfile.write(ins_field)
            
            if num_of_out_pars > 1:
                ins_field1 = "\nreport.ins " + self.tpl_file_name + ".rpt"
                ctlfile.write(ins_field1)
            
            
    def call_pest(self):
        print "In call_pest method"
        line = "pest " + self.ctl_file_name
        print line
        output = os.popen(line).readlines()
        
        output = re.sub("\x08.", "", ''.join(output))
        print output
        
        return output
        
        
    def generate_ins(self, par, out_fname, num_of_out_pars, field_fname):
        Create_pst.num_of_out_pars += 1
        num_of_obs = self.num_of_obs
        
        if out_fname[-3:] == "txt":
            
            with open(self.ins_file_name, 'w') as insfile:
                ins_file_headers = 'pif #\n#-------#\n'
                line = Create_pst.get_ins_line(par)
                print 'in generate_ins method'
                print line
                self.out_par_name = line[1]
                #print self.out_par_name
                line_num = 1
                insfile.write(ins_file_headers)
                if num_of_out_pars == 1:
                    
                    while num_of_obs > 0:
                        ins_line = 'l1 [' + line[1] + str(line_num) + ']' + line[0] + '\n'
                        print ins_line
                        insfile.write(ins_line)
                        line_num += 1
                        num_of_obs -= 1
                    
                else:
                    while num_of_obs > 1:
                        ins_line = 'l1 [' + line[1] + str(line_num) + ']' + line[0] + '\n'
                        print ins_line
                        insfile.write(ins_line)
                        line_num += 1
                        num_of_obs -= 1
                        
            
            self.fill_obs_data_section(field_fname, out_fname, self.out_par_name)
            
            self.save_old_vals(field_fname, out_fname, par)
            
        elif out_fname[-3:] == "rpt":
            line = Create_pst.get_ins_line(par)
            self.out_par_name1 = line[1]
            with open(self.ins_file_name1, 'w') as insfile:
                line_num = 1
                insfile.write("pif #\n#LID Performance#\n")
                insfile.write("l8 [" + line[1] + "]" + line[0] + "\n")
            self.fill_obs_data_section(field_fname, out_fname, self.out_par_name1)
                

    @staticmethod
    def get_ins_line(x):
        return {
         'Surface Runoff': ['75:82', 'srunoff', 7],
         'Drain Outflow': ['85:92', 'doutflow', 8],
         'Surface Depth': ['95:102', 'sdepth', 9],
         'Storage Depth': ['115:122', 'stdepth', 11],
         'Surface Outflow(LID Summary)': ['71:79', 'ttl_sflw', 0], 
         'Drain Outflow(LID Summary)': ['81:89', 'ttl_dflw', 0]}[x]



class ControlDataSection(object):

    def line1(RSTFLE = 'restart', PESTMODE = 'estimation'):
        return RSTFLE + '  ' + PESTMODE

    def line2(NPAR, NOBS, NPARGP, NPRIOR, NOBSGP, MAXCOMPDIM):
        return NPAR + ' ' + NOBS + ' ' + NPARGP + ' ' + NPRIOR + ' ' + NOBSGP + ' ' + MAXCOMPDIM

    def line3(NTPLFLE, NINSFLE, PRECIS, DPOINT, NUMCOM, JACFILE, MESSFILE, OBSREREF):
        return NTPLFLE + ' ' + NINSFLE + ' ' + PRECIS + ' ' + DPOINT + ' ' + NUMCOM + ' ' + JACFILE + ' ' + MESSFILE + ' ' + OBSREREF

    def line4(RLAMBDA1, RLAMFAC, PHIRATSUF, PHIREDLAM, NUMLAM, JACUPDATE, LAMFORGIVE, DERFORGIVE):
        return RLAMBDA1 + ' ' + RLAMFAC + ' ' + PHIRATSUF + ' ' + PHIREDLAM + ' ' + NUMLAM + ' ' + JACUPDATE + ' ' + LAMFORGIVE + ' ' + DERFORGIVE

    def line5(RELPARMAX, FACPARMAX, FACORIG, IBOUNDSTICK, UPVECBEND):
        return RELPARMAX + ' ' + FACPARMAX + ' ' + FACORIG + ' ' + IBOUNDSTICK + ' ' + UPVECBEND

    def line6(PHIREDSWH, NOPTSWITCH, SPLITSWH, DOAUI, DOSENREUSE, BOUNDSCALE):
        return PHIREDSWH + ' ' + NOPTSWITCH + ' ' + SPLITSWH + ' ' + DOAUI + ' ' + DOSENREUSE + ' ' + BOUNDSCALE

    def line7(NOPTMAX, PHIREDSTP, NPHISTP, NPHINORED, RELPARSTP, NRELPAR, PHISTOPTHRESH, LASTRUN, PHIABANDON):
        return NOPTMAX + ' ' + PHIREDSTP + ' ' + NPHISTP + ' ' + NPHINORED + ' ' + RELPARSTP + ' ' + NRELPAR + ' ' + PHISTOPTHRESH + ' ' + LASTRUN + ' ' + PHIABANDON

    def line8(ICOV, ICOR, IEIG, IRES, JCOSAVE, VERBOSEREC, JCOSAVEITN, REISAVEITN, PARSAVEITN, PARSAVERUN):
        return ICOV + ' ' + ICOR + ' ' + IEIG + ' ' + IRES + ' ' + JCOSAVE + ' ' + VERBOSEREC + ' ' + JCOSAVEITN + ' ' + REISAVEITN + ' ' + PARSAVEITN + ' ' + PARSAVERUN