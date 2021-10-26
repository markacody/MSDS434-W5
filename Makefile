setup:
	python3 -m venv venv

install:
	pip install -r requirements.txt

test: 
	python -m pytest -vv --cov=MSDS434-W5 main_test.py

lint:
	pylint --disable=R,C lib 

run:
	python main.py

all: install lint test 