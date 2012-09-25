#!/bin/bash

BIN_PATH=/cad2/ece344f/cs161/bin
#TEST_PATH=/cad2/ece344f/cs161-tester/
TEST_PATH=$HOME/os161-tester/

#setup the path
export PATH=$PATH:$BIN_PATH:$TEST_PATH

#goto the correct directory
echo "Entering $HOME/ece344/root"
cd $HOME/ece344/root

echo "Testing HELLO WORLD"
$TEST_PATH/core/asst0-hello.py kernel

echo "Testing dbflags"
$TEST_PATH/core/asst0-dbflags.py kernel
