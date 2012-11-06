TOP_DIR=/cad2/ece344f

TESTER_DIR=$(TOP_DIR)/os161-tester
INSTALL_BIN_DIR=$(TOP_DIR)/cs161/bin
RESULTS_DIR=$(TOP_DIR)/results

BIN_DIR=bin
MARKING_DIR=marking-scripts
OTHER_DIRS=core testing-scripts sysconfig
TESTER_SCRIPT=$(TESTER_DIR)/$(BIN_DIR)/os161-tester

# students shouldn't have access to the marking directory, but
# TAs should have read access to it
all: bin
	mkdir -p $(TESTER_DIR) && \
	rsync -avR --delete $(BIN_DIR) $(MARKING_DIR) $(OTHER_DIRS) $(TESTER_DIR) && \
	chgrp e344F12 $(TESTER_DIR)/$(MARKING_DIR) && \
	chmod o-rwx $(TESTER_DIR)/$(MARKING_DIR)

bin:
	ln -sf  $(TESTER_SCRIPT) $(INSTALL_BIN_DIR)


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
			      $(RESULTS_DIR)/asst3 && \
	cp templates/design-marks-format.csv templates/roster.csv $(RESULTS_DIR)


.PHONY: all bin results
