# Define the Python interpreter for the virtual environment
VENV := venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

# creates the virtual environment
$(VENV)/bin/activate:
	python3 -m venv $(VENV)

# installs dependencies in the virtual environment
install: $(VENV)/bin/activate
	$(PIP) install -r requirements.txt

# runs the program with arguments in the virtual environment
run: $(VENV)/bin/activate
	$(PYTHON) main.py $(ARGS)

# cleans up the virtual environment
clean:
	rm -rf $(VENV)