TOP_DIR=/cad2/ece344f

TESTER_DIR=$(TOP_DIR)/os161-tester
BIN_DIR=$(TOP_DIR)/cs161/bin
RESULTS_DIR=$(TOP_DIR)/results

BIN_FILES=os161-tester
RSYNC_FILES:=$(wildcard core/*.py) $(wildcard testing-scripts/*.py)
MARKING_DIR= marking-scripts

all: bin core

# run this once
# students shouldn't have access to the results directory, but
# TAs should have read-write access to it
results:
	mkdir -p $(RESULTS_DIR) && \
	chgrp e344F12 $(RESULTS_DIR) && \
	chmod o-rwx,g+w,g+s $(RESULTS_DIR) && \
	mkdir -m g+w,o-rwx -p $(RESULTS_DIR)/asst0 \
			      $(RESULTS_DIR)/asst1 \
	                      $(RESULTS_DIR)/asst2 \
			      $(RESULTS_DIR)/asst3

bin:
	rsync -avRC $(BIN_FILES) $(BIN_DIR)

# students shouldn't have access to the marking directory, but
# TAs should have read access to it
core:
	mkdir -p $(TESTER_DIR) && \
	rsync -avRC --delete $(RSYNC_FILES) $(MARKING_DIR) $(TESTER_DIR) && \
	chgrp e344F12 $(TESTER_DIR)/$(MARKING_DIR) && \
	chmod o-rwx $(TESTER_DIR)/$(MARKING_DIR)



.PHONY: bin core results
