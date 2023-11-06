#!/usr/bin/env bash

dmso_path=/home/bioinf/big-ssd/SCV2/DMSO/Shan_new/CV_Unique.bam
dmso_dup_path=/home/bioinf/big-ssd/SCV2/FPV_fake/Shan_new/CV_Unique.bam
nhc_path=/home/bioinf/big-ssd2/NHC/Shan/CV_Unique.bam
nhc_dup_path=/home/bioinf/big-ssd/SCV2/RBV_fake/Shan_new/CV_Unique.bam
fpv_path=/home/bioinf/big-ssd2/FPV/Shan/CV_Unique.bam
rbv_path=/home/bioinf/big-ssd2/RBV/Shan/CV_Unique.bam

exps=dmso,dmso_dup,nhc,nhc_dup,fpv,rbv

t=19 # number of threads
    
for i in ${exps//,/ } # comma separator pattern using //,/
do
    # echo "${!${i}_path} > ${i}.sub.sambamba.bam"
    path="${i}_path"
    echo "${!path} > ${i}.sub.sambamba.bam"
done