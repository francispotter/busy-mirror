.PHONY: test cover install

test:
	python3 -m unittest -v

cover:
	python3 -m coverage run --source=busy --omit busy/__main__.py -m unittest -v
	python3 -m coverage report -m

install:
	sudo pip3 install --upgrade .
