setup:
	python3 -m venv ~/.MSDS434-W5

install:
	pip install -r requirements.txt

test: 
	python -m pytest -vv --cov=MSDS434-W5 tests/*.py

lint:
	pylint --disable=R,C lib 

all: install lint test 