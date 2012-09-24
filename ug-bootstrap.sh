#!/bin/bash

BIN_PATH=/cad2/ece344f/cs161/bin
TEST_PATH=/cad2/ece344f/cs161-tester/

#setup the path
export PATH=$PATH:$BIN_PATH:$TEST_PATH

#goto the correct directory
echo "Entering $HOME/ece344/root"
cd $HOME/ece344/root

echo "Testing HELLO WORLD"
asst0-hello.py

echo "Testing dbflags"
asst0-dbflags.py
