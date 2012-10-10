TARGET_DIR=/cad2/ece344f/os161-tester
TARGET_BIN_DIR=/cad2/ece344f/cs161/bin

BIN_FILES=os161-tester
RSYNC_FILES:=$(wildcard core/*.py) $(wildcard testing-scripts/*.py)
MARKING_DIR= marking-scripts

all: bin core

bin:
	rsync --chmod=g+w -avRC $(BIN_FILES) $(TARGET_BIN_DIR) && \
	chgrp -R e344F12 $(TARGET_BIN_DIR) && \
	chmod g+w $(TARGET_BIN_DIR)

core:
	mkdir -p $(TARGET_DIR) && \
	rsync --chmod=g+w -avRC --delete $(RSYNC_FILES) $(MARKING_DIR) $(TARGET_DIR) && \
	chmod -R o-rwx $(TARGET_DIR)/marking-scripts && \
	chgrp -R e344F12 $(TARGET_DIR) && \
	chmod g+w $(TARGET_DIR)

.PHONY: bin core
