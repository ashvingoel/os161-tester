#!/bin/bash

# Let's get the group data and from there we get the utorids
# and from there we get the email address and append them to one file

#Should only be run on the ug machines

LOC=/cad2/ece344f/results/
ROSTER=${LOC}/roster.csv
EMAIL=${LOC}/email-list
rm ${EMAIL}

#Total number of groups
START=1
END=39

for i in `seq -f "%03g" ${START} ${END}`
do
	#Someone could use sed/awk, but I think I just prefer this
	UTOR1=`grep os-${i} /etc/group | cut -d ":" -f 4 | cut -d "," -f1`
	UTOR2=`grep os-${i} /etc/group | cut -d ":" -f 4 | cut -d "," -f2`
	EMAIL1=`grep ${UTOR1} ${ROSTER}`
	EMAIL2=`grep ${UTOR2} ${ROSTER}`
	echo "os-${i},${EMAIL1},${EMAIL2}" >> ${EMAIL}
done
