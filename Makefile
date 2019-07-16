all: install

install:
	pip install -r requirements.txt

run:
	uvicorn server:app --reload --port 8888

test:
	cd tests/ && python -m unittest 

download:
	wget -x -nH https://imlo.s3.amazonaws.com/wordlist/latin/imlo.txt.gz

clean:
	find .|grep pyc |xargs rm -rf
