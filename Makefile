.PHONY: test install

test:
	python3 -m coverage run --source=busy -m unittest -v
	python3 -m coverage report

install:
	sudo pip3 install --upgrade .
