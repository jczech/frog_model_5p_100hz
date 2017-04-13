#!/bin/bash
#PBS -N analys_frog_newmdl
#PBS -l nodes=1:ppn=8
#PBS -l walltime=340:00:00              
#PBS -j oe
#PBS -q gb64

set echo
cd /helix/home/usr/ue/2/rlagha/RL/frog_mdl/frog_AP_newmdl_1.5xalpha/binary_count

./frogAnalyzerYV7  -T 4 -e -i 0.01 -p 5 -s 9 -y 11 seed_count.*.bin.bz2 >& result.dat
