TOP_DIR=/cad2/ece344f

TESTER_DIR=$(TOP_DIR)/os161-tester
INSTALL_BIN_DIR=$(TOP_DIR)/cs161/bin
RESULTS_DIR=$(TOP_DIR)/results
RESULTS_DIRS=$(RESULTS_DIR) \
	$(RESULTS_DIR)/asst0 \
	$(RESULTS_DIR)/asst1 \
	$(RESULTS_DIR)/asst2 \
	$(RESULTS_DIR)/asst3

DIRS=bin src scripts
TESTER_SCRIPT=$(TESTER_DIR)/bin/os161-tester

all: tester results

tester:
	mkdir -p $(TESTER_DIR) && \
	rsync -avR --delete $(DIRS) $(TESTER_DIR) && \
	chgrp -R e344F13 $(TESTER_DIR) && \
	chmod -R o-w,g+w $(TESTER_DIR) && \
	ln -sf  $(TESTER_SCRIPT) $(INSTALL_BIN_DIR)

# results directory
results:
	mkdir -p $(RESULTS_DIRS) && \
	chgrp -R e344F13 $(RESULTS_DIRS) && \
	chmod o-rwx,g+w,g+s $(RESULTS_DIRS)

.PHONY: all tester bin results
