# These codes are used to generate reaction parameter files for the multi-pulses az mcell simulation.
# the first parameter is the interval between pulses, the second on the number of
# pulses
# 
# This script was adapted on 04102015 by Markus Dittrich based on a script by
# Jun Ma.
# RL:  this code is revised for step potentials
# to run it : python RATE_GEN_RL_step.py 0.01 (interval) 2 (number of pulses)
# 

import sys

interval=float((sys.argv)[1])
num_of_pulses=int((sys.argv)[2])


def Make_New_Parameter_File_1(template_name,interval):
    parameter_change_time_step=0.00002
    if interval<0.003:
        print "Error: Interval cannot be shorter than 0.003s.\n"
        exit(0)
    f_in=open(template_name)
    output_name=template_name[0:len(template_name)-13]+".txt"
    f_out=open(output_name,'w')
    line=f_in.readline()
    token=line.split()
    first_value=float(token[1])
    f_out.write(line)
    while 1:
        line=f_in.readline()
        if not line: break
        f_out.write(line)
        line_backup=line
    token=line_backup.split()
    last_value=float(token[1])
    f_in.close()
    
    mid_interval_steps=int((interval-0.003)/parameter_change_time_step)
    
    for p in range(1,num_of_pulses):
#        for i in range(1,mid_interval_steps):
#            output_line=str(0.003+(p-1)*interval+i*parameter_change_time_step)+'  '+str(last_value-(last_value-first_value)/mid_interval_steps*i)+'\n'
    
        f_in=open(template_name)
        while 1:
            line=f_in.readline()
            if not line: break
            token=line.split()
            time=float(token[0])
            output_line=str(str(time+interval+(p-1)*interval))+'  '+token[1]+'\n'
            f_out.write(output_line)

    f_out.close()


def Make_New_Parameter_File_2(template_name,interval):
    parameter_change_time_step=0.00002
    if interval<0.003:
        print "Error: Interval cannot be shorter than 0.003s.\n"
        exit(0)
    
    total_t=interval*(num_of_pulses-1)+0.003
    for p in range(1,num_of_pulses+1):
        f_in=open(template_name)
        output_name=template_name[0:len(template_name)-13]+"_"+str(p)+".txt"
        f_out=open(output_name,'w')
        start_t=interval*(p-1)
        if p>1:
           end_t=start_t+0.003
        else:
           end_t=start_t+0.003
        t=0
        while t<=total_t:
            if t>=start_t and t<=end_t:
                line=f_in.readline()
                token=line.split()
                output_line=str(t)+"    "+token[1]+"\n"
            else:
                output_line=str(t)+"    "+str(0)+"\n"                   #'0\n'
            f_out.write(output_line)
            t=t+parameter_change_time_step

        f_in.close()
        f_out.close()


Make_New_Parameter_File_1('2_alpha_control_short_scaled_1.0_template.txt',interval)
Make_New_Parameter_File_1('2_beta_control_short_template.txt',interval)
Make_New_Parameter_File_1('3_alpha_control_short_scaled_1.0_template.txt',interval)
Make_New_Parameter_File_1('5_beta_control_short_template.txt',interval)
Make_New_Parameter_File_1('beta_control_short_template.txt',interval)
Make_New_Parameter_File_1('alpha_control_short_scaled_1.0_template.txt',interval)
Make_New_Parameter_File_2('k3_control_short_1.8_template.txt',interval)













