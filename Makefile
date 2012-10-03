TARGET_DIR=/cad2/ece344f/os161-tester
TARGET_BIN_DIR=/cad2/ece344f/cs161/bin

BIN_FILES=os161-tester
PYTHON_FILES:=$(wildcard core/*.py) $(wildcard testing-scripts/*.py) $(wildcard marking-scripts/*.py)


all: marking bin core

marking:
	mkdir -p ($TARGET_DIR)/marking-scripts
	chmod 770 ($TARGET_DIR)/marking-scripts

bin:
	rsync -avRC $(BIN_FILES) $(TARGET_BIN_DIR)
core:
	mkdir -p $(TARGET_DIR) && rsync -avRC --delete $(PYTHON_FILES) $(TARGET_DIR)

.PHONY: bin core