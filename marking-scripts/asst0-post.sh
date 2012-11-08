#!/bin/bash

pushd .

cd ${BUILD_PATH}../asst0-end/

# copy our own printchar tester and build/install it
/bin/cp -r ${TEST_PATH}/marking-scripts/asst0-code/test_printchar testbin/
cd testbin/test_printchar && make -s && make -s install

popd
