# These scripts are used to generate codes in mdl for the multi-pulse model in frog az mcell simulations.
# Input pulse_num = number of pulses 

import sys

if len(sys.argv) == 1:
	pulse_num = 2
else:
	pulse_num = int((sys.argv)[1])



#################
# molecules.mdl #
#################

channel = ['A01','A04','A09','A13','A17','A21','A25','A29','A33','A38','A42','A46','A49','D01','D04','D09','D13','D17','D21','D25','D29','D33','D37','D42','D46','D49']
#channel = ['D25']
#
f = open("molecules.mdl",'w')

out = "DEFINE_MOLECULES {\n\n"
f.write(out)

for i in channel:
	for pulse in range(1,pulse_num+1):
		out = "ca_" + i + "_" + str(pulse) + "{ DIFFUSION_CONSTANT_3D = ca_diff_const }\n"
		f.write(out)

out = "\n\n\n" + "unbound_sensor { DIFFUSION_CONSTANT_2D = 0 }\n"
f.write(out)

for i in channel:
	for pulse in range(1,pulse_num+1):
		out = "bound_sensor_" + i + "_" + str(pulse) + "{ DIFFUSION_CONSTANT_2D = 0 }\n"
		f.write(out)

out = "\n\n\n" + "unbound_sensor_Y { DIFFUSION_CONSTANT_2D = 0 }\n"
f.write(out)

for i in channel:
	for pulse in range(1,pulse_num+1):
		out = "bound_sensor_Y_" + i + "_" + str(pulse) + "{ DIFFUSION_CONSTANT_2D = 0 }\n"
		f.write(out)



out = "\n\n\n" + "unbound_fixed_buffer { DIFFUSION_CONSTANT_3D = 0 }\n"
f.write(out)

for i in channel:
        for pulse in range(1,pulse_num+1):
                out = "bound_fixed_buffer_" + i + "_" + str(pulse) + "{ DIFFUSION_CONSTANT_3D = 0 }\n"
                f.write(out)

out = "\n\n\n" + "unbound_mobile_buffer { DIFFUSION_CONSTANT_3D = 0 }\n"
f.write(out)


for i in channel:
        for pulse in range(1,pulse_num+1):
                out = "bound_mobile_buffer_" + i + "_" + str(pulse) + "{ DIFFUSION_CONSTANT_3D = mobile_buffer_diff_const }\n"
                f.write(out)


out = "\n\n\n"
f.write(out)


for i in channel:
	out = "closed_channel_" + i + "{ DIFFUSION_CONSTANT_2D = 0 }\n"
	f.write(out)
	out = "closed2_channel_" + i + "{ DIFFUSION_CONSTANT_2D = 0 }\n"
        f.write(out)
	out = "closed3_channel_" + i + "{ DIFFUSION_CONSTANT_2D = 0 }\n"
        f.write(out)
	out = "open_channel_" + i + "{ DIFFUSION_CONSTANT_2D = 0 }\n\n"
        f.write(out)


out = "\n}\n"
f.write(out)


f.close()




#######################
# surface_classes.mdl #
#######################

f = open("surface_classes.mdl",'w')

out = "DEFINE_SURFACE_CLASSES {\n\n"
f.write(out)

out = "absorb_all_calcium_ions {\n\n"
f.write(out)

for i in channel:
	for pulse in range(1,pulse_num+1):
		out = "ABSORPTIVE = ca_" + i + "_" + str(pulse) + "\n"
		f.write(out)

for i in channel:
        for pulse in range(1,pulse_num+1):
                out = "ABSORPTIVE = bound_mobile_buffer_" + i + "_" + str(pulse) + "\n"
                f.write(out)


out = "\n\n}\n\n"
f.write(out)

out = "transparent_to_all_diffusing_molecules {\n\n"
f.write(out)

for i in channel:
        for pulse in range(1,pulse_num+1):
                out = "TRANSPARENT = ca_" + i + "_" + str(pulse) + "\n"
                f.write(out)

out = "TRANSPARENT = unbound_mobile_buffer \n\n"
f.write(out)

for i in channel:
        for pulse in range(1,pulse_num+1):
                out = "TRANSPARENT = bound_mobile_buffer_" + i + "_" + str(pulse) + "\n"
                f.write(out)


#out = "\n\n\nTRANSPARENT = unbound_mobile_buffer\n"
#f.write(out)

##########################
####        RL
#########################


#for i in channel:
#        for pulse in range(1,pulse_num+1):
#                out = "TRANSPARENT = bound_mobile_buffer_" + i + "_" + str(pulse) + "\n"
#                f.write(out)
#
out = "\n\n}\n\n} /*end define surface classes*/\n"
f.write(out)

f.close()


##########################
# reactions.mdl #
##########################

f = open("reactions.mdl",'w')

out = "DEFINE_REACTIONS {\n\n"
f.write(out)

for i in channel:
	for pulse in range(1,pulse_num+1):
		out = "unbound_sensor' + ca_" + i + "_" + str(pulse) + "' -> bound_sensor_" + i + "_" + str(pulse) + "' [sensor_onrate]\n"
		f.write(out)

out = "\n\n\n"
f.write(out)

for i in channel:
        for pulse in range(1,pulse_num+1):
		out = "bound_sensor_" + i + "_" + str(pulse) + "' -> unbound_sensor' + ca_" + i + "_" + str(pulse) + "' [sensor_offrate]\n"
                f.write(out)

out = "\n\n\n"
f.write(out)


for i in channel:
	for pulse in range(1,pulse_num+1):
		out = "unbound_sensor_Y' + ca_" + i + "_" + str(pulse) + "' -> bound_sensor_Y_" + i + "_" + str(pulse) + "' [sensor_Y_onrate]\n"
		f.write(out)

out = "\n\n\n"
f.write(out)

for i in channel:
        for pulse in range(1,pulse_num+1):
		out = "bound_sensor_Y_" + i + "_" + str(pulse) + "' -> unbound_sensor_Y' + ca_" + i + "_" + str(pulse) + "' [sensor_Y_offrate]\n"
                f.write(out)

out = "\n\n\n"
f.write(out)

########################
#     RL
########################


for i in channel:
        for pulse in range(1,pulse_num+1):
                out = "unbound_fixed_buffer + ca_" + i + "_" + str(pulse) + " -> bound_fixed_buffer_" + i + "_" + str(pulse) + " [fixed_buffer_onrate]\n"
                f.write(out)

out = "\n\n\n"
f.write(out)

for i in channel:
        for pulse in range(1,pulse_num+1):
                out = "bound_fixed_buffer_" + i + "_" + str(pulse) + " -> unbound_fixed_buffer + ca_" + i + "_" + str(pulse) + " [fixed_buffer_offrate]\n"
                f.write(out)


out = "\n\n\n"
f.write(out)



for i in channel:
        for pulse in range(1,pulse_num+1):
                out = "unbound_mobile_buffer + ca_" + i + "_" + str(pulse) + " -> bound_mobile_buffer_" + i + "_" + str(pulse) + " [mobile_buffer_onrate]\n"
                f.write(out)

out = "\n\n\n"
f.write(out)

for i in channel:
        for pulse in range(1,pulse_num+1):
                out = "bound_mobile_buffer_" + i + "_" + str(pulse) + " -> unbound_mobile_buffer + ca_" + i + "_" + str(pulse) + " [mobile_buffer_offrate]\n"
                f.write(out)


out = "\n\n\n"
f.write(out)

for i in channel:
	out = "closed_channel_" + i + "' -> closed2_channel_" + i + "' [\"3_alpha_control_short_scaled_1.0.txt\"]\n"
	f.write(out)
	out = "closed2_channel_" + i + "' -> closed_channel_" + i + "' [\"beta_control_short.txt\"]\n"
	f.write(out)
	out = "closed2_channel_" + i + "' -> closed3_channel_" + i + "' [\"2_alpha_control_short_scaled_1.0.txt\"]\n"
	f.write(out)
	out = "closed3_channel_" + i + "' -> closed2_channel_" + i + "' [\"2_beta_control_short.txt\"]\n"
	f.write(out)
	out = "closed3_channel_" + i + "' -> open_channel_" + i + "' [\"alpha_control_short_scaled_1.0.txt\"]\n"
	f.write(out)
	out = "open_channel_" + i + "' -> closed3_channel_" + i + "' [\"5_beta_control_short.txt\"]\n"
        f.write(out)

	for pulse in range(1,pulse_num+1):
		out = "open_channel_" + i + "' -> open_channel_" + i + "' + ca_" + i + "_" + str(pulse) + "' [\"k3_control_short_1.8_" + str(pulse) + ".txt\"]\n"
		f.write(out)
	out = "\n\n"
	f.write(out)

out = "\n\n\n}\n"
f.write(out)

f.close()


#####################
# reaction_data.mdl #
#####################

f = open("reaction_data.mdl",'w')

out = "REACTION_DATA_OUTPUT {\n\nOUTPUT_BUFFER_SIZE =3000\nBINARY_OUTPUT = TRUE\nBINARY_OUTPUT_COMPRESSION_LEVEL = 9\nBINARY_OUTPUT_COMPRESSION_TYPE = BZIP2\nBINARY_OUTPUT_DIRECTORY = binary_out\nBINARY_OUTPUT_FILENAME = \"seed_count.\" & seed & \".bin.bz2\"\n\nSTEP = reaction_output_time_step\n\n{COUNT[unbound_mobile_buffer,WORLD]}=> reactdir & \"mobile_buffer_unbound.\" & seed & \".dat\"\n\n{COUNT[unbound_fixed_buffer,WORLD]}=> reactdir & \"buffer_unbound.\" & seed & \".dat\"\n\n"
f.write(out)

out = "{"
f.write(out)
for i in channel:
	for pulse in range(1,pulse_num+1):
		out = "COUNT[bound_mobile_buffer_" + i + "_" + str(pulse) + ",WORLD]"
		if pulse == pulse_num and channel.index(i) == len(channel)-1:
			out = out + "}=> reactdir & \"mobile_buffer_bound.\" & seed & \".dat\"\n\n\n"
		else:
			out = out + "+\n"
		f.write(out)

##########################
####        RL
#########################

out = "{"
f.write(out)
for i in channel:
        for pulse in range(1,pulse_num+1):
                out = "COUNT[bound_fixed_buffer_" + i + "_" + str(pulse) + ",WORLD]"
                if pulse == pulse_num and channel.index(i) == len(channel)-1:
                        out = out + "}=> reactdir & \"buffer_bound.\" & seed & \".dat\"\n\n\n"
                else:
                        out = out + "+\n"
                f.write(out)


for i in range(1,27):

        if i < 10:
                i_tag = "0" + str(i)
        else:
                i_tag = str(i)

        out = "{"
        f.write(out)

        for j in channel:
##for i in range(1,27):

##        if i < 10:
##                i_tag = "0" + str(i)
##        else:
##                i_tag = str(i)
#i = 20
#i_tag = str(i)
#out = "{"
#f.write(out)

#for j in channel:
                for pulse in range(1,pulse_num+1):
                        if i <=13:
                                out = "COUNT[ca_" + j + "_" + str(pulse) + ",presynaptic_segment.vesicles.top.sampling_box_" + i_tag + "]"
                        else:
                                out = "COUNT[ca_" + j + "_" + str(pulse) + ",presynaptic_segment.vesicles.bottom.sampling_box_" + i_tag + "]"

                        if pulse == pulse_num and channel.index(j) == len(channel)-1:
                                out = out + "} => reactdir & \"summed_box_" + i_tag + "\" & \".\" & seed & \".dat\"\n"
                        else:
                                out = out + "+\n"
                        f.write(out)
			

out = "\n\n\n"
f.write(out)


for i in channel:
	for pulse in range(1,pulse_num+1):
		out = "{COUNT[ca_" + i + "_" + str(pulse) + ",WORLD]}=> reactdir & \"ca_ions_" + i + "_" + str(pulse) + "\" & \".\" & seed & \".dat\"\n"
		f.write(out)

out = "\n\n\n{"
f.write(out)
for i in channel:
	for pulse in range(1,pulse_num+1):
		out = "COUNT[ca_" + i + "_" + str(pulse) + ",WORLD]"
		if pulse == pulse_num and channel.index(i) == len(channel)-1:
			out = out + "}=> reactdir & \"summed_ca_ions\" & \".\" & seed & \".dat\"\n\n\n"			
		else:
			out = out + "+\n"
		f.write(out)
	

for pulse in range(1,pulse_num+1):
	out = "{"
	f.write(out)
	for i in channel:
		out = "COUNT[ca_" + i + "_" + str(pulse) + ",WORLD]"
		if channel.index(i) == len(channel)-1:
			out = out + "}=> reactdir & \"summed_ca_ions_" + str(pulse) + "\" & \".\" & seed & \".dat\"\n\n\n"
		else:
			out = out + "+\n"
		f.write(out)

for i in range(1,27):

        if i < 10:
                i_tag = "0" + str(i)
        else:
                i_tag = str(i)


        for j in channel:

##for i in range(1,27):

##        if i < 10:
##                i_tag = "0" + str(i)
##        else:
##                i_tag = str(i)
#i = 20
#i_tag=str(i)

#for j in channel:
                for pulse in range(1,pulse_num+1):
                        if i <=13:
                                out = "{COUNT[bound_sensor_" + j + "_" + str(pulse) + ",presynaptic_segment.vesicles.top.sensor_" + i_tag + "[sites_all]]} => reactdir & \"vesicle_" + i_tag + "_ca_" + j + "_" + str(pulse) + ".\" & seed & \".dat\"\n"
                        else:
				out = "{COUNT[bound_sensor_" + j + "_" + str(pulse) + ",presynaptic_segment.vesicles.bottom.sensor_" + i_tag + "[sites_all]]} => reactdir & \"vesicle_" + i_tag + "_ca_" + j + "_" + str(pulse) + ".\" & seed & \".dat\"\n"
                        f.write(out)

out = "\n\n\n"
f.write(out)


for i in range(1,27):

        if i < 10:
                i_tag = "0" + str(i)
        else:
                i_tag = str(i)


        for j in channel:
##for i in range(1,27):

##        if i < 10:
##                i_tag = "0" + str(i)
##        else:
##                i_tag = str(i)
#i = 20
#i_tag=str(i)


#for j in channel:
                for pulse in range(1,pulse_num+1):
                        if i <=13:
                                out = "{COUNT[bound_sensor_Y_" + j + "_" + str(pulse) + ",presynaptic_segment.vesicles.top.sensor_Y_" + i_tag + "[sites_all]]} => reactdir & \"vesicle_Y_" + i_tag + "_ca_" + j + "_" + str(pulse) + ".\" & seed & \".dat\"\n"
                        else:
				out = "{COUNT[bound_sensor_Y_" + j + "_" + str(pulse) + ",presynaptic_segment.vesicles.bottom.sensor_Y_" + i_tag + "[sites_all]]} => reactdir & \"vesicle_Y_" + i_tag + "_ca_" + j + "_" + str(pulse) + ".\" & seed & \".dat\"\n"
                        f.write(out)

out = "\n\n\n"
f.write(out)



for i in channel:
	out = "{COUNT[open_channel_" + i + ",WORLD]}=> reactdir & \"open_channel_" + i + "\" & \".\" & seed & \".dat\"\n"
	f.write(out)


out = "\n\n\n{"
f.write(out)

for i in channel:
	out = "COUNT[open_channel_" + i + ",WORLD]"
	if channel.index(i) == len(channel)-1:
		out = out + "}=> reactdir & \"summed_open_channels\" & \".\" & seed & \".dat\"\n\n\n"
	else:
		out = out + "+\n"
	f.write(out)



X_sensor=[9,8,31,29,30,7,34,35,32,33,3,6,36,37,38,17,39,40,41,42,15,16,45,43,44,14,48,49,46,47,4,12,50,24,51,10,25,26,27,28]
X_sensor.sort()

#Y_sensor=range(0, 144)
Y_sensor=[122, 70, 126, 142, 62, 118, 22, 134, 110, 66, 106, 130, 2, 114, 42, 138]

for i in X_sensor:
	if i<10:
		i_tag='0'+str(i)
	else:
		i_tag=str(i)
	for j in range(1,27):
		if j<10:
			j_tag='0'+str(j)
		else:
			j_tag=str(j)

		for l in range(1,pulse+1):
##	for j in range(1,27):
##		if j<10:
##			j_tag='0'+str(j)
##		else:
##			j_tag=str(j)
#	j = 20
#	j_tag=str(j)

#	for l in range(1,pulse+1):
			for k in channel:
				if j<=13:
					base_out="COUNT[bound_sensor_"+k+"_"+str(l)+",presynaptic_segment.vesicles.top.sensor_"+j_tag+"[site_"+str(i)+"]]"
				else:
					base_out="COUNT[bound_sensor_"+k+"_"+str(l)+",presynaptic_segment.vesicles.bottom.sensor_"+j_tag+"[site_"+str(i)+"]]"			

				if len(channel)-1 == 0:
					out="{"+base_out+"} => reactdir & \"bound_vesicle_"+j_tag+"_sensor_"+i_tag+"_"+str(l)+".\" & seed & \".dat\"\n\n"
				elif channel.index(k)==0 and len(channel)-1 != 0:
					out="{"+base_out+"+\n"
				elif channel.index(k)==len(channel)-1 and len(channel)-1 != 0:
					out=base_out+"} => reactdir & \"bound_vesicle_"+j_tag+"_sensor_"+i_tag+"_"+str(l)+".\" & seed & \".dat\"\n\n"
				else:
					out=base_out+"+\n"
				f.write(out)	


out = "\n\n\n\n"
f.write(out)


for i in Y_sensor:
	if i<10:
		i_tag='0'+str(i)
	else:
		i_tag=str(i)
	for j in range(1,27):
		if j<10:
			j_tag='0'+str(j)
		else:
			j_tag=str(j)

		for l in range(1,pulse+1):
##	for j in range(1,27):
##		if j<10:
##			j_tag='0'+str(j)
##		else:
##			j_tag=str(j)
#	j = 20
#	j_tag=str(j)
#	for l in range(1,pulse+1):
			for k in channel:
				if j<=13:
					base_out="COUNT[bound_sensor_Y_"+k+"_"+str(l)+",presynaptic_segment.vesicles.top.sensor_Y_"+j_tag+"[site_"+str(i)+"]]"
				else:
					base_out="COUNT[bound_sensor_Y_"+k+"_"+str(l)+",presynaptic_segment.vesicles.bottom.sensor_Y_"+j_tag+"[site_"+str(i)+"]]"			

				if len(channel)-1 == 0:
					out="{"+base_out+"} => reactdir & \"bound_vesicle_"+j_tag+"_sensor_Y_"+i_tag+"_"+str(l)+".\" & seed & \".dat\"\n\n"
				elif channel.index(k)==0 and len(channel)-1 != 0:
					out="{"+base_out+"+\n"
				elif channel.index(k)==len(channel)-1 and len(channel)-1 != 0:
					out=base_out+"} => reactdir & \"bound_vesicle_"+j_tag+"_sensor_Y_"+i_tag+"_"+str(l)+".\" & seed & \".dat\"\n\n"
				else:
					out=base_out+"+\n"
				f.write(out)	


out = "\n\n\n}\n"
f.write(out)

f.close()










