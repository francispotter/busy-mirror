.PHONY: test cover install dist style

test:
	python3 -m unittest -v

cover:
	python3 -m coverage run --source=busy --omit busy/__main__.py -m unittest -v > /dev/null 2>&1
	python3 -m coverage report -m --fail-under 100

style:
	pycodestyle busy/**/*.py

install:
	sudo pip3 install .

dist:
	mkdir -p dist
	rm -f dist/*
	python3 setup.py sdist bdist_wheel
	twine upload dist/*
