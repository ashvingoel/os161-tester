#!/bin/bash

ASST=$1
PATH=/cad2/ece344f/cs161/bin:$PATH
TOP_DIR=/cad2/ece344f
RESULTS_DIR=${TOP_DIR}/results
ASST_DIR=${RESULTS_DIR}/asst${ASST}
TESTER_DIR=${TOP_DIR}/os161-tester
BINDIR=${TESTER_DIR}/bin

pushd .
cd ${ASST_DIR}
${BINDIR}/mail.py ${ASST}
popd

##This can be removed after testing
#cp ${ASST_DIR}/test.mbox .
#mutt -f test.mbox
