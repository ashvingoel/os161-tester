#!/bin/bash

pushd .

cd ${BUILD_PATH}../asst2-end/

# copy our own printchar tester and build/install it
for i in `ls ${TEST_PATH}/marking-scripts/asst2-code/`
do
	pushd .
	/bin/cp -r $TEST_PATH/marking-scripts/asst0-code/$i testbin/
	cd testbin/$i && make -s && make -s install
	popd
done
