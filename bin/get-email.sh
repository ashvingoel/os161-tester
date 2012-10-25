#!/bin/bash

PATH=/cad2/ece344f/cs161/bin:$PATH
TOP_DIR=/cad2/ece344f
RESULTS_DIR=${TOP_DIR}/results
TESTER_DIR=${TOP_DIR}/os161-tester
BINDIR=${TESTER_DIR}/bin

pushd .
#Check if the roster file exists or not, if not, then barf

if [ ! -f ${RESULTS_DIR}/roster.csv ]; then
	echo "Roster not found"
	echo "Aborting!!!"
	popd
	return
fi

${BINDIR}/generate-email-id > ${RESULTS_DIR}/emails.txt
popd
