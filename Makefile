run:
	python app.py

test:
	python -m unittest discover -s tests

lint:
	flake8 .

coverage:
	coverage run -m unittest discover -s tests
	coverage report -m

trivy:
	trivy fs .
