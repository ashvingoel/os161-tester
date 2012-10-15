#!/bin/bash

# copy our own printchar tester and build/install it
if [  -G "$TEST_PATH/marking-scripts" ]; then
    /bin/cp -r $TEST_PATH/marking-scripts/asst0-code/test_printchar ../../../testbin/
    cd ../../../testbin/test_printchar && make -s && make -s install
fi

