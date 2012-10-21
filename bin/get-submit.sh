#!/bin/bash

ASST_NR=$1
ECE_SVN=svn+ssh://ug131.eecg.utoronto.ca/svn

#newgrp e344F12
for i in `seq -f "%03g" 1 39`
do
	svn co ${ECE_SVN}/os-${i}/svn/tags/asst${ASST_NR}-end/submit/${ASST_NR}/&& cp ${ASST_NR}/solution.txt solution-${i}.txt
	rm -rf ${ASST_NR}
done
