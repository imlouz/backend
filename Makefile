all: install

install:
	pip install -r requirements.txt

run:
	uvicorn server:app --reload --port 8888

test:
	cd tests/ && python -m unittest 
