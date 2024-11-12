# Define the Python interpreter for the virtual environment
VENV := venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

# Rule to create the virtual environment
$(VENV)/bin/activate:
	python3 -m venv $(VENV)

# Rule to install dependencies in the virtual environment
install: $(VENV)/bin/activate
	$(PIP) install -r requirements.txt

# Rule to run the program with arguments in the virtual environment
run: $(VENV)/bin/activate
	$(PYTHON) main.py $(ARGS)

# Rule to clean up the virtual environment (optional)
clean:
	rm -rf $(VENV)