VERSION=$(shell grep -Po 'version = \K(\d\.\d\.\d)' setup.cfg)
VENV = .venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
PYRIGHT = $(VENV)/bin/pyright
COVERAGE = $(VENV)/bin/coverage
SPHINX = $(VENV)/bin/sphinx-build

SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = src/docs
BUILDDIR      = dist/doc

COVARAGE_SOURCES = src
TARGET=dist/sconstool_nbconvert-$(VERSION)-py3-none-any.whl

.PHONY: help clean Makefile

SOURCES = $(wildcard src/sconstool_nbconvert/*.py)

all: $(TARGET)

$(TARGET): $(VENV)/bin/activate $(SOURCES)
	$(PYTHON) -m build

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

install: $(TARGET)
	$(PIP) install --force $(TARGET)

clean:
	rm -rf dist
	rm -rf `find src -name __pycache__`
	rm -rf src/sconstool_nbconvert.egg-info
	rm -rf $(VENV)

