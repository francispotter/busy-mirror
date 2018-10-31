.PHONY: test install

test:
	python3 -m unittest -v

install:
	sudo pip3 install --upgrade .
