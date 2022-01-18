SHELL:=/bin/bash

include .env

VENV = venv
PYTHON = $(VENV)/bin/python3
PIP3 = $(VENV)/bin/pip3
PIP3 = $(VENV)/bin/pip
COPY = /usr/bin/rsync
GUNICORN = bin/gunicorn
RM = /usr/bin/rm


build: $(VENV)/bin/activate
	$(PYTHON) -m pip install --upgrade build
	$(PYTHON) -m build
	$(PYTHON) -m pip install dist/codeTest-*.tar.*
	$(COPY) $(VENV)/lib/python3.8/site-packages/codeTest/app.py $(VENV)/app.py
	cd codeTest/client && npm install
	cd codeTest/client && npm run build && npm run postbuild
	$(COPY) -a codeTest/static $(VENV)/


$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP3) install -r requirements.txt


clean:
	$(RM) -rf **/**/**/__pycache__
	$(RM) -rf **/**/__pycache__
	$(RM) -rf **/__pycache__
	$(RM) -rf build
	$(RM) -rf dist
	$(RM) -rf $(VENV)
	$(RM) -rf codeTest.egg-info
	$(RM) -rf codeTest/static
	$(RM) -rf codeTest/client/build
	$(RM) -rf codeTest/client/node_modules

run: $(VENV)/bin/activate
	export FLASK_APP=$(VENV)/app.py
	cd venv && $(GUNICORN) -w 4 -b 127.0.0.1:5000 app:app > /dev/null 2&>1 &


test: $(VENV)/bin/activate
	$(PYTHON) -m unittest discover -s test


.PHONY: build env run clean test